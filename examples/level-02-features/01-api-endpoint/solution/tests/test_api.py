"""
Comprehensive tests for User Management API.

These tests verify that the API correctly handles:
- Successful requests
- Validation errors
- Not found errors
- Edge cases
"""

import pytest
from flask import Flask
from main import app, user_store, UserCreate, UserResponse, ErrorResponse


@pytest.fixture
def client():
    """Create a test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Clear store before each test
        user_store._users.clear()
        user_store._next_id = 1
        yield client


class TestCreateUser:
    """Test user creation endpoint."""
    
    def test_create_user_success(self, client):
        """Test successful user creation."""
        response = client.post('/api/users', json={
            'name': 'Alice Smith',
            'email': 'alice@example.com',
            'age': 25
        })
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['id'] == 1
        assert data['name'] == 'Alice Smith'
        assert data['email'] == 'alice@example.com'
        assert data['age'] == 25
    
    def test_create_user_with_default_age(self, client):
        """Test user creation with default age."""
        response = client.post('/api/users', json={
            'name': 'Bob Jones',
            'email': 'bob@example.com'
        })
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['age'] == 0  # Default age
    
    def test_create_user_missing_name(self, client):
        """Test validation error when name is missing."""
        response = client.post('/api/users', json={
            'email': 'alice@example.com'
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert data['error'] == 'ValidationError'
        assert 'name' in data['message'].lower()
    
    def test_create_user_missing_email(self, client):
        """Test validation error when email is missing."""
        response = client.post('/api/users', json={
            'name': 'Alice Smith'
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert data['error'] == 'ValidationError'
        assert 'email' in data['message'].lower()
    
    def test_create_user_invalid_email(self, client):
        """Test validation error with invalid email format."""
        response = client.post('/api/users', json={
            'name': 'Alice Smith',
            'email': 'not-an-email'
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert data['error'] == 'ValidationError'
        assert 'email' in data['message'].lower()
    
    def test_create_user_name_too_long(self, client):
        """Test validation error when name exceeds max length."""
        response = client.post('/api/users', json={
            'name': 'A' * 101,  # Exceeds max_length=100
            'email': 'alice@example.com'
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert data['error'] == 'ValidationError'
    
    def test_create_user_age_out_of_range(self, client):
        """Test validation error when age is out of range."""
        response = client.post('/api/users', json={
            'name': 'Alice Smith',
            'email': 'alice@example.com',
            'age': 200  # Exceeds max age=150
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert data['error'] == 'ValidationError'
    
    def test_create_user_negative_age(self, client):
        """Test validation error when age is negative."""
        response = client.post('/api/users', json={
            'name': 'Alice Smith',
            'email': 'alice@example.com',
            'age': -1
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert data['error'] == 'ValidationError'
    
    def test_create_user_duplicate_email(self, client):
        """Test error when creating user with duplicate email."""
        # Create first user
        client.post('/api/users', json={
            'name': 'Alice Smith',
            'email': 'alice@example.com',
            'age': 25
        })
        
        # Try to create duplicate
        response = client.post('/api/users', json={
            'name': 'Alice Johnson',
            'email': 'alice@example.com',
            'age': 30
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert data['error'] == 'ValidationError'
        assert 'already exists' in data['message']
    
    def test_create_user_not_json(self, client):
        """Test error when request is not JSON."""
        response = client.post('/api/users', data='not json')
        
        assert response.status_code == 400
        data = response.get_json()
        assert data['error'] == 'ValidationError'


class TestGetUsers:
    """Test get all users endpoint."""
    
    def test_get_users_empty(self, client):
        """Test getting users when none exist."""
        response = client.get('/api/users')
        
        assert response.status_code == 200
        data = response.get_json()
        assert data == []
    
    def test_get_users_with_data(self, client):
        """Test getting all users."""
        # Create users
        client.post('/api/users', json={
            'name': 'Alice Smith',
            'email': 'alice@example.com',
            'age': 25
        })
        client.post('/api/users', json={
            'name': 'Bob Jones',
            'email': 'bob@example.com',
            'age': 30
        })
        
        response = client.get('/api/users')
        
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 2
        assert data[0]['name'] == 'Alice Smith'
        assert data[1]['name'] == 'Bob Jones'


class TestGetUser:
    """Test get user by ID endpoint."""
    
    def test_get_user_success(self, client):
        """Test successful user retrieval."""
        # Create user
        create_response = client.post('/api/users', json={
            'name': 'Alice Smith',
            'email': 'alice@example.com',
            'age': 25
        })
        user_id = create_response.get_json()['id']
        
        # Get user
        response = client.get(f'/api/users/{user_id}')
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['id'] == user_id
        assert data['name'] == 'Alice Smith'
    
    def test_get_user_not_found(self, client):
        """Test error when user doesn't exist."""
        response = client.get('/api/users/999')
        
        assert response.status_code == 404
        data = response.get_json()
        assert data['error'] == 'NotFound'
        assert 'not found' in data['message'].lower()


class TestUpdateUser:
    """Test update user endpoint."""
    
    def test_update_user_success(self, client):
        """Test successful user update."""
        # Create user
        create_response = client.post('/api/users', json={
            'name': 'Alice Smith',
            'email': 'alice@example.com',
            'age': 25
        })
        user_id = create_response.get_json()['id']
        
        # Update user
        response = client.put(f'/api/users/{user_id}', json={
            'name': 'Alice Johnson',
            'age': 26
        })
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['name'] == 'Alice Johnson'
        assert data['age'] == 26
        assert data['email'] == 'alice@example.com'  # Unchanged
    
    def test_update_user_not_found(self, client):
        """Test error when updating non-existent user."""
        response = client.put('/api/users/999', json={
            'name': 'Alice Johnson'
        })
        
        assert response.status_code == 404
        data = response.get_json()
        assert data['error'] == 'NotFound'
    
    def test_update_user_invalid_email(self, client):
        """Test validation error with invalid email."""
        # Create user
        create_response = client.post('/api/users', json={
            'name': 'Alice Smith',
            'email': 'alice@example.com',
            'age': 25
        })
        user_id = create_response.get_json()['id']
        
        # Try to update with invalid email
        response = client.put(f'/api/users/{user_id}', json={
            'email': 'not-an-email'
        })
        
        assert response.status_code == 400
        data = response.get_json()
        assert data['error'] == 'ValidationError'


class TestDeleteUser:
    """Test delete user endpoint."""
    
    def test_delete_user_success(self, client):
        """Test successful user deletion."""
        # Create user
        create_response = client.post('/api/users', json={
            'name': 'Alice Smith',
            'email': 'alice@example.com',
            'age': 25
        })
        user_id = create_response.get_json()['id']
        
        # Delete user
        response = client.delete(f'/api/users/{user_id}')
        
        assert response.status_code == 200
        data = response.get_json()
        assert 'deleted' in data['message'].lower()
        
        # Verify user is deleted
        get_response = client.get(f'/api/users/{user_id}')
        assert get_response.status_code == 404
    
    def test_delete_user_not_found(self, client):
        """Test error when deleting non-existent user."""
        response = client.delete('/api/users/999')
        
        assert response.status_code == 404
        data = response.get_json()
        assert data['error'] == 'NotFound'


class TestErrorHandling:
    """Test error handling consistency."""
    
    def test_error_response_structure(self, client):
        """Test that all errors return consistent structure."""
        # Test validation error
        response = client.post('/api/users', json={})
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
        assert 'message' in data
        assert 'status_code' in data
        
        # Test not found error
        response = client.get('/api/users/999')
        assert response.status_code == 404
        data = response.get_json()
        assert 'error' in data
        assert 'message' in data
        assert 'status_code' in data


class TestHealthCheck:
    """Test health check endpoint."""
    
    def test_health_check(self, client):
        """Test health check endpoint."""
        response = client.get('/health')
        
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'healthy'


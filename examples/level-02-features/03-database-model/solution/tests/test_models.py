"""
Comprehensive tests for database models.

These tests verify that models correctly handle:
- Field validation
- Relationships
- Constraints
- Model methods
- Data integrity
"""

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils import timezone
from models import User, Post, Comment


@pytest.mark.django_db
class TestUserModel:
    """Test User model."""
    
    def test_create_user_success(self):
        """Test successful user creation."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        assert user.id is not None
        assert user.email == 'alice@example.com'
        assert user.name == 'Alice Smith'
        assert user.age == 25
        assert user.created_at is not None
        assert user.updated_at is not None
    
    def test_user_str_representation(self):
        """Test user string representation."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        assert str(user) == 'Alice Smith (alice@example.com)'
    
    def test_user_email_unique(self):
        """Test that email must be unique."""
        User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        with pytest.raises(IntegrityError):
            User.objects.create(
                email='alice@example.com',
                name='Alice Johnson',
                age=30
            )
    
    def test_user_age_validation(self):
        """Test age validation."""
        # Test negative age
        user = User(email='alice@example.com', name='Alice', age=-1)
        with pytest.raises(ValidationError):
            user.full_clean()
        
        # Test age too high
        user = User(email='alice@example.com', name='Alice', age=200)
        with pytest.raises(ValidationError):
            user.full_clean()
    
    def test_user_is_adult_property(self):
        """Test is_adult property."""
        adult = User.objects.create(
            email='adult@example.com',
            name='Adult User',
            age=18
        )
        
        child = User.objects.create(
            email='child@example.com',
            name='Child User',
            age=17
        )
        
        assert adult.is_adult is True
        assert child.is_adult is False
    
    def test_user_post_count(self):
        """Test post_count property."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        assert user.post_count == 0
        
        Post.objects.create(
            title='Test Post',
            content='Content',
            author=user
        )
        
        assert user.post_count == 1


@pytest.mark.django_db
class TestPostModel:
    """Test Post model."""
    
    def test_create_post_success(self):
        """Test successful post creation."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post = Post.objects.create(
            title='My First Post',
            content='This is the content of my first post.',
            author=user
        )
        
        assert post.id is not None
        assert post.title == 'My First Post'
        assert post.content == 'This is the content of my first post.'
        assert post.author == user
        assert post.created_at is not None
    
    def test_post_str_representation(self):
        """Test post string representation."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post = Post.objects.create(
            title='My First Post',
            content='Content',
            author=user
        )
        
        assert str(post) == 'My First Post by Alice Smith'
    
    def test_post_cascade_delete(self):
        """Test that deleting user deletes posts."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post = Post.objects.create(
            title='Test Post',
            content='Content',
            author=user
        )
        
        post_id = post.id
        user.delete()
        
        assert not Post.objects.filter(id=post_id).exists()
    
    def test_post_word_count(self):
        """Test word_count property."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post = Post.objects.create(
            title='Test Post',
            content='This is a test post with multiple words.',
            author=user
        )
        
        assert post.word_count == 8
    
    def test_post_comment_count(self):
        """Test comment_count property."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post = Post.objects.create(
            title='Test Post',
            content='Content',
            author=user
        )
        
        assert post.comment_count == 0
        
        Comment.objects.create(
            post=post,
            author=user,
            content='Test comment'
        )
        
        assert post.comment_count == 1


@pytest.mark.django_db
class TestCommentModel:
    """Test Comment model."""
    
    def test_create_comment_success(self):
        """Test successful comment creation."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post = Post.objects.create(
            title='Test Post',
            content='Content',
            author=user
        )
        
        comment = Comment.objects.create(
            post=post,
            author=user,
            content='This is a test comment.'
        )
        
        assert comment.id is not None
        assert comment.post == post
        assert comment.author == user
        assert comment.content == 'This is a test comment.'
        assert comment.created_at is not None
    
    def test_comment_str_representation(self):
        """Test comment string representation."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post = Post.objects.create(
            title='Test Post',
            content='Content',
            author=user
        )
        
        comment = Comment.objects.create(
            post=post,
            author=user,
            content='Test comment'
        )
        
        assert 'Alice Smith' in str(comment)
        assert 'Test Post' in str(comment)
    
    def test_comment_cascade_delete_on_post(self):
        """Test that deleting post deletes comments."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post = Post.objects.create(
            title='Test Post',
            content='Content',
            author=user
        )
        
        comment = Comment.objects.create(
            post=post,
            author=user,
            content='Test comment'
        )
        
        comment_id = comment.id
        post.delete()
        
        assert not Comment.objects.filter(id=comment_id).exists()
    
    def test_comment_cascade_delete_on_user(self):
        """Test that deleting user deletes comments."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post = Post.objects.create(
            title='Test Post',
            content='Content',
            author=user
        )
        
        comment = Comment.objects.create(
            post=post,
            author=user,
            content='Test comment'
        )
        
        comment_id = comment.id
        user.delete()
        
        assert not Comment.objects.filter(id=comment_id).exists()
    
    def test_comment_word_count(self):
        """Test word_count property."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post = Post.objects.create(
            title='Test Post',
            content='Content',
            author=user
        )
        
        comment = Comment.objects.create(
            post=post,
            author=user,
            content='This is a test comment with multiple words.'
        )
        
        assert comment.word_count == 8


@pytest.mark.django_db
class TestRelationships:
    """Test model relationships."""
    
    def test_user_posts_relationship(self):
        """Test user.posts reverse relationship."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post1 = Post.objects.create(
            title='Post 1',
            content='Content 1',
            author=user
        )
        
        post2 = Post.objects.create(
            title='Post 2',
            content='Content 2',
            author=user
        )
        
        assert user.posts.count() == 2
        assert post1 in user.posts.all()
        assert post2 in user.posts.all()
    
    def test_post_comments_relationship(self):
        """Test post.comments reverse relationship."""
        user = User.objects.create(
            email='alice@example.com',
            name='Alice Smith',
            age=25
        )
        
        post = Post.objects.create(
            title='Test Post',
            content='Content',
            author=user
        )
        
        comment1 = Comment.objects.create(
            post=post,
            author=user,
            content='Comment 1'
        )
        
        comment2 = Comment.objects.create(
            post=post,
            author=user,
            content='Comment 2'
        )
        
        assert post.comments.count() == 2
        assert comment1 in post.comments.all()
        assert comment2 in post.comments.all()


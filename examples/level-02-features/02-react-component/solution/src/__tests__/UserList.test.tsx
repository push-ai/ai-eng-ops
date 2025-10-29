/**
 * Tests for UserList component.
 * 
 * Verifies component behavior, error handling, loading states, and user interactions.
 */

import React from 'react';
import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import UserList from '../UserList';
import { User } from '../types';

// Mock fetch globally
global.fetch = jest.fn();

describe('UserList', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('Loading State', () => {
    it('shows loading indicator when fetching users', async () => {
      (global.fetch as jest.Mock).mockImplementation(() =>
        new Promise(() => {}) // Never resolves
      );

      render(<UserList />);

      expect(screen.getByTestId('user-list-loading')).toBeInTheDocument();
      expect(screen.getByText('Loading users...')).toBeInTheDocument();
    });
  });

  describe('Error State', () => {
    it('displays error message when API call fails', async () => {
      (global.fetch as jest.Mock).mockRejectedValueOnce(
        new Error('Network error')
      );

      render(<UserList />);

      await waitFor(() => {
        expect(screen.getByTestId('user-list-error')).toBeInTheDocument();
        expect(screen.getByText(/Error Loading Users/i)).toBeInTheDocument();
        expect(screen.getByText('Network error')).toBeInTheDocument();
      });
    });

    it('displays error message when API returns error status', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: false,
        status: 500,
        json: async () => ({
          error: 'InternalError',
          message: 'Server error',
          status_code: 500
        })
      });

      render(<UserList />);

      await waitFor(() => {
        expect(screen.getByTestId('user-list-error')).toBeInTheDocument();
        expect(screen.getByText('Server error')).toBeInTheDocument();
      });
    });

    it('allows retry after error', async () => {
      (global.fetch as jest.Mock)
        .mockRejectedValueOnce(new Error('Network error'))
        .mockResolvedValueOnce({
          ok: true,
          json: async () => []
        });

      render(<UserList />);

      await waitFor(() => {
        expect(screen.getByText('Retry')).toBeInTheDocument();
      });

      fireEvent.click(screen.getByText('Retry'));

      await waitFor(() => {
        expect(global.fetch).toHaveBeenCalledTimes(2);
      });
    });
  });

  describe('Success State', () => {
    const mockUsers: User[] = [
      { id: 1, name: 'Alice Smith', email: 'alice@example.com', age: 25 },
      { id: 2, name: 'Bob Jones', email: 'bob@example.com', age: 30 }
    ];

    it('displays list of users when API call succeeds', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => mockUsers
      });

      render(<UserList />);

      await waitFor(() => {
        expect(screen.getByText('Alice Smith')).toBeInTheDocument();
        expect(screen.getByText('alice@example.com')).toBeInTheDocument();
        expect(screen.getByText('Bob Jones')).toBeInTheDocument();
        expect(screen.getByText('bob@example.com')).toBeInTheDocument();
      });
    });

    it('displays empty state when no users exist', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => []
      });

      render(<UserList />);

      await waitFor(() => {
        expect(screen.getByTestId('user-list-empty')).toBeInTheDocument();
        expect(screen.getByText('No users found.')).toBeInTheDocument();
      });
    });
  });

  describe('User Interactions', () => {
    const mockUsers: User[] = [
      { id: 1, name: 'Alice Smith', email: 'alice@example.com', age: 25 }
    ];

    it('calls onUserSelect when user is clicked', async () => {
      const onUserSelect = jest.fn();

      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => mockUsers
      });

      render(<UserList onUserSelect={onUserSelect} />);

      await waitFor(() => {
        expect(screen.getByText('Alice Smith')).toBeInTheDocument();
      });

      fireEvent.click(screen.getByText('Alice Smith'));

      expect(onUserSelect).toHaveBeenCalledWith(mockUsers[0]);
    });

    it('handles keyboard navigation', async () => {
      const onUserSelect = jest.fn();

      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => mockUsers
      });

      render(<UserList onUserSelect={onUserSelect} />);

      await waitFor(() => {
        expect(screen.getByText('Alice Smith')).toBeInTheDocument();
      });

      const userItem = screen.getByText('Alice Smith').closest('li');
      if (userItem) {
        fireEvent.keyDown(userItem, { key: 'Enter' });
        expect(onUserSelect).toHaveBeenCalledWith(mockUsers[0]);
      }
    });
  });

  describe('Delete Functionality', () => {
    const mockUsers: User[] = [
      { id: 1, name: 'Alice Smith', email: 'alice@example.com', age: 25 }
    ];

    beforeEach(() => {
      // Mock window.confirm
      window.confirm = jest.fn(() => true);
    });

    it('shows delete button when showActions is true', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => mockUsers
      });

      render(<UserList showActions={true} />);

      await waitFor(() => {
        expect(screen.getByText('Alice Smith')).toBeInTheDocument();
      });

      expect(screen.getByLabelText('Delete Alice Smith')).toBeInTheDocument();
    });

    it('does not show delete button when showActions is false', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => mockUsers
      });

      render(<UserList showActions={false} />);

      await waitFor(() => {
        expect(screen.getByText('Alice Smith')).toBeInTheDocument();
      });

      expect(screen.queryByLabelText('Delete Alice Smith')).not.toBeInTheDocument();
    });

    it('deletes user when delete button is clicked', async () => {
      (global.fetch as jest.Mock)
        .mockResolvedValueOnce({
          ok: true,
          json: async () => mockUsers
        })
        .mockResolvedValueOnce({
          ok: true,
          json: async () => ({
            message: 'User deleted successfully'
          })
        })
        .mockResolvedValueOnce({
          ok: true,
          json: async () => []
        });

      render(<UserList showActions={true} />);

      await waitFor(() => {
        expect(screen.getByText('Alice Smith')).toBeInTheDocument();
      });

      const deleteButton = screen.getByLabelText('Delete Alice Smith');
      fireEvent.click(deleteButton);

      await waitFor(() => {
        expect(global.fetch).toHaveBeenCalledWith('/api/users/1', {
          method: 'DELETE'
        });
      });
    });

    it('does not delete when confirmation is cancelled', async () => {
      window.confirm = jest.fn(() => false);

      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => mockUsers
      });

      render(<UserList showActions={true} />);

      await waitFor(() => {
        expect(screen.getByText('Alice Smith')).toBeInTheDocument();
      });

      const deleteButton = screen.getByLabelText('Delete Alice Smith');
      fireEvent.click(deleteButton);

      expect(global.fetch).toHaveBeenCalledTimes(1); // Only initial fetch
    });
  });

  describe('Props', () => {
    it('applies custom className', async () => {
      (global.fetch as jest.Mock).mockResolvedValueOnce({
        ok: true,
        json: async () => []
      });

      const { container } = render(<UserList className="custom-class" />);

      await waitFor(() => {
        expect(container.querySelector('.user-list.custom-class')).toBeInTheDocument();
      });
    });
  });
});


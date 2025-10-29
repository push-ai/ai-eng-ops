/**
 * UserList Component
 * 
 * Displays a list of users with loading states, error handling, and actions.
 * Demonstrates proper TypeScript usage, error boundaries, and component structure.
 */

import React, { useState, useEffect, useCallback } from 'react';
import { User, ApiError, LoadingState } from './types';
import './UserList.css';

/**
 * Props for UserList component.
 */
export interface UserListProps {
  /** Callback when a user is selected */
  onUserSelect?: (user: User) => void;
  /** Whether to show action buttons (delete, edit, etc.) */
  showActions?: boolean;
  /** Custom CSS class name */
  className?: string;
}

/**
 * UserList Component
 * 
 * Fetches and displays a list of users from the API.
 * Handles loading states, errors, and user interactions.
 * 
 * @param props - Component props
 * @returns UserList component
 * 
 * @example
 * ```tsx
 * <UserList 
 *   onUserSelect={(user) => console.log(user)}
 *   showActions={true}
 * />
 * ```
 */
const UserList: React.FC<UserListProps> = ({
  onUserSelect,
  showActions = false,
  className = ''
}) => {
  // State management with explicit types
  const [users, setUsers] = useState<User[]>([]);
  const [loadingState, setLoadingState] = useState<LoadingState>('idle');
  const [error, setError] = useState<string | null>(null);

  /**
   * Fetches users from the API.
   * Handles loading states and errors properly.
   */
  const fetchUsers = useCallback(async () => {
    setLoadingState('loading');
    setError(null);

    try {
      const response = await fetch('/api/users');

      if (!response.ok) {
        // Handle API errors
        const errorData: ApiError = await response.json();
        throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
      }

      const data: User[] = await response.json();
      setUsers(data);
      setLoadingState('success');
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to fetch users';
      setError(errorMessage);
      setLoadingState('error');
    }
  }, []);

  // Fetch users on component mount
  useEffect(() => {
    fetchUsers();
  }, [fetchUsers]);

  /**
   * Handles user deletion.
   * 
   * @param userId - ID of the user to delete
   */
  const handleDelete = useCallback(async (userId: number) => {
    if (!window.confirm('Are you sure you want to delete this user?')) {
      return;
    }

    setLoadingState('loading');
    setError(null);

    try {
      const response = await fetch(`/api/users/${userId}`, {
        method: 'DELETE'
      });

      if (!response.ok) {
        const errorData: ApiError = await response.json();
        throw new Error(errorData.message || `Failed to delete user: ${userId}`);
      }

      // Refresh user list after deletion
      await fetchUsers();
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to delete user';
      setError(errorMessage);
      setLoadingState('error');
    }
  }, [fetchUsers]);

  /**
   * Handles user selection.
   * 
   * @param user - Selected user
   */
  const handleUserClick = useCallback((user: User) => {
    if (onUserSelect) {
      onUserSelect(user);
    }
  }, [onUserSelect]);

  // Render loading state
  if (loadingState === 'loading' && users.length === 0) {
    return (
      <div className={`user-list loading ${className}`} data-testid="user-list-loading">
        <div className="spinner" aria-label="Loading users">Loading users...</div>
      </div>
    );
  }

  // Render error state
  if (loadingState === 'error' && users.length === 0) {
    return (
      <div className={`user-list error ${className}`} data-testid="user-list-error">
        <div className="error-message" role="alert">
          <h3>Error Loading Users</h3>
          <p>{error || 'An unknown error occurred'}</p>
          <button onClick={fetchUsers} className="retry-button">
            Retry
          </button>
        </div>
      </div>
    );
  }

  // Render user list
  return (
    <div className={`user-list ${className}`} data-testid="user-list">
      {error && (
        <div className="error-banner" role="alert">
          {error}
          <button onClick={() => setError(null)} className="dismiss-button">×</button>
        </div>
      )}

      <h1>Users</h1>

      {users.length === 0 ? (
        <div className="empty-state" data-testid="user-list-empty">
          <p>No users found.</p>
        </div>
      ) : (
        <ul className="user-list-items">
          {users.map((user) => (
            <li 
              key={user.id} 
              className="user-item"
              onClick={() => handleUserClick(user)}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                  e.preventDefault();
                  handleUserClick(user);
                }
              }}
            >
              <div className="user-info">
                <span className="user-name">{user.name}</span>
                <span className="user-email">{user.email}</span>
                <span className="user-age">Age: {user.age}</span>
              </div>
              {showActions && (
                <div className="user-actions">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleDelete(user.id);
                    }}
                    className="delete-button"
                    aria-label={`Delete ${user.name}`}
                  >
                    Delete
                  </button>
                </div>
              )}
            </li>
          ))}
        </ul>
      )}

      {loadingState === 'loading' && users.length > 0 && (
        <div className="loading-indicator">Refreshing...</div>
      )}
    </div>
  );
};

export default UserList;


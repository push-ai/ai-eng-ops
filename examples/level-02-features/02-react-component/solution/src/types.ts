/**
 * Type definitions for User Management components.
 * 
 * These types define the contracts used throughout the application,
 * enabling type safety and AI understanding of data structures.
 */

/**
 * User data structure.
 * 
 * Represents a user in the system with all required fields.
 * Used for API responses and component props.
 */
export interface User {
  /** Unique user identifier */
  id: number;
  /** User's full name */
  name: string;
  /** User's email address */
  email: string;
  /** User's age (0-150) */
  age: number;
}

/**
 * API Error response structure.
 * 
 * Standard error format returned by the API.
 */
export interface ApiError {
  /** Error type or code */
  error: string;
  /** Human-readable error message */
  message: string;
  /** HTTP status code */
  status_code: number;
}

/**
 * Loading state for async operations.
 */
export type LoadingState = 'idle' | 'loading' | 'success' | 'error';


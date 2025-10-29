/**
 * UserForm component using shared types.
 * 
 * Uses types from shared/types.ts which are generated from backend types,
 * ensuring consistency across frontend and backend.
 */

import React, { useState } from 'react';
import { UserCreate, UserResponse } from './shared/types';

function UserForm() {
  const [user, setUser] = useState<UserResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const formData = new FormData(e.currentTarget);
    
    // Use shared UserCreate type
    const userData: UserCreate = {
      name: formData.get('name') as string,
      email: formData.get('email') as string,
      age: formData.get('age') ? parseInt(formData.get('age') as string) : undefined
    };

    try {
      const response = await fetch('/api/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData)
      });

      if (!response.ok) {
        throw new Error('Failed to create user');
      }

      const data: UserResponse = await response.json();
      setUser(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" placeholder="Name" required />
      <input name="email" type="email" placeholder="Email" required />
      <input name="age" type="number" min="0" max="150" placeholder="Age (optional)" />
      <button type="submit" disabled={loading}>
        {loading ? 'Creating...' : 'Create User'}
      </button>
      {error && <div className="error">{error}</div>}
      {user && (
        <div className="success">
          Created: {user.name} ({user.email}) - Age: {user.age}
        </div>
      )}
    </form>
  );
}

export default UserForm;


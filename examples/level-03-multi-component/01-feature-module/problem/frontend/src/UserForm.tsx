// Frontend defines its own user structure - no shared types
import React, { useState } from 'react';

interface User {
  id: number;
  name: string;
  email: string;
  age?: number;  // Different from backend!
}

function UserForm() {
  const [user, setUser] = useState<User | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const formData = new FormData(e.target as HTMLFormElement);
    
    const response = await fetch('/api/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: formData.get('name'),
        email: formData.get('email'),
        age: formData.get('age')  // May not match backend expectations
      })
    });
    
    const data = await response.json();
    setUser(data);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" placeholder="Name" />
      <input name="email" placeholder="Email" />
      <input name="age" type="number" placeholder="Age" />
      <button type="submit">Create User</button>
      {user && <div>Created: {user.name}</div>}
    </form>
  );
}

export default UserForm;


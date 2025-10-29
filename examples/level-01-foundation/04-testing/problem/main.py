"""
A simple user authentication module.
This example demonstrates code that lacks comprehensive testing.
"""


class UserAuthenticator:
    """Handles user authentication operations."""
    
    def __init__(self):
        self.users = {}
        self.min_password_length = 6
    
    def register_user(self, username, password, email):
        """Register a new user."""
        if username in self.users:
            return False, "Username already exists"
        
        if len(password) < self.min_password_length:
            return False, "Password too short"
        
        self.users[username] = {
            'password': password,
            'email': email,
            'active': True
        }
        return True, "User registered successfully"
    
    def authenticate(self, username, password):
        """Authenticate a user."""
        if username not in self.users:
            return False, "User not found"
        
        user = self.users[username]
        if not user['active']:
            return False, "User account is inactive"
        
        if user['password'] != password:
            return False, "Invalid password"
        
        return True, "Authentication successful"
    
    def deactivate_user(self, username):
        """Deactivate a user account."""
        if username in self.users:
            self.users[username]['active'] = False
            return True
        return False


# Example usage
if __name__ == "__main__":
    auth = UserAuthenticator()
    
    # Register a user
    success, message = auth.register_user("alice", "password123", "alice@example.com")
    print(f"Register: {success} - {message}")
    
    # Authenticate the user
    success, message = auth.authenticate("alice", "password123")
    print(f"Authenticate: {success} - {message}")
    
    # Try wrong password
    success, message = auth.authenticate("alice", "wrong")
    print(f"Wrong password: {success} - {message}")


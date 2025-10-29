"""
A simple user authentication module with comprehensive error handling.
This improved version addresses edge cases identified through testing.
"""


class UserAuthenticator:
    """Handles user authentication operations."""
    
    def __init__(self):
        self.users = {}
        self.min_password_length = 6
        self.max_password_length = 128
        self.max_username_length = 50
    
    def register_user(self, username, password, email):
        """Register a new user."""
        # Validate inputs
        if not username or not isinstance(username, str):
            return False, "Username is required"
        
        username = username.strip()
        if not username:
            return False, "Username cannot be empty"
        
        if len(username) > self.max_username_length:
            return False, f"Username too long (max {self.max_username_length} characters)"
        
        if username in self.users:
            return False, "Username already exists"
        
        if not password or not isinstance(password, str):
            return False, "Password is required"
        
        password = password.strip()
        if len(password) < self.min_password_length:
            return False, f"Password too short (minimum {self.min_password_length} characters)"
        
        if len(password) > self.max_password_length:
            return False, f"Password too long (max {self.max_password_length} characters)"
        
        if not email or not isinstance(email, str):
            return False, "Email is required"
        
        email = email.strip()
        if '@' not in email:
            return False, "Invalid email format"
        
        self.users[username] = {
            'password': password,
            'email': email,
            'active': True
        }
        return True, "User registered successfully"
    
    def authenticate(self, username, password):
        """Authenticate a user."""
        if not username or not isinstance(username, str):
            return False, "Username is required"
        
        username = username.strip()
        
        if not password or not isinstance(password, str):
            return False, "Password is required"
        
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
        if not username or not isinstance(username, str):
            return False
        
        username = username.strip()
        if username in self.users:
            self.users[username]['active'] = False
            return True
        return False
    
    def activate_user(self, username):
        """Activate a user account."""
        if not username or not isinstance(username, str):
            return False
        
        username = username.strip()
        if username in self.users:
            self.users[username]['active'] = True
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


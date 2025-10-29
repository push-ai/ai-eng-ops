"""
Legacy code without structure.

This demonstrates code that works but is difficult for AI to understand and modify
due to lack of structure, type hints, tests, and documentation.
"""

class UserManager:
    def __init__(self):
        self.users = {}
        self.id_counter = 0
    
    def add_user(self, name, email, age):
        self.id_counter += 1
        user = {
            'id': self.id_counter,
            'name': name,
            'email': email,
            'age': age
        }
        self.users[self.id_counter] = user
        return user
    
    def get_user(self, user_id):
        return self.users.get(user_id)
    
    def update_user(self, user_id, name=None, email=None, age=None):
        if user_id not in self.users:
            return None
        user = self.users[user_id]
        if name:
            user['name'] = name
        if email:
            user['email'] = email
        if age:
            user['age'] = age
        return user
    
    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

# Usage
if __name__ == '__main__':
    manager = UserManager()
    user = manager.add_user('Alice', 'alice@example.com', 25)
    print(user)
    updated = manager.update_user(user['id'], age=26)
    print(updated)


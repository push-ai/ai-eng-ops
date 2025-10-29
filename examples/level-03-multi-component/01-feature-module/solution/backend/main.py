"""
Backend API using shared types.

Backend imports types from shared module, ensuring consistency with frontend.
"""

from flask import Flask, request, jsonify
import sys
from pathlib import Path

# Add shared directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'shared'))

from types import UserCreate, UserResponse

app = Flask(__name__)

users = []
next_id = 1

@app.route('/api/users', methods=['POST'])
def create_user():
    """Create user using shared UserCreate type."""
    try:
        user_data = UserCreate(**request.json)
        
        user = UserResponse(
            id=next_id,
            name=user_data.name,
            email=str(user_data.email),
            age=user_data.age
        )
        users.append(user)
        next_id += 1
        
        return jsonify(user.dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user using shared UserResponse type."""
    for user in users:
        if user.id == user_id:
            return jsonify(user.dict()), 200
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)


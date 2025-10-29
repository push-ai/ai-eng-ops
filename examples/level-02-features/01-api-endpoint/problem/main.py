"""
Basic API endpoint example without proper structure.
This demonstrates common issues with AI-generated API code.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory storage
users = []
next_id = 1

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    global next_id
    
    user = {
        'id': next_id,
        'name': data['name'],
        'email': data['email'],
        'age': data.get('age', 0)
    }
    users.append(user)
    next_id += 1
    return jsonify(user), 201

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for user in users:
        if user['id'] == user_id:
            user.update(data)
            return jsonify(user)
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'Deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)


"""
Backend API without shared types.
Frontend and backend define types separately, causing inconsistencies.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Backend defines its own user structure
users = []

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email'],
        'age': data.get('age', 0)
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)


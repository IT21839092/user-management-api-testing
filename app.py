from flask import Flask, jsonify, request
import os
app =Flask(__name__)

#Simulated database
users = {}

#GETall users or aspecific user
@app.route('/users', methods=['GET'])
def get_users():
    user_id = request.args.get('id')
    if user_id:
        user = users.get(user_id)
        if user:
            return jsonify({'id': user_id, 'details': user}), 200
        return jsonify({'error': 'User not found'}), 404
    return jsonify(users), 200

#POSTtoaddanewuser
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = data.get('id')
    if user_id in users:
        return jsonify({'error': 'User already exists'}), 400
    users[user_id] = data.get('details')
    return jsonify({'message': 'User added successfully'}), 201

#PUTtoupdateauser
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.json
    users[user_id] = data.get('details')
    return jsonify({'message': 'User updated successfully'}), 200

#DELETEtoremoveauser
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    del users[user_id]
    return jsonify({'message': 'User deleted successfully'}), 200

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-Memory-Liste als "Datenbank"
wishes = []  # z.B. [{"id":0, "wish":"Bike", "status":1}, ...]
next_id = 0   # Auto-Increment für die Wishes

@app.route('/wishes', methods=['POST'])
def create_wish():
    """Legt einen neuen Wunsch an."""
    global next_id
    data = request.get_json()
    wish_text = data.get('wish', '')
    status = data.get('status', 1)  # default status

    new_wish = {
        'id': next_id,
        'wish': wish_text,
        'status': status
    }
    wishes.append(new_wish)
    next_id += 1

    return jsonify({
        'message': 'Wish created',
        'wish': new_wish
    }), 201

@app.route('/wishes', methods=['GET'])
def get_wishes():
    """Gibt alle Wünsche zurück."""
    return jsonify(wishes), 200

@app.route('/wishes/<int:wish_id>', methods=['PUT'])
def update_wish_status(wish_id):
    """Aktualisiert den Status eines bestehenden Wunsches."""
    data = request.get_json()
    new_status = data.get('status', None)

    if new_status is None:
        return jsonify({'error': 'Missing status field in request'}), 400

    for wish in wishes:
        if wish['id'] == wish_id:
            wish['status'] = new_status
            return jsonify({'message': 'Wish status updated', 'wish': wish}), 200

    return jsonify({'error': f'Wish with id {wish_id} not found'}), 404

if __name__ == '__main__':
    # Starte auf Port 7887
    app.run(host='0.0.0.0', port=7887)

from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.Transposition import TranspositionCipher

app = Flask(__name__)

# Hàm bổ trợ để tự động lấy dữ liệu từ Form (Web) hoặc JSON (Postman)
def get_data(keys):
    data = {}
    if request.is_json: # Nếu gửi từ Postman (Content-Type: application/json)
        json_data = request.get_json()
        for key in keys:
            data[key] = json_data.get(key)
    else: # Nếu gửi từ Trình duyệt (HTML Form)
        for key in keys:
            data[key] = request.form.get(key)
    return data

# 1. --- CAESAR ---
caesar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = get_data(['plain_text', 'key'])
    text = data.get('plain_text')
    key = int(data.get('key')) # Ép kiểu sang số nguyên
    return jsonify({'encrypted_text': caesar_cipher.encrypt_text(text, key)})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = get_data(['cipher_text', 'key'])
    text = data.get('cipher_text')
    key = int(data.get('key'))
    return jsonify({'decrypted_text': caesar_cipher.decrypt_text(text, key)})


# 2. --- VIGENERE ---
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = get_data(['plain_text', 'key'])
    text = data.get('plain_text')
    key = data.get('key')
    return jsonify({'encrypted_text': vigenere_cipher.encrypt_text(text, key)})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = get_data(['cipher_text', 'key'])
    text = data.get('cipher_text')
    key = data.get('key')
    return jsonify({'decrypted_text': vigenere_cipher.decrypt_text(text, key)})


# 3. --- RAILFENCE ---
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = get_data(['plain_text', 'key'])
    text = data.get('plain_text')
    key = int(data.get('key'))
    return jsonify({'encrypted_text': railfence_cipher.rail_fence_encrypt(text, key)})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = get_data(['cipher_text', 'key'])
    text = data.get('cipher_text')
    key = int(data.get('key'))
    return jsonify({'decrypted_text': railfence_cipher.rail_fence_decrypt(text, key)})


# 4. --- PLAYFAIR ---
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = get_data(['plain_text', 'key'])
    text = data.get('plain_text')
    key = data.get('key')
    matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'encrypted_text': playfair_cipher.playfair_encrypt(text, matrix)})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = get_data(['cipher_text', 'key'])
    text = data.get('cipher_text')
    key = data.get('key')
    matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'decrypted_text': playfair_cipher.playfair_decrypt(text, matrix)})


# 5. --- TRANSPOSITION ---
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = get_data(['plain_text', 'key'])
    text = data.get('plain_text')
    key = int(data.get('key'))
    return jsonify({'encrypted_text': transposition_cipher.encrypt(text, key)})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = get_data(['cipher_text', 'key'])
    text = data.get('cipher_text')
    key = int(data.get('key'))
    return jsonify({'decrypted_text': transposition_cipher.decrypt(text, key)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
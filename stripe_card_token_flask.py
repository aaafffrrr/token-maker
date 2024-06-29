from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Hardcoded Stripe publishable key
STRIPE_PUBLISHABLE_KEY = 'pk_test_51KCnvuJshHAfrxBUDHSlfrQefwZSC7vWTSDndZyNIvDROQC1rPzJUCDf5AjL7ycZ6yztCs8FNV4Hh4yqMsauGRGM0006vgbSBz'

@app.route('/')
def index():
    return render_template('index.html', publishable_key=STRIPE_PUBLISHABLE_KEY)

@app.route('/receive_token', methods=['POST'])
def receive_token():
    token = request.json.get('token')
    print(f"Received token: {token}")
    # Here you can do something with the token, like save it to your database
    return jsonify({'status': 'success', 'token': token}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

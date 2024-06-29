from flask import Flask, render_template, request, redirect, url_for, flash
import stripe

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Set your Stripe secret key
stripe.api_key = 'sk_test_51KCnvuJshHAfrxBU7q7avpoI585IA95UdKOOkAIMi85GCw4lgxvAuu1Ut3tvqizlCpBZZZH7d67yPIDp8S84qOhK00A5tZgrTx'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_token', methods=['POST'])
def create_token():
    card_number = request.form['card_number']
    exp_month = request.form['exp_month']
    exp_year = request.form['exp_year']
    cvc = request.form['cvc']

    try:
        token = stripe.Token.create(
            card={
                'number': card_number,
                'exp_month': exp_month,
                'exp_year': exp_year,
                'cvc': cvc,
            },
        )
        flash(f"Card Token: {token.id}", 'success')
    except stripe.error.StripeError as e:
        flash(f"Stripe error: {e.user_message}", 'danger')
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'danger')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

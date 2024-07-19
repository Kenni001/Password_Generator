# api/index.py
from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length: int = 10, use_upper=True, use_lower=True, use_digits=True, use_punctuation=True):
    alphabet = ""
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_lower:
        alphabet += string.ascii_lowercase
    if use_digits:
        alphabet += string.digits
    if use_punctuation:
        alphabet += string.punctuation

    if not alphabet:
        return "Please select at least one character type."

    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 10))
        use_upper = 'upper' in request.form
        use_lower = 'lower' in request.form
        use_digits = 'digits' in request.form
        use_punctuation = 'punctuation' in request.form
        password = generate_password(length, use_upper, use_lower, use_digits, use_punctuation)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)

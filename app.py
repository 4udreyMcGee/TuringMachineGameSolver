from flask import Flask, render_template, request

from main import solve

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        # Retrieve values from the form
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        num3 = float(request.form['num3'])
        num4 = float(request.form['num4'])

        res = solve(num1, num2, num3, num4)
        result = f'possibles codes: {list(res.keys())}'
        return render_template('result.html', solutions=list(res.keys()))
    except ValueError:
        return 'Invalid input. Please enter valid numbers.'

if __name__ == '__main__':
    app.run(debug=True)

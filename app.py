from flask import Flask, render_template, request

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

        # Display the entered numbers
        result = f'You entered: {num1}, {num2}, {num3}, {num4}'
        return result
    except ValueError:
        return 'Invalid input. Please enter valid numbers.'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template
import re

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Function to safely evaluate expressions
def evaluate_expression(expression):
    try:
        cleaned_expression = re.sub(r'[^0-9+\-*/().]', '', expression)
        result = eval(cleaned_expression)
        return result
    except Exception as e:
        return f"Error: {e}"

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        expression = request.form['expression']
        result = evaluate_expression(expression)
    
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

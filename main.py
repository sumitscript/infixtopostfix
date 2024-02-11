from flask import Flask, render_template, request 
import re
app = Flask(__name__, static_folder="static")
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        expr = request.form['infix']
        if expr.lower() == "hi":
            result = "Hello" 
        else:           
            try:
                postfix = to_postfix(expr)
                result = postfix 
            except Exception as e:
                result = str(e)

    return render_template('index.html', result=result)

operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def to_postfix(postfix):
    stack = []
    
    for t in postfix:
        if t in operators:
            op2 = stack.pop() 
            op1 = stack.pop()
            expr = "(" + op1 + t + op2 + ")"
            stack.append(expr) 
        else:
            stack.append(t)
            
    return stack.pop()
        
if __name__ == '__main__':
    app.run(debug=True)
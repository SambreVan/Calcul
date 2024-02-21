from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérer les nombres et l'opération du formulaire
        number1 = request.form.get('number1', type=float)
        number2 = request.form.get('number2', type=float)
        operation = request.form.get('operation')
        
        # Effectuer le calcul
        result = None
        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            result = number1 / number2

        return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)

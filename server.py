from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def tablero_1():
    return render_template('index.html', num1=8, num2=8, color1='lightblue', color2='black')

@app.route('/<int:numero>')
def tablero_2(numero):
    return render_template('index.html', num1=8, num2=numero, color1='lightblue', color2='black')

@app.route('/<int:numero1>/<int:numero2>')
def tablero_3(numero1, numero2):
    return render_template('index.html', num1=numero1, num2=numero2, color1='lightblue', color2='black')

@app.route('/<int:numero1>/<int:numero2>/<string:color1>')
def tablero_4(numero1, numero2, color1):
    return render_template('index.html', num1=numero1, num2=numero2, color1=color1, color2='black')

@app.route('/<int:numero1>/<int:numero2>/<string:color1>/<string:color2>')
def tablero_5(numero1, numero2, color1, color2):
    return render_template('index.html', num1=numero1, num2=numero2, color1=color1, color2=color2)





if __name__=='__main__':
    app.run(debug=True)
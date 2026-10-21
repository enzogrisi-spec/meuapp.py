from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def exibir_pagina():
    return render_template('index.html')


@app.route('/contato')
def exibir_contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
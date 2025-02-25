from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


# Executa o app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return 'Hello!'

@app.route('/about')
def about():
    return 'About this page'

if __name__ == "__main__":
    app.run(debug=True) # Видимость ошибок

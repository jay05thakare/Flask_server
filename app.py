from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # return '<h1>Hello {} !</h1>' .format(name)

@app.route('/products')
def products():
    return '<h1>this is product page</h1>'

# @app.route('/about')

if __name__ == '__main__':
    app.run(debug=True)
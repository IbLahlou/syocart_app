
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Route 1 : Home page

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

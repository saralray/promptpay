import os
from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


@app.route('/')
def index():
    phone = os.getenv('PHONE')
    return render_template('index.html', phone=phone)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

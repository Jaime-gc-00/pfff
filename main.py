from Flask import current_app, Flask, render_template
import json
import os

app = Flask(__name__, static_url_path='/static')

APP_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(APP_DIR, 'templates')
STATIC_DIR = os.path.join(APP_DIR,'static')
current_app.template_folder = TEMPLATE_DIR
current_app.static_folder = STATIC_DIR

@app.route('/main')
def main():
    return render_template('index.html')

from Flask import current_app, Flask, render_template
import json
import os

ROOT_PREFIX = "/app"
app = Flask(__name__, static_url_path=ROOT_PREFIX + '/static')

APP_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(APP_DIR, 'templates')
STATIC_DIR = os.path.join(APP_DIR,'static')
current_app.template_folder = TEMPLATE_DIR
current_app.static_folder = STATIC_DIR

@app.route('/'+ROOT_PREFIX)
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

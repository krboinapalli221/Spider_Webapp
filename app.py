from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    user_name = request.form['name']
    greeting_message = f'Hello, {user_name}! Welcome to the Spider Web App!'
    return render_template('greet.html', greeting=greeting_message)

# Route to serve static files (images, etc.)
@app.route('/static/<path:filename>')
def static_files(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

if __name__ == '__main__':
    app.run(debug=True, port=4000)

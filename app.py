from flask import Flask, render_template, jsonify
import threading
from Brain.main import start_vapi

app = Flask(__name__)

# Define the UI function
def UI():
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/status')
    def status():
        return jsonify({"status": "UI is running"})

    # Start the Flask app
    app.run(port=5000)

# Function to launch both UI and VAPI using threading
def launch_vapi():
    t1 = threading.Thread(target=UI)
    t2 = threading.Thread(target=start_vapi)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    launch_vapi()

from flask import Flask
import subprocess
import os
import getpass
import platform
import html
from datetime import datetime
import pytz

app = Flask(_name_)

@app.route('/')
def sample():
    return "Hello World" # to test if the flask endpoint is working

@app.route('/htop')
def htop():
    
    name = "Deepanshu Ganguli"

    # Get system username 
    username = getpass.getuser()

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get system process info based on OS
    try:
        if platform.system() == "Windows":
            top_output = subprocess.check_output(['tasklist']).decode('utf-8')
        else:
            top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error fetching process info: {str(e)}"

    # Sanitize output
    safe_top_output = html.escape(top_output)

    # HTML response
    return f"""
    <html>
        <body>
            <h1>System Info</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time:</strong> {server_time}</p>
            <pre>{safe_top_output}</pre>
        </body>
    </html>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5050)

from flask import Flask
import os
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def info():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pod_name = socket.gethostname()
    pod_ip = socket.gethostbyname(pod_name)
    
    return f"""
    <h1>System Monitor</h1>
    <p><b>Server Time:</b> {now}</p>
    <p><b>Pod Name:</b> {pod_name}</p>
    <p><b>Pod IP:</b> {pod_ip}</p>
    <hr>
    <p>Running on Kubernetes!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
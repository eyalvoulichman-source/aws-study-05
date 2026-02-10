from flask import Flask
import os
import socket
import datetime

app = Flask(__name__)

# הנתיב שחיברנו ב-YAML ל-emptyDir
DATA_FILE = "/tmp/app-data/last_visit.txt"

@app.route("/")
def info():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pod_name = socket.gethostname()
    pod_ip = socket.gethostbyname(pod_name)
    
    # 1. קריאה מהדיסק הזמני (אם הקובץ קיים)
    last_visit = "זו הפעם הראשונה שהפוד הזה רואה אותך (או שהדיסק התנקה)"
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            last_visit = f.read()

    # 2. כתיבת הזמן הנוכחי לדיסק עבור הביקור הבא
    # אנחנו יוצרים את התיקייה ליתר ביטחון אם היא לא קיימת
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        f.write(now)
    
    return f"""
    <h1>System Monitor</h1>
    <p><b>Server Time:</b> {now}</p>
    <p><b>Pod Name:</b> {pod_name}</p>
    <p><b>Pod IP:</b> {pod_ip}</p>
    <hr>
    <p><b>Last visit recorded on ephemeral disk:</b> {last_visit}</p>
    <hr>
    <p>Running on Kubernetes with <b>emptyDir</b> storage!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
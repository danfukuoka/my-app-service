import os
from flask import Flask

app = Flask(__name__)

print("test4")

@app.route("/")
def home():
    print("test1")
    identity_endpoint = os.environ.get("IDENTITY_ENDPOINT")
    identity_header = os.environ.get("IDENTITY_HEADER")

    return f"""
    IDENTITY_ENDPOINT: {identity_endpoint}
    <br><br>
    IDENTITY_HEADER: {identity_header}
    """

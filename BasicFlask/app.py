from flask import Flask, escape, request
import socket

app = Flask(__name__)

@app.route('/')
def get_hostname():
    return 'You’ve hit {} \n'.format(escape(socket.gethostname()))
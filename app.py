# app.py
from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO
import random

app = Flask(name)
app.secret_key = 'ваш_секретный_ключ'
socketio = SocketIO(app)

# Здесь будет основной код из примера (создание комнат, лобби и т.д.)
# ...

if name == 'main':
    socketio.run(app, debug=True)

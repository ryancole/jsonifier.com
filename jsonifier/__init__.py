from flask import Flask, redirect, url_for


# application

app = Flask(__name__)
app.secret_key = 'foo'


# modules

from jsonifier.views.api import api
from jsonifier.views.fluff import fluff
from jsonifier.views.paste import paste

app.register_module(fluff)
app.register_module(api, url_prefix='/api')
app.register_module(paste, url_prefix='/paste')


# 404 redirect

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('paste.create'))
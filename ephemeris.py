#!/usr/bin/env python
import logging

from flask import Flask, render_template, request, send_from_directory
app = Flask('ephemeris', static_folder='static', static_url_path='')

@app.route('/')
def welcome():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    logging.debug('LOGGING IN!')
    return 'hey you logged in!: ' + str(request.form)

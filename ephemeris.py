#!/usr/bin/env python
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

from flask import (Flask, render_template, session, request, redirect, url_for)
app = Flask('ephemeris', static_folder='static', static_url_path='')

app.secret_key = 'is this secret key good enough?'


@app.route('/')
def welcome():
    if 'user_id' in session:
        logger.debug('user {} is already logged in'.format(session['user_id']))
        return redirect(url_for('user_page'))

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'ddavella' and password == 'password':
        logger.debug('logging in as', username)
        session['user_id'] = username
        return redirect(url_for('user_page'))
    else:
        logger.debug('failed to log in')
        return redirect(url_for('welcome'))

@app.route('/logout')
def logout():
    if 'user_id' in session:
        logger.debug('logging out {}'.format(session['user_id']))
        session.pop('user_id')
    return redirect(url_for('welcome'))

@app.route('/user_page')
def user_page():
    if 'user_id' not in session:
        return redirect(url_for('welcome'))

    return 'welcome {}!'.format(session['user_id'])

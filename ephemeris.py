#!/usr/bin/env python
from flask import (Flask, render_template, session, request, redirect, url_for)

app = Flask('ephemeris', static_folder='static', static_url_path='')
app.secret_key = 'is this secret key good enough?'


@app.route('/')
def welcome():
    if 'user_id' in session:
        app.logger.info('user {} is already logged in'.format(session['user_id']))
        return redirect(url_for('user_page'))

    action = '/login?admin=true' if request.args.get('admin') else '/login'
    return render_template('login.html', context={'action': action})

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if request.args.get('admin'):
        app.logger.info('admin login attempt')

    if username == 'ddavella' and password == 'password':
        app.logger.info('logging in as {}'.format(username))
        session['user_id'] = username
        return redirect(url_for('user_page'))
    else:
        app.logger.info('failed to log in')
        return redirect(url_for('welcome'))

@app.route('/admin')
def admin_login():
    return redirect(url_for('welcome', admin='true'))

@app.route('/logout')
def logout():
    if 'user_id' in session:
        app.logger.info('logging out {}'.format(session['user_id']))
        session.pop('user_id')
    return redirect(url_for('welcome'))

@app.route('/user_page')
def user_page():
    if 'user_id' not in session:
        return redirect(url_for('welcome'))

    return 'welcome {}!'.format(session['user_id'])

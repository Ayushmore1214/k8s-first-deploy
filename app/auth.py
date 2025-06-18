from flask import Blueprint, redirect, session, url_for
from flask_oauthlib.client import OAuth
import os

oauth = OAuth()
github = oauth.remote_app(
    'github',
    consumer_key=os.environ.get("GH_CLIENT_ID"),
    consumer_secret=os.environ.get("GH_CLIENT_SECRET"),
    request_token_params={'scope': 'repo'},
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)

github_blueprint = Blueprint('github', __name__)

@github_blueprint.route('/login')
def login():
    return github.authorize(callback=url_for('github.authorized', _external=True))

@github_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@github_blueprint.route('/login/authorized')
def authorized():
    resp = github.authorized_response()
    if resp is None or resp.get('access_token') is None:
        return 'Access denied'
    session['github_token'] = (resp['access_token'], '')
    user = github.get('user')
    session['github_user'] = user.data['login']
    return redirect('/dashboard')

@github.tokengetter
def get_github_token():
    return session.get('github_token')

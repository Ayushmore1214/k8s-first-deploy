from flask import Blueprint, render_template, session, redirect, request
from .auth import github
from .backup import backup_repo
from .models import db, BackupHistory

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/dashboard')
def dashboard():
    if 'github_token' not in session:
        return redirect('/login')
    user = github.get('user').data
    repos = github.get('user/repos').data
    return render_template('dashboard.html', user=user, repos=repos)

@main.route('/backup', methods=['POST'])
def backup():
    repo = request.form['repo']
    user = session['github_user']
    token = session['github_token'][0]
    gcs_url = backup_repo(user, repo, token)
    if gcs_url:
        db.session.add(BackupHistory(username=user, repo_name=repo, gcs_path=gcs_url))
        db.session.commit()
    return redirect('/dashboard')

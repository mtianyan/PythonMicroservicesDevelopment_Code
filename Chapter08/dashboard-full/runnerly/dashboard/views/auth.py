from stravalib.client import Client
from flask import Blueprint, abort, session, request, current_app, redirect


auth = Blueprint('auth', __name__)


def send_user_to_dataservice(email, access_token):
    pass


@auth.route('/strava_redirect')
def strava_login():
    code = request.args.get('code')
    client = Client()
    cid = current_app.config['STRAVA_CLIENT_ID']
    csecret = current_app.config['STRAVA_CLIENT_SECRET']
    access_token = client.exchange_code_for_token(client_id=cid,
            client_secret=csecret, code=code)
    athlete = client.get_athlete()
    email = athlete.email
    send_user_to_dataservice(email, access_token)
    session['user'] = email
    session['token'] = access_token
    return redirect('/')


@auth.route('/logout')
def logout():
    if 'user' in session:
        del session['user']
        del session['token']
    return redirect('/')



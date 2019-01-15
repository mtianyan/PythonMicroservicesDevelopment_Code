from flask import Blueprint, session, render_template
from flask import current_app as app
from stravalib.client import Client


home = Blueprint('home', __name__)


def get_strava_url():
    client = Client()
    cid = app.config['STRAVA_CLIENT_ID']
    redirect = app.config['STRAVA_REDIRECT']
    url = client.authorization_url(client_id=cid,
                                   redirect_uri=redirect)
    return url



@home.route('/')
def index():
    strava_url = get_strava_url()
    user = session.get('user')
    return render_template('index.html', strava_url=strava_url, user=user)



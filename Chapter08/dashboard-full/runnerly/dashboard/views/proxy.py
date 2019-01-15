import requests

from flakon import JsonBlueprint
from flask import Blueprint, abort, session, jsonify
from flask import current_app as app


proxy = JsonBlueprint('proxy', __name__)


def email_to_uid(email):
    return 1


def get_token():
    data = [('client_id', app.config['TOKENDEALER_CLIENT_ID']),
            ('client_secret', app.config['TOKENDEALER_CLIENT_SECRET']),
            ('audience', 'runnerly.io'),
            ('grant_type', 'client_credentials')]

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url = app.config['TOKENDEALER'] + '/oauth/token'
    resp = requests.post(url, data=data, headers=headers)
    return resp.json()['access_token']


_TOKEN = 'NOT_SET'


def get_auth_header(new=False):
    global _TOKEN
    if _TOKEN is None or new:
        _TOKEN = get_token()
    return 'Bearer ' + _TOKEN


def call_data_service(endpoint):
    token = get_auth_header()
    resp = requests.get(app.config['DATASERVICE'] + endpoint,
                        headers={'Authorization': token})
    if resp.status_code == 401:
        # the token might be revoked
        token = get_auth_header(new=True)
        resp = requests.get(app.config['DATASERVICE'] + endpoint,
                            headers={'Authorization': token})

    return resp


@proxy.route('/api/runs/<int:year>/<int:month>')
def runs(year, month):
    if 'user' not in session:
        abort(401)
    uid = email_to_uid(session['user'])
    endpoint = '/runs/%d/%d/%d' % (uid, year, month)
    resp = call_data_service(endpoint)
    return jsonify(resp.json())

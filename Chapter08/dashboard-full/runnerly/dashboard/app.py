import os
from flask import (Flask, render_template, jsonify, request,
                   redirect, session, abort)
from stravalib.client import Client
import requests
from flakon import create_app as _create
from .views import blueprints



def create_app(settings=None):
    app = _create(blueprints=blueprints, settings=settings)
    return app

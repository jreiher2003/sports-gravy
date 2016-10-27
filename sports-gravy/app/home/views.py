import os
import requests
import json
from dateutil.parser import parse as parse_date
from app import app, db, cache, bcrypt, uploaded_photos
from flask_uploads import UploadNotAllowed
from flask import request, flash, redirect, url_for
from sqlalchemy import exc
from flask_security import login_required, roles_required, roles_accepted, current_user
from flask import Blueprint, render_template
# from .utils import api_request


home_blueprint = Blueprint("home", __name__, template_folder="templates")

def api_request(params):
    try:
        headers = {'Ocp-Apim-Subscription-Key': os.environ["OCP_APIM_SUBSCRIPTION_KEY"],}
        url = "https://api.fantasydata.net"
        conn = requests.get("https://api.fantasydata.net/" + params, headers=headers)
        print conn.status_code
        return conn.json()
    except Exception as e:
        print e
 
@home_blueprint.route("/", methods=["GET","POST"])
# @cache.cached(timeout=60*5, key_prefix="nfl_all_teams")
def home():
    all_teams = api_request("v3/nfl/scores/JSON/Teams/2016REG")
    team = api_request("v3/nfl/scores/JSON/Teams/2016REG")
    return render_template(
        "home.html",
        all_teams = all_teams,
        team = team,
        )


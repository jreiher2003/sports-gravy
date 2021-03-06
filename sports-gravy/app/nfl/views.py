import os
import json
import datetime
import requests
from datetime import date
import hashlib
from dateutil.parser import parse as parse_date
from app import app, db, cache
from sqlalchemy import exc
# from app.users.models import Users, Role, UserRoles, Profile
from flask import Blueprint, render_template, url_for, request, redirect,flash, abort
from flask_security import login_required, roles_required, current_user, roles_accepted
from slugify import slugify
from .utils import team_rush_avg, team_pass_avg, \
opp_team_rush_avg, opp_team_pass_avg, team_off_avg, \
team_def_avg, today_date,today_and_now, make_salt, yesterday

nfl_blueprint = Blueprint("nfl", __name__, template_folder="templates")

def api_request(params):
    try:
        headers = {'Ocp-Apim-Subscription-Key': os.environ["OCP_APIM_SUBSCRIPTION_KEY"],}
        url = "https://api.fantasydata.net"
        conn = requests.get("https://api.fantasydata.net/" + params, headers=headers)
        return conn.json()
    except Exception as e:
        print e

all_nfl_teams = api_request("v3/nfl/scores/JSON/Teams/2016REG")

@nfl_blueprint.route("/nfl/home/")
@nfl_blueprint.route("/nfl/")
def nfl_home():
    return render_template(
        "nfl_home.html", 
        all_teams = all_nfl_teams,
        )

@nfl_blueprint.route("/nfl/standings/")
@cache.cached(timeout=60*5, key_prefix="nfl_season_standings")
def nfl_standings():
    st = api_request("/v3/nfl/scores/JSON/Standings/2016REG")
    return render_template(
        "nfl_standings/nfl standings.html", 
        all_teams = all_nfl_teams,
        standing = st, 
        )

@nfl_blueprint.route("/nfl/schedule/")
def nfl_schedule():
    dt = datetime.datetime.now()
    sch = api_request("/v3/nfl/scores/JSON/Schedules/2016REG")
    for i in sch:
        print i
    return render_template(
        "nfl_schedule.html", 
        all_teams = all_nfl_teams, 
        data = sch, 
        dt = dt,
        )

@nfl_blueprint.route("/nfl/stats/<int:sid>/")
def nfl_stats(sid): 
    teamseason1 = api_request("/v3/nfl/stats/JSON/TeamSeasonStats/2016REG")
    return render_template(
        "nfl_stats.html", 
        all_teams = all_nfl_teams, 
        teamseason = teamseason1,
        )

@nfl_blueprint.route("/nfl/team/home/<int:sid>/<path:key>/<path:team>/")
def nfl_team_home(sid,key,team):
    dt = today_and_now()
    dt_plus_2h = dt - datetime.timedelta(hours=4)
    jj = NFLTeam.query.filter_by(Key=key).one()
    tt = NFLStadium.query.filter_by(StadiumID=jj.StadiumID).one() 
    ss = NFLStandings.query.filter_by(Team=key).one()
    tss = NFLTeamSeason.query.filter_by(Team=key, SeasonType=sid).one()
    ts = NFLSchedule.query.filter_by(SeasonType=sid).filter((NFLSchedule.AwayTeam==key) | (NFLSchedule.HomeTeam==key))
    team_score = NFLScore.query.filter_by(SeasonType=sid).filter((NFLScore.AwayTeam==key) | (NFLScore.HomeTeam==key))
    team_rush_rank = team_rush_avg(tss.RushingYards,tss.Team, sid) 
    team_pass_rank = team_pass_avg(tss.PassingYards,tss.Team, sid) 
    opp_team_rush_rank = opp_team_rush_avg(tss.OpponentRushingYards,tss.Team, sid) 
    opp_team_pass_rank = opp_team_pass_avg(tss.OpponentPassingYards,tss.Team, sid) 
    team_off_rank = team_off_avg(tss.OffensiveYards,tss.Team, sid)
    team_def_rank = team_def_avg(tss.OpponentOffensiveYards,tss.Team, sid) 
    return render_template(
        "nfl_team/nfl_team_home.html",
        all_teams = all_nfl_teams,
        team_rush_rank = team_rush_rank,
        team_pass_rank = team_pass_rank,
        opp_team_rush_rank = opp_team_rush_rank,
        opp_team_pass_rank = opp_team_pass_rank,
        team_off_rank = team_off_rank,
        team_def_rank = team_def_rank,
        team_score = team_score,
        dt_plus_2h = dt_plus_2h,
        dt = dt,
        tt = tt,
        jj = jj,
        ss = ss,
        tss = tss,
        ts = ts
        )


@nfl_blueprint.route("/nfl/team/schedule/<path:team>/")
def nfl_team_schedule(team):
    all_teams = all_nfl_teams
    return "schedule"

@nfl_blueprint.route("/nfl/team/stats/<path:team>/")
def nfl_team_stats(team):
    all_teams = all_nfl_teams
    return "stats"









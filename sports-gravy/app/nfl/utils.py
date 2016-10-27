import json
import datetime
import random
from string import hexdigits
from app import db


def make_salt(length=10):
    return "".join(random.choice(hexdigits) for x in xrange(length))

def today_date():
    t = datetime.time()
    d = datetime.date.today()
    return datetime.datetime.combine(d,t)

def today_and_now():
    return datetime.datetime.now()

def yesterday():
    return datetime.datetime.now() - datetime.timedelta(days=1)

## OFFENSIVE STATS by TEAM
def team_rush_avg(rush_yds, team, sid):
    q = db.session.query(NFLTeamSeason.RushingYards,NFLTeamSeason.Team).filter_by(SeasonType=sid).order_by(db.desc(NFLTeamSeason.RushingYards)).all()
    team_ = []
    for y,t in q:
        team_.append((y,t)) 
    return team_.index((rush_yds, team)) + 1
    

def team_pass_avg(pass_yds, team, sid):
    q = db.session.query(NFLTeamSeason.PassingYards,NFLTeamSeason.Team).filter_by(SeasonType=sid).order_by(db.desc(NFLTeamSeason.PassingYards)).all()
    team_ = []
    for y,t in q:
        team_.append((y,t))
    return team_.index((pass_yds, team)) + 1
    

def opp_team_rush_avg(rush_yds, team, sid):
    q = db.session.query(NFLTeamSeason.OpponentRushingYards,NFLTeamSeason.Team).filter_by(SeasonType=sid).order_by(db.desc(NFLTeamSeason.OpponentRushingYards)).all()
    team_ = []
    for y,t in q:
        team_.append((y,t))
    return team_.index((rush_yds, team)) + 1

def opp_team_pass_avg(pass_yds, team, sid):
    q = db.session.query(NFLTeamSeason.OpponentPassingYards,NFLTeamSeason.Team).filter_by(SeasonType=sid).order_by(db.desc(NFLTeamSeason.OpponentPassingYards)).all()
    team_ = []
    for y,t in q:
        team_.append((y,t))
    return team_.index((pass_yds, team)) + 1

def team_off_avg(pass_yds, team, sid):
    q = db.session.query(NFLTeamSeason.OffensiveYards,NFLTeamSeason.Team).filter_by(SeasonType=sid).order_by(db.desc(NFLTeamSeason.OffensiveYards)).all()
    team_ = []
    for y,t in q:
        team_.append((y,t))
    return team_.index((pass_yds, team)) + 1

def team_def_avg(pass_yds, team, sid):
    q = db.session.query(NFLTeamSeason.OpponentOffensiveYards,NFLTeamSeason.Team).filter_by(SeasonType=sid).order_by(db.desc(NFLTeamSeason.OpponentOffensiveYards)).all()
    team_ = []
    for y,t in q:
        team_.append((y,t))
    return team_.index((pass_yds, team)) + 1


    
             
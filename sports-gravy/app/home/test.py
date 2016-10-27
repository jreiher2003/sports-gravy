########### Python 2.7 #############
import os
import httplib, urllib, base64
from pprint import pprint 

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': os.environ["OCP_APIM_SUBSCRIPTION_KEY"],
}

params = urllib.urlencode({
})
##################################################################
## games in progress boolean true/false 
def games_in_progress():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/AreAnyGamesInProgress?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        pprint(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

##################################################################
# bye weeks 
# {"Season":2016,"Week":13,"Team":"TEN"}
def bye_weeks():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/Byes/2016REG?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        pprint(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

##################################################################
# news by player 
# {"NewsID":43530,"Title":"Robert Griffin III likely out for the season","Updated":"2016-09-18T08:33:00","Url":"http:\/\/www.rotoworld.com\/player\/nfl\/7406\/robert-griffin-iii","Content":"ESPN's Adam Schefter reports Robert Griffin III's (shoulder, injured reserve) season &quot;could well be over.&quot;","Source":"NBCSports.com","TermsOfUse":"NBCSports.com feeds in the RSS format are provided free of charge for use by individuals for personal, non-commercial uses. More details here: http:\/\/fantasydata.com\/resources\/rotoworld-rss-feed.aspx","Team":"CLE","PlayerID":14257}
def news_by_player():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/NewsByPlayerID/14257?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# news by team 
# {"NewsID":45063,"Title":"Chris Thompson: 19 touches for 113 yards","Updated":"2016-10-23T16:58:00","Url":"http:\/\/www.rotoworld.com\/player\/nfl\/8563\/chris-thompson","Content":"Chris Thompson rushed 12 times for 73 yards in the Redskins' Week 7 loss to the Lions, adding seven receptions for 40 additional yards.","Source":"NBCSports.com","TermsOfUse":"NBCSports.com feeds in the RSS format are provided free of charge for use by individuals for personal, non-commercial uses. More details here: http:\/\/fantasydata.com\/resources\/rotoworld-rss-feed.aspx","Team":"WAS","PlayerID":15102}
def news_by_team():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/NewsByTeam/WAS?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print "\n\n\n\n"
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# {"NewsID":45199,"Title":"Aldon Smith has applied for reinstatement","Updated":"2016-10-27T11:00:00","Url":"http:\/\/www.rotoworld.com\/player\/nfl\/6477\/aldon-smith","Content":"Suspended Raiders OLB Aldon Smith has applied for reinstatement.","Source":"NBCSports.com","TermsOfUse":"NBCSports.com feeds in the RSS format are provided free of charge for use by individuals for personal, non-commercial uses. More details here: http:\/\/fantasydata.com\/resources\/rotoworld-rss-feed.aspx","Team":"OAK","PlayerID":13453},
# news by league
def news_by_league():
    print "news by league"
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/News?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# schedule 
def schedule():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/Schedules/2016REG?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        pprint(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# scores by season
def scores_by_season():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/Scores/2016REG?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        pprint(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# scores by week
def scores_by_week():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/ScoresByWeek/2016REG/7?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# current season # just gives the year 
def current_season():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/CurrentSeason?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# season last completed gives only a year also
def last_season():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/LastCompletedSeason?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# year only 
def next_year():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/UpcomingSeason?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# stadiums 
def stadiums():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/Stadiums?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        pprint(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

# ####################################
# standings 
def standings():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/Standings/2016REG?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# Teams Active 
# {"Key":"WAS","TeamID":35,"PlayerID":97,"City":"Washington","Name":"Redskins","Conference":"NFC","Division":"East","FullName":"Washington Redskins","StadiumID":19,"ByeWeek":9,"AverageDraftPosition":null,"AverageDraftPositionPPR":787.00,"HeadCoach":"Jay Gruden","OffensiveCoordinator":"Sean McVay","DefensiveCoordinator":"Joe Barry","SpecialTeamsCoach":"Ben Kotwica","OffensiveScheme":"3WR","DefensiveScheme":"3-4","UpcomingSalary":2400,"UpcomingOpponent":"CIN","UpcomingOpponentRank":9,"UpcomingOpponentPositionRank":9,"UpcomingFanDuelSalary":4300,"UpcomingDraftKingsSalary":2400,"UpcomingYahooSalary":15,"StadiumDetails":{"StadiumID":19,"Name":"FedEx Field","City":"Landover","State":"MD","Country":"USA","Capacity":85000,"PlayingSurface":"Grass","GeoLat":38.907652,"GeoLong":-76.864479}
def teams_active():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/Teams?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        return data
        print "\n\n\n\n"
        
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# teams by season 
# "Key":"WAS","TeamID":35,"PlayerID":97,"City":"Washington","Name":"Redskins","Conference":"NFC","Division":"East","FullName":"Washington Redskins","StadiumID":19,"ByeWeek":9,"AverageDraftPosition":null,"AverageDraftPositionPPR":787.00,"HeadCoach":"Jay Gruden","OffensiveCoordinator":"Sean McVay","DefensiveCoordinator":"Joe Barry","SpecialTeamsCoach":"Ben Kotwica","OffensiveScheme":"3WR","DefensiveScheme":"3-4","UpcomingSalary":2400,"UpcomingOpponent":"CIN","UpcomingOpponentRank":9,"UpcomingOpponentPositionRank":9,"UpcomingFanDuelSalary":4300,"UpcomingDraftKingsSalary":2400,"UpcomingYahooSalary":15,"StadiumDetails":{"StadiumID":19,"Name":"FedEx Field","City":"Landover","State":"MD","Country":"USA","Capacity":85000,"PlayingSurface":"Grass","GeoLat":38.907652,"GeoLong":-76.864479
def teams_by_season():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/Teams/2016REG?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print data
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
# timeframes season/year/week/date/time/firstgamestarted/
def timeframes():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/{format}/Timeframes/{type}?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        print "\n\n\n\n"
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
#current week # last week # week upcoming  
def current_week():
    try:
        conn = httplib.HTTPSConnection('api.fantasydata.net')
        conn.request("GET", "/v3/nfl/scores/JSON/CurrentWeek?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

if __name__ == "__main__":
    # teams_active()
    # current_week()
    # teams_by_season()
    scores_by_season()
    # conn.close()
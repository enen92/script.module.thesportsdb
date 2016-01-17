import datetime

class Livescore:
    def __init__(self):
        self.Date = ""
        self.League = ""
        self.Round = ""
        self.Spectators = ""
        self.HomeTeam = ""
        self.HomeTeam_Id = ""
        self.AwayTeam = ""
        self.AwayTeam_Id = ""
        self.Time = ""
        self.HomeGoals = ""
        self.AwayGoals = ""
        self.HomeGoalDetails = ""
        self.AwayGoalDetails = ""
        self.HomeLineupGoalkeeper = ""
        self.AwayLineupGoalkeeper = ""
        self.HomeLineupDefense = ""
        self.AwayLineupDefense = ""
        self.HomeLineupMidfield = ""
        self.AwayLineupMidfield = ""
        self.HomeLineupForward = ""
        self.AwayLineupForward = ""
        self.HomeLineupSubstitutes = ""
        self.AwayLineupSubstitutes = ""
        self.HomeLineupCoach = ""
        self.AwayLineupCoach = ""
        self.HomeSubDetails = ""
        self.AwaySubDetails =  ""
        self.HomeTeamFormation = ""
        self.AwayTeamFormation = ""
        self.Location = ""
        self.Stadium = ""
        self.HomeTeamYellowCardDetails = ""
        self.AwayTeamYellowCardDetails = ""
        self.HomeTeamRedCardDetails = ""
        self.AwayTeamRedCardDetails = ""

    def setHomeTeamObj(self,img):
        self.HomeTeamObj = img

    def setAwayTeamObj(self,img):
        self.AwayTeamObj = img

    def getDatetime(self):
        hour = self.Date.split("T")[1].split("+")[0]
        print hour

def as_event(d):
    e = Livescore()
    e.__dict__.update(d)
    return e
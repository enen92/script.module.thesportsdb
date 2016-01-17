class Team:
    def __init__(self):
        self.idTeam = ""
        self.idSoccerXML = ""
        self.intLoved = ""
        self.strTeam = ""
        self.strTeamShort = ""
        self.strAlternate = ""
        self.intFormedYear = ""
        self.strSport = ""
        self.strLeague = ""
        self.idLeague = ""
        self.strDivision = ""
        self.strManager = ""
        self.strStadium = ""
        self.strKeywords = ""
        self.strRSS = ""
        self.strStadiumThumb = ""
        self.strStadiumDescription = ""
        self.strStadiumLocation = ""
        self.strWebsite = ""
        self.strFacebook = ""
        self.strTwitter = ""
        self.strInstagram = ""
        self.strDescriptionEN = ""
        self.strDescriptionDE = ""
        self.strDescriptionFR = ""
        self.strDescriptionCN = ""
        self.strDescriptionIT = ""
        self.strDescriptionJP = ""
        self.strDescriptionRU = ""
        self.strDescriptionES = ""
        self.strDescriptionPT = ""
        self.strDescriptionSE = ""
        self.strDescriptionNL = ""
        self.strDescriptionHU = ""
        self.strDescriptionNO = ""
        self.strDescriptionIL = ""
        self.strDescriptionPL = ""
        self.strGender = ""
        self.strCountry = ""
        self.strTeamBadge = ""
        self.strTeamJersey = ""
        self.strTeamLogo = ""
        self.strTeamFanart1 = ""
        self.strTeamFanart2 = ""
        self.strTeamFanart3 = ""
        self.strTeamFanart4 = ""
        self.strTeamBanner = ""
        self.strYoutube = ""
        self.strLocked = ""

    @property
    def FanartList(self):
        fanartlist = []
        if self.strTeamFanart1: fanartlist.append(self.strTeamFanart1)
        if self.strTeamFanart2: fanartlist.append(self.strTeamFanart2)
        if self.strTeamFanart3: fanartlist.append(self.strTeamFanart3)
        if self.strTeamFanart4: fanartlist.append(self.strTeamFanart4)
        return fanartlist

    def strDescription(self,language):
        if self.strDescriptionPT: return self.strDescriptionPT
        else: return self.strDescriptionEN


def as_team(d):
    t = Team()
    t.__dict__.update(d)
    return t
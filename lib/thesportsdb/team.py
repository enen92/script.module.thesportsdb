# -*- coding: utf-8 -*-
'''
    script.module.thesportsdb - A python module to wrap the main thesportsdb
    API methods
    Copyright (C) 2016 enen92,Zag

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

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
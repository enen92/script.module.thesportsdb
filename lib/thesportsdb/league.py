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

class League:
    def __init__(self):
        self.idLeague = ""
        self.idSoccerXML = ""
        self.strSport = ""
        self.strLeague = ""
        self.strLeagueAlternate = ""
        self.intFormedYear = ""
        self.dateFirstEvent = ""
        self.strGender = ""
        self.strCountry = ""
        self.strWebsite = ""
        self.strFacebook = ""
        self.strTwitter = ""
        self.strYoutube = ""
        self.strRSS = ""
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
        self.strFanart1 = ""
        self.strFanart2 = ""
        self.strFanart3 = ""
        self.strFanart4 = ""
        self.strBanner = ""
        self.strBadge = ""
        self.strLogo = ""
        self.strPoster = ""
        self.strTrophy = ""
        self.strNaming = ""
        self.strLocked = ""


    @property
    def FanartList(self):
        fanartlist = []
        if self.strFanart1: fanartlist.append(self.strFanart1)
        if self.strFanart2: fanartlist.append(self.strFanart2)
        if self.strFanart3: fanartlist.append(self.strFanart3)
        if self.strFanart4: fanartlist.append(self.strFanart4)
        return fanartlist

    def strDescription(self,language):
        if self.strDescriptionPT: return self.strDescriptionPT
        else: return self.strDescriptionEN


def as_league(d):
    l = League()
    l.__dict__.update(d)
    return l
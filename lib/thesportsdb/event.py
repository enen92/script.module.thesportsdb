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

class Event:
    def __init__(self):
        self.idEvent = ""
        self.idSoccerXML = ""
        self.strEvent = ""
        self.strFilename = ""
        self.strSport = ""
        self.idLeague = ""
        self.strLeague = ""
        self.strSeason = ""
        self.strDescriptionEN = ""
        self.strHomeTeam = ""
        self.strAwayTeam = ""
        self.intHomeScore = ""
        self.intRound = ""
        self.intAwayScore = ""
        self.intSpectators = ""
        self.strHomeGoalDetails = ""
        self.strHomeRedCards = ""
        self.strHomeYellowCards = ""
        self.strHomeLineupGoalkeeper = ""
        self.strHomeLineupDefense = ""
        self.strHomeLineupMidfield = ""
        self.strHomeLineupForward = ""
        self.strHomeLineupSubstitutes = ""
        self.strHomeFormation = ""
        self.strAwayRedCards = ""
        self.strAwayYellowCards = ""
        self.strAwayGoalDetails = ""
        self.strAwayLineupGoalkeeper = ""
        self.strAwayLineupDefense = ""
        self.strAwayLineupMidfield = ""
        self.strAwayLineupForward = ""
        self.strAwayLineupSubstitutes = ""
        self.strAwayFormation = ""
        self.intHomeShots = ""
        self.intAwayShots = ""
        self.dateEvent = ""
        self.strDate = ""
        self.strTime = ""
        self.strTVStation = ""
        self.idHomeTeam = ""
        self.idAwayTeam = ""
        self.strResult = ""
        self.strCircuit = ""
        self.strCountry = ""
        self.strCity = ""
        self.strPoster = ""
        self.strFanart = ""
        self.strThumb = ""
        self.strBanner = ""
        self.strMap = ""
        self.strLocked = ""

    def strDescription(self,language=None):
        return self.strDescriptionEN

def as_event(d):
    e = Event()
    e.__dict__.update(d)
    return e
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
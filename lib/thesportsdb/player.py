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

class Player:
    def __init__(self):
        self.idPlayer = ""
        self.idTeam = ""
        self.idSoccerXML = ""
        self.idPlayerManager = ""
        self.strNationality = ""
        self.strPlayer = ""
        self.strTeam = ""
        self.strSport = ""
        self.intSoccerXMLTeamID = ""
        self.dateBorn = ""
        self.dateSigned = ""
        self.strSigning = ""
        self.strWage = ""
        self.strBirthLocation = ""
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
        self.strPosition = ""
        self.strCollege = ""
        self.strFacebook = ""
        self.strWebsite = ""
        self.strTwitter = ""
        self.strInstagram = ""
        self.strYoutube = ""
        self.strHeight = ""
        self.strWeight = ""
        self.intLoved = ""
        self.strThumb = ""
        self.strCutout = ""
        self.strFanart1 = ""
        self.strFanart2 = ""
        self.strFanart3 = ""
        self.strFanart4 = ""
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


def as_player(d):
    p = Player()
    p.__dict__.update(d)
    return p
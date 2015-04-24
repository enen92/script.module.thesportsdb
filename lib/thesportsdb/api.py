'''
    script.module.thesportsdb - Python wrapper for thesportsdb API methods 
    Copyright (C) 2015 enen92

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
import json,urllib,urllib2

API_BASE_URL = 'http://www.thesportsdb.com/api/v1/json'

class Search:
	
	def __init__(self,API_KEY):
		self.API_KEY = API_KEY
	
	def searchteams(self,TeamName):
		url = '%s/%s/searchteams.php?t=%s' % (API_BASE_URL,self.API_KEY,str(TeamName))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def searchplayers(self,TeamName,PlayerName):
		if TeamName and not PlayerName:
			url = '%s/%s/searchplayers.php?t=%s' % (API_BASE_URL,self.API_KEY,str(TeamName))
		elif PlayerName and not TeamName:
			url = '%s/%s/searchplayers.php?p=%s' % (API_BASE_URL,self.API_KEY,str(PlayerName))
		else:
			url = '%s/%s/searchplayers.php?t=%s&p=%s' % (API_BASE_URL,self.API_KEY,str(TeamName),str(PlayerName))
		data = json.load(urllib2.urlopen(url))
		return data
	
	def searchevents(self,Event,Season):
		if Event and not Season:
			url = '%s/%s/searchevents.php?e=%s' % (API_BASE_URL,self.API_KEY,str(Event))
		else:
			url = '%s/%s/searchevents.php?e=%s&s=%s' % (API_BASE_URL,self.API_KEY,str(Event),str(Season))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def search_all_leagues(self,CountryName,SportName,LeagueName):
		if SportName and not CountryName:
			url = '%s/%s/search_all_leagues.php?s=%s' % (API_BASE_URL,self.API_KEY,str(SportName))
		elif SportName and CountryName:
			url = '%s/%s/search_all_leagues.php?s=%s&c=%s' % (API_BASE_URL,self.API_KEY,str(SportName),str(CountryName))
		else:
			if LeagueName:
				url = '%s/%s/search_all_teams.php?l=%s' % (API_BASE_URL,self.API_KEY,str(LeagueName))
			else:
				url = '%s/%s/search_all_leagues.php?&c=%s' % (API_BASE_URL,self.API_KEY,str(CountryName))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def search_all_teams(self,LeagueName):
		url = '%s/%s/search_all_teams.php?l=%s' % (API_BASE_URL,self.API_KEY,str(LeagueName))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def search_loves(self,Username):
		url = '%s/%s/searchloves.php?u=%s' % (API_BASE_URL,self.API_KEY,str(Username))
		data = json.load(urllib2.urlopen(url))
		return data
	
	

class Lookups:
	def __init__(self,API_KEY):
		self.API_KEY = API_KEY
		
	def lookupleague(self,LeagueId):
		url = '%s/%s/lookupleague.php?id=%s' % (API_BASE_URL,self.API_KEY,str(LeagueId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def lookupteam(self,TeamId):
		url = '%s/%s/lookupteam.php?id=%s' % (API_BASE_URL,self.API_KEY,str(TeamId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def lookupplayer(self,PlayerId):
		url = '%s/%s/lookuplayer.php?id=%s' % (API_BASE_URL,self.API_KEY,str(PlayerId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def lookupevent(self,EventId):
		url = '%s/%s/lookupevent.php?id=%s' % (API_BASE_URL,self.API_KEY,str(EventId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def lookup_all_teams(self,LeagueId):
		url = '%s/%s/lookup_all_teams.php?id=%s' % (API_BASE_URL,self.API_KEY,str(LeagueId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def lookup_all_players(self,TeamId):
		url = '%s/%s/lookup_all_players.php?id=%s' % (API_BASE_URL,self.API_KEY,str(TeamId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def lookup_leaguetables(self,LeagueId,Season):
		if Season: url = '%s/%s/lookuptable.php?l=%s&s=%s' % (API_BASE_URL,self.API_KEY,str(LeagueId),str(Season))
		else: url = '%s/%s/lookuptable.php?l=%s' % (API_BASE_URL,self.API_KEY,str(LeagueId))
		data = json.load(urllib2.urlopen(url))
		return data
		
		
class Schedules:
	def __init__(self,API_KEY):
		self.API_KEY = API_KEY
	
	def eventsnext(self,TeamId):
		url = '%s/%s/eventsnext.php?id=%s' % (API_BASE_URL,self.API_KEY,str(TeamId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def eventslast(self,TeamId):
		url = '%s/%s/eventslast.php?id=%s' % (API_BASE_URL,self.API_KEY,str(TeamId))
		data = json.load(urllib2.urlopen(url))
		return data
	
	def eventsnextleague(self,LeagueId):
		url = '%s/%s/eventsnextleague.php?id=%s' % (API_BASE_URL,self.API_KEY,str(LeagueId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def eventspastleague(self,LeagueId):
		url = '%s/%s/eventspastleague.php?id=%s' % (API_BASE_URL,self.API_KEY,str(LeagueId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def eventsday(self,Day,Sport,League):
		if Day and Sport:
			url = '%s/%s/eventsday.php?d=%s&s=%s' % (API_BASE_URL,self.API_KEY,str(Day),str(Sport))
		elif Day and League:
			url = '%s/%s/eventsday.php?d=%s&l=%s' % (API_BASE_URL,self.API_KEY,str(Day),str(League))
		elif Day and not League and not Sport:
			url = '%s/%s/eventsday.php?d=%s' % (API_BASE_URL,self.API_KEY,str(Day))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def eventsround(self,League,Round,Season):
		if League and Round and not Season:
			url = '%s/%s/eventsround.php?id=%s&r=%s' % (API_BASE_URL,self.API_KEY,str(League),str(Round))
		elif League and Round and Season:
			url = '%s/%s/eventsday.php?id=%s&r=%s&s=%s' % (API_BASE_URL,self.API_KEY,str(League),str(Round),str(Season))
		data = json.load(urllib2.urlopen(url))
		return data

class LiveScores:
	def __init__(self,API_KEY):
		self.API_KEY = API_KEY
		
	def latestsoccer(self):
		url = '%s/%s/latestsoccer.php' % (API_BASE_URL,self.API_KEY)
		data = json.load(urllib2.urlopen(url))
		return data

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

API_KEY = '1'
API_BASE_URL = 'http://www.thesportsdb.com/api/v1/json'

class Search:
	
	def __init__(self):
		pass
	
	def searchteams(self,TeamName=None):
		url = '%s/%s/searchteams.php?t=%s' % (API_BASE_URL,API_KEY,str(TeamName))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def searchplayers(self,TeamName=None,PlayerName=None):
		if TeamName and not PlayerName:
			url = '%s/%s/searchplayers.php?t=%s' % (API_BASE_URL,API_KEY,str(TeamName)
		elif not TeamName and PlayerName:
			url = '%s/%s/searchplayers.php?p=%s' % (API_BASE_URL,API_KEY,str(PlayerName))
		else:
			url = '%s/%s/searchplayers.php?t=%s&p=%s' % (API_BASE_URL,API_KEY,str(TeamName),str(PlayerName))
		data = json.load(urllib2.urlopen(url))
		return data
	
	def searchevents(self,Event=None,Season=None):
		if Event and not Season:
			url = '%s/%s/searchevents.php?e=%s' % (API_BASE_URL,API_KEY,str(Event))
		else:
			url = '%s/%s/searchevents.php?e=%s&s=%s' % (API_BASE_URL,API_KEY,str(Event),str(Season))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def search_all_leagues(self,CountryName=None,SportName=None):
		if SportName and not CountryName:
			url = '%s/%s/search_all_leagues.php?s=%s' % (API_BASE_URL,API_KEY,str(SportName))
		elif SportName and CountryName:
			url = '%s/%s/search_all_leagues.php?s=%s&c=%s' % (API_BASE_URL,API_KEY,str(SportName),str(CountryName))
		else:
			url = '%s/%s/search_all_leagues.php?&c=%s' % (API_BASE_URL,API_KEY,str(CountryName))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def search_all_leagues(self,LeagueName=None)
		url = '%s/%s/search_all_teams.php?l=%s' % (API_BASE_URL,API_KEY,str(LeagueName))
		data = json.load(urllib2.urlopen(url))
		return data
	

class Lookups:
	def __init__(self):
		pass
		
	def lookupleague(self,LeagueId=None):
		url = '%s/%s/lookupleague.php?id=%s' % (API_BASE_URL,API_KEY,str(LeagueId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def lookupteam(self,TeamId=None):
		url = '%s/%s/lookupteam.php?id=%s' % (API_BASE_URL,API_KEY,str(TeamId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def lookupplayer(self,PlayerId=None):
		url = '%s/%s/lookuplayer.php?id=%s' % (API_BASE_URL,API_KEY,str(PlayerId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def lookupevent(self,EventId=None):
		url = '%s/%s/lookuevent.php?id=%s' % (API_BASE_URL,API_KEY,str(EventId))
		data = json.load(urllib2.urlopen(url))
		return data
		
		
class Schedules:
	def __init__(self):
		pass
	
	def eventsnext(self,TeamId)
		url = '%s/%s/eventsnext.php?id=%s' % (API_BASE_URL,API_KEY,str(TeamId))
		data = json.load(urllib2.urlopen(url))
		return data
		
	def eventslast(self,TeamId)
		url = '%s/%s/eventslast.php?id=%s' % (API_BASE_URL,API_KEY,str(TeamId))
		data = json.load(urllib2.urlopen(url))
		return data
	
	def eventsnextleague(self,LeagueId)
		url = '%s/%s/eventsnextleague.php?id=%s' % (API_BASE_URL,API_KEY,str(LeagueId))
		data = json.load(urllib2.urlopen(url))
		return data
	

class LiveScores:
	def __init__(self):
		pass
		
	def latestsoccer(self):
		url = '%s/%s/latestsoccer.php' % (API_BASE_URL,API_KEY)
		data = json.load(urllib2.urlopen(url))
		return data

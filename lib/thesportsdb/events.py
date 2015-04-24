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
import datetime
import re

class Events:
	
	def __init__(self,API_KEY=None):
		pass
		
	def get_datetime_object(self,event):
		event_date = self.get_eventdate(event)
		event_time = self.get_time(event)
		if event_date and event_date != 'null' and event_date != 'None':
			date_array = event_date.split('-')
			year = date_array[0]
			month = date_array[1]
			day = date_array[2]
			if event_time and event_time != 'null' and event_time != 'None':
				event_timematch = re.compile('(.+?)\+').findall(event_time)
				event_timetmp = event_timematch[0].split(':')
				hour = event_timetmp[0]
				minute = event_timetmp[1]
				return datetime.datetime(int(year), int(month), int(day), hour=int(hour), minute=int(minute))
			else: return datetime.datetime(int(year), int(month), int(day))
		else: return
		
	def get_homeredcards(self,event):
		return event["strHomeRedCards"]
		
	def get_leagueid(self,event):
		return str(event["idLeague"])
	
	def get_awayredcards(self,event):
		return event["strAwayRedCards"]
		
	def get_awayteamid(self,event):
		return str(event["idAwayTeam"])
		
	def get_awayteamname(self,event):
		return event["strAwayTeam"]
		
	def get_eventdate(self,event):
		return event["dateEvent"]
		
	def get_awayscore(self,event):
		return event["intAwayScore"]
		
	def get_spectators(self,event):
		return event["intSpectators"]
		
	def get_homescore(self,event):
		return event["intHomeScore"]
		
	def get_racecountry(self,event):
		return event["strRaceCountry"]
	
	def get_eventtitle(self,event):
		return event["strEvent"]
		
	def get_round(self,event):
		return event["intRound"]
		
	def get_tvstation(self,event):
		return event["strTVStation"]
		
	def get_hometeamname(self,event):
		return event["strHomeTeam"]
		
	def get_date(self,event):
		return event["strDate"]
		
	def get_homegoaldetails(self,event):
		return event["strHomeGoalDetails"]
	
	def get_awaygoaldetails(self,event):
		return event["strAwayGoalDetails"]
		
	def get_homeshots(self,event):
		return event["intHomeShots"]
		
	def get_season(self,event):
		return event["strSeason"]
		
	def get_sport(self,event):
		return event["strSport"]
		
	def get_awayshots(self,event):
		return event["intAwayShots"]
		
	def get_eventid(self,event):
		return event["idEvent"]
		
	def get_awayyellowcards(self,event):
		return event["strAwayYellowCards"]
		
	def get_homeyellowcards(self,event):
		return event["strHomeYellowCards"]
		
	def get_league(self,event):
		return event["strLeague"]
		
	def get_racelocation(self,event):
		return event["strRaceLocality"]
		
	def get_hometeamid(self,event):
		return event["idHomeTeam"]
		
	def get_homeformation(self,event):
		return event["strHomeFormation"]
		
	def get_homegoalkeeper(self,event):
		return event["strHomeLineupGoalkeeper"]
		
	def get_awaygoalkeeper(self,event):
		return event["strAwayLineupGoalkeeper"]
		
	def get_homedefense(self,event):
		return event["strHomeLineupDefense"]
		
	def get_awaydefense(self,event):
		return event["strAwayLineupDefense"]
		
	def get_homemidfielders(self,event):
		return event["strHomeLineupMidfield"]
		
	def get_awaymidfielders(self,event):
		return event["strAwayLineupMidfield"]
		
	def get_homeforward(self,event):
		return event["strHomeLineupForward"]
		
	def get_awayforward(self,event):
		return event["strAwayLineupForward"]
		
	def get_homesubs(self,event):
		return event["strHomeLineupSubstitutes"]
		
	def get_awaysubs(self,event):
		return event["strAwayLineupSubstitutes"]
		
	def get_awayformation(self,event):
		return event["strAwayFormation"]
		
	def get_time(self,event):
		return event["strTime"]
	

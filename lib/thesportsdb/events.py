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

class Events:
	
	def __init__(self):
		pass
	
	def get_awayredcards(self,event):
		return event["strAwayRedCards"]
		
	def get_awayteamid(self,event):
		return event["idAwayTeam"]
		
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
	
	def get_eventtile(self,event):
		return event["strEvent"]
		
	def get_round(self,event):
		return event["intRound"]
		
	def get_tvstation(self,event):
		return event["strTVStation"]
		
	def get_hometeam(self,event):
		return event["strHomeTeam"]
		
	def get_date(self,event):
		return event["strDate"]
		
	def get_homegoaldetails(self,event):
		return event["strHomeGoalDetails"]
		
	def get_homeshots(self,event):
		return event["intHomeShots"]
		
	def get_season(self,event):
		return event["strSeason"]
		
	def get_sport(self,event):
		return event["Soccer"]
		
	def get_awayshots(self,event):
		return event["intAwayShots"]
		
	def get_eventid(self,event):
		return event["idEvent"]
		
	def get_awayyellowcards(self,event):
		return event["strAwayYellowCards"]
		
	def get_league(self,event):
		return event["strLeague"]
		
	def get_racelocation(self,event):
		return event["strRaceLocality"]
		
	def get_hometeamid(self,event):
		return event["idHomeTeam"]
	

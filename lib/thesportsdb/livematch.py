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

class Livematch:
	
	def __init__(self):
		pass
		
	#event
	
	def get_location(self,event):
		return event["Location"]
		
	def get_stadium(self,event):
		return event["Stadium"]
		
	def get_referee(self,event):
		return event["Referee"]
		
	def get_spectators(self,event):
		return str(event["Spectators"])
	
	def get_date(self,event):
		return event["Date"]
		
	def get_league(self,event):
		return event["League"]
	
	def get_time(self,event):
		return event["Time"]
		
	def get_round(self,event):
		return event["Round"]
	
	
		
	#hometeam
		
	def get_homegoalkeeper(self,event):
		return event["HomeLineupGoalkeeper"]
		
	def get_homedefense(self,event):
		return event["HomeLineupDefense"]
		
	def get_homecoach(self,event):
		return event["HomeLineupCoach"]
	
	def get_homeformation(self,event):
		return event["HomeTeamFormation"]
		
	
	def get_homeforward(self,event):
		return event["HomeLineupForward"]
		
	def get_homeredcards(self,event):
		return event["HomeTeamRedCardDetails"]
		
	def get_homeyellowcards(self,event):
		return event["HomeTeamYellowCardDetails"]
		
	def get_home_id(self, event):
		return str(event["HomeTeam_Id"])
		
	def get_home_name(self,event):
		return event["Hometeam"]
		
	def get_homegoals_number(self,event):
		return str(event["HomeGoals"])
		
	def get_homegoals_detail(self,event):
		return event["HomeGoalDetails"]
		
	def get_homesubs(self,event):
		return event["HomeLineupSubstitutes"]
		
	def get_homemidfield(self,event):
		return event["HomeLineupMidfield"]
		
	def get_home_subdetails(self,event):
		return event["HomeSubDetails"]
		
	#away
		
	def get_awaysubs(self,event):
		return event["AwayLineupSubstitutes"]
		
	def get_awayyellow(self,event):
		return event["AwayTeamYellowCardDetails"]
		
	def get_awaycoach(self,event):
		return event["AwayLineupCoach"]
		
	def get_awayforward(self,event):
		return event["AwayLineupForward"]
		
	def get_awaymidfielder(self,event):
		return event["AwayLineupMidfield"]
		
	def get_away_id(self,event):
		return str(event["AwayTeam_Id"])
		
	def get_away_goalkeeper(self,event):
		return event["AwayLineupGoalkeeper"]
		
	def get_awaygoals_number(self,event):
		return event["AwayGoals"]
		
	def get_awayformation(self,event):
		return event["AwayTeamFormation"]
		
	def get_awaydefense(self,event):
		return event["AwayLineupDefense"]
		
	def get_away_name(self,event):
		return event["Awayteam"]
		
	def get_away_redcards(self,event):
		return event["AwayTeamRedCardDetails"]
		
	def get_away_goaldetails(self,event):
		return event["AwayGoalDetails"]
		
	def get_away_subdetails(self,event):
		return event["AwaySubDetails"]
		
	def get_awaygoals_number(self,event):
		return str(event["AwayGoals"])
		


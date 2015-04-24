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

class Tables:
	
	def __init__(self,API_KEY=None):
		pass
	
	def get_name(self,TeamEntry):
		return TeamEntry["name"]
		
	def get_id(self,TeamEntry):
		return TeamEntry["teamid"]
		
	def get_totalplayed(self,TeamEntry):
		return str(TeamEntry["played"])
		
	def get_goalsscored(self,TeamEntry):
		return str(TeamEntry["goalsfor"])
		
	def get_goalssuffered(self,TeamEntry):
		return str(TeamEntry["goalsagainst"])

	def get_goalsdifference(self,TeamEntry):
		return str(TeamEntry["goalsdifference"])
		
	def get_wins(self,TeamEntry):
		return str(TeamEntry["win"])
		
	def get_draws(self,TeamEntry):
		return str(TeamEntry["draw"])
		
	def get_loss(self,TeamEntry):
		return str(TeamEntry["loss"])
		
	def get_points(self,TeamEntry):
		return str(TeamEntry["total"])


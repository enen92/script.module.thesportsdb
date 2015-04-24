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
import api

class User:
	
	def __init__(self,API_KEY):
		self.API_KEY = API_KEY
	
	def get_favourite_teams(self,user):
		favourite_teams = []
		result = api.Search(self.API_KEY).search_loves(user)["players"]
		if result:
			for entry in result:
				if entry["strEditType"] == "Updated Team Loved":
					if entry["idTeam"]:
						favourite_teams.append(entry["idTeam"])
		return favourite_teams
		

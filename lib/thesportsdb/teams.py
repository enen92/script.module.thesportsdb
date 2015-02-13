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

class Teams:
	
	def __init__(self):
		pass
	
	def get_id(self,team):
		return str(team["idTeam"])
		
	def get_likes(self,team):
		return str(team["intLoved"])
	
	def get_name(self,team):
		return team["strTeam"]
		
	def get_shortname(self,team):
		return str(team["strTeamShort"])
		
	def get_alternativename(self,team):
		return str(team["strAlternate"])
		
	def get_formedyear(self,team):
		return str(team["intFormedYear"])
		
	def get_sport(self,team):
		return str(team["strSport"])
		
	def get_league(self,team):
		return str(team["strLeague"])
		
	def get_league_id(self,team):
		return str(team["idLeague"])
		
	def get_division(self,team):
		return str(team["strDivision"])
		
	def get_manager(self,team):
		return str(team["strManager"])
		
	def get_stadium(self,team):
		return str(team["strStadium"])
	
	def get_stadium_thumb(self,team):
		return str(team["strStadiumThumb"])
		
	def get_team_jersey(self,team):
		return str(team["strTeamJersey"])
		
	def get_stadium_plot(self,team):
		return str(team["strStadiumDescription"])
		
	def get_stadium_location(self,team):
		return str(team["strStadiumLocation"])
		
	def get_stadium_capacity(self,team):
		return str(team["intStadiumCapacity"])
		
	def get_team_website(self,team):
		return str(team["strWebsite"])
		
	def get_team_facebook(self,team):
		return str(team["strFacebook"])
		
	def get_team_twitter(self,team):
		return str(team["strTwitter"])
		
	def get_team_instagram(self,team):
		return str(team["strInstagram"])
		
	def get_team_youtube(self,team):
		return str(team["strYoutube"])
		
	def get_plot_en(self,team):
		return team["strDescriptionEN"]
		
	def get_plot_de(self,team):
		plot = team["strDescriptionDE"]
		if not plot: plot = self.get_plot_en(team)
		return plot
		
	def get_plot_fr(self,team):
		plot = team["strDescriptionFR"]
		if not plot: plot = self.get_plot_en(team)
		return plot

	def get_plot_it(self,team):
		plot = team["strDescriptionIT"]
		if not plot: plot = self.get_plot_en(team)
		return plot
		
	def get_plot_cn(self,team):
		plot = team["strDescriptionCN"]
		if not plot: plot = self.get_plot_en(team)
		return plot
	
	def get_plot_jp(self,team):
		plot = team["strDescriptionJP"]
		if not plot: plot = self.get_plot_en(team)
		return plot
		
	def get_plot_ru(self,team):
		plot = team["strDescriptionRU"]
		if not plot: plot = self.get_plot_en(team)
		return plot
		
	def get_plot_es(self,team):
		plot = team["strDescriptionES"]
		if not plot: plot = self.get_plot_en(team)
		return plot
		
	def get_plot_pt(self,team):
		plot = team["strDescriptionPT"]
		if not plot: plot = self.get_plot_en(team)
		return plot
		
	def get_plot_se(self,team):
		plot = team["strDescriptionSE"]
		if not plot: plot = self.get_plot_en(team)
		return plot
		
	def get_plot_nl(self,team):
		plot = team["strDescriptionJP"]
		if not plot: plot = self.get_plot_en(team)
		return plot
		
	def get_plot_hu(self,team):
		plot = team["strDescriptionHU"]
		if not plot: plot = self.get_plot_en(team)
		return plot
		
	def get_plot_no(self,team):
		plot = team["strDescriptionNO"]
		if not plot: plot = self.get_plot_en(team)
		return plot
		
	def get_plot_pl(self,team):
		plot = team["strDescriptionPL"]
		if not plot: plot = self.get_plot_en(team)
		return plot
		
	def get_gender(self,team):
		return team["strGender"]
		
	def get_country(self,team):
		return team["strCountry"]
	
	def get_fanart_list(self,team):
		fanart_list = []
		if team["strTeamFanart1"]: fanart_list.append(team["strTeamFanart1"])
		if team["strTeamFanart2"]: fanart_list.append(team["strTeamFanart2"])
		if team["strTeamFanart3"]: fanart_list.append(team["strTeamFanart3"])
		if team["strTeamFanart4"]: fanart_list.append(team["strTeamFanart4"])
		return fanart_list
		
	def get_fanart_general1(self,team):
		return team["strTeamFanart1"]
		
	def get_fanart_general2(self,team):
		return team["strTeamFanart2"]
		
	def get_fanart_general_list(self,team):
		fanart_list = []
		if team["strTeamFanart1"]: fanart_list.append(team["strTeamFanart1"])
		if team["strTeamFanart2"]: fanart_list.append(team["strTeamFanart2"])
		return fanart_list
	
	def get_fanart_player(self,team):
		return team["strTeamFanart3"]
		
	def get_fanart_fans(self,team):
		return team["strTeamFanart4"]
		
	def get_banner(self,team):
		return str(team["strTeamBanner"])
		
	def get_badge(self,team):
		return team["strTeamBadge"]
		
	def get_logo(self,team):
		return str(team["strTeamLogo"])

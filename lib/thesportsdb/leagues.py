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
class Leagues:
	
	def __init__(self):
		pass
	
	def get_id(self,league):
		return str(league["idLeague"])
		
	def get_sport(self,league):
		return str(league["strSport"])
		
	def get_name(self,league):
		return league["strLeague"]
		
	def get_formedyear(self,league):
		return str(league["intFormedYear"])
		
	def get_gender(self,league):
		return str(league["strGender"])
		
	def get_rssurl(self,team):
		return team["strRSS"]
	
	def get_country(self,league):
		return str(league["strCountry"])
		
	def get_website(self,league):
		return str(league["strWebsite"])
		
	def get_facebook(self,league):
		return str(league["strFacebook"])
		
	def get_twitter(self,league):
		return str(league["strTwitter"])
		
	def get_youtube(self,league):
		return str(league["strYoutube"])
		
	def get_plot_en(self,league):
		return league["strDescriptionEN"]
		
	def get_plot_de(self,league):
		plot = league["strDescriptionDE"]
		if not plot: plot = self.get_plot_en(league)
		return plot
		
	def get_plot_fr(self,league):
		plot = league["strDescriptionFR"]
		if not plot: plot = self.get_plot_en(league)
		return plot

	def get_plot_it(self,league):
		plot = league["strDescriptionIT"]
		if not plot: plot = self.get_plot_en(league)
		return plot
		
	def get_plot_cn(self,league):
		plot = league["strDescriptionCN"]
		if not plot: plot = self.get_plot_en(league)
		return plot
	
	def get_plot_jp(self,league):
		plot = league["strDescriptionJP"]
		if not plot: plot = self.get_plot_en(league)
		return plot
		
	def get_plot_ru(self,league):
		plot = league["strDescriptionRU"]
		if not plot: plot = self.get_plot_en(league)
		return plot
		
	def get_plot_es(self,league):
		plot = league["strDescriptionES"]
		if not plot: plot = self.get_plot_en(league)
		return plot
		
	def get_plot_pt(self,league):
		plot = league["strDescriptionPT"]
		if not plot: plot = self.get_plot_en(league)
		return plot
		
	def get_plot_se(self,league):
		plot = league["strDescriptionSE"]
		if not plot: plot = self.get_plot_en(league)
		return plot
		
	def get_plot_nl(self,league):
		plot = league["strDescriptionJP"]
		if not plot: plot = self.get_plot_en(league)
		return plot
		
	def get_plot_hu(self,league):
		plot = league["strDescriptionHU"]
		if not plot: plot = self.get_plot_en(league)
		return plot
		
	def get_plot_no(self,league):
		plot = league["strDescriptionNO"]
		if not plot: plot = self.get_plot_en(league)
		return plot
		
	def get_plot_pl(self,league):
		plot = league["strDescriptionPL"]
		if not plot: plot = self.get_plot_en(league)
		return plot
	
	def get_fanart(self,league):
		fanart_list = []
		if league["strFanart1"]: fanart_list.append(league["strFanart1"])
		if league["strFanart2"]: fanart_list.append(league["strFanart2"])
		if league["strFanart3"]: fanart_list.append(league["strFanart3"])
		if league["strFanart4"]: fanart_list.append(league["strFanart4"])
		return fanart_list
		
	def get_banner(self,league):
		return str(league["strBanner"])
		
	def get_badge(self,league):
		return str(league["strBadge"])
		
	def get_logo(self,league):
		return str(league["strLogo"])
		
	def get_trophy(self,league):
		return str(league["strTrophy"])

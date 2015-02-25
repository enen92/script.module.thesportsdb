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

class Players:
	
	def __init__(self):
		pass
	
	def get_id(self,player):
		return str(player["idPlayer"])
		
	def get_teamid(self,player):
		return str(player["idTeam"])
		
	def get_manager(self,player):
		return str(player["idPlayerManager"])
		
	def get_nationality(self,player):
		return str(player["strNationality"])
		
	def get_name(self,player):
		return player["strPlayer"]
		
	def get_teamname(self,player):
		return str(player["strTeam"])
		
	def get_sport(self,player):
		return str(player["strSport"])
		
	def get_borndate(self,player):
		return str(player["dateBorn"])
		
	def get_bornlocation(self,player):
		return player["strBirthLocation"]
		
	def get_signeddate(self,player):
		return str(player["dateSigned"])
		
	def get_signedvalue(self,player):
		return player["strSigning"]
		
	def get_plot_en(self,player):
		return player["strDescriptionEN"]
		
	def get_plot_de(self,player):
		plot = player["strDescriptionDE"]
		if not plot: plot = self.get_plot_en(player)
		return plot
		
	def get_plot_fr(self,player):
		plot = player["strDescriptionFR"]
		if not plot: plot = self.get_plot_en(player)
		return plot

	def get_plot_it(self,player):
		plot = player["strDescriptionIT"]
		if not plot: plot = self.get_plot_en(player)
		return plot
		
	def get_plot_cn(self,player):
		plot = player["strDescriptionCN"]
		if not plot: plot = self.get_plot_en(player)
		return plot
	
	def get_plot_jp(self,player):
		plot = player["strDescriptionJP"]
		if not plot: plot = self.get_plot_en(player)
		return plot
		
	def get_plot_ru(self,player):
		plot = player["strDescriptionRU"]
		if not plot: plot = self.get_plot_en(player)
		return plot
		
	def get_plot_es(self,player):
		plot = player["strDescriptionES"]
		if not plot: plot = self.get_plot_en(player)
		return plot
		
	def get_plot_pt(self,player):
		plot = player["strDescriptionPT"]
		if not plot: plot = self.get_plot_en(player)
		return plot
		
	def get_plot_se(self,player):
		plot = player["strDescriptionSE"]
		if not plot: plot = self.get_plot_en(player)
		return plot
		
	def get_plot_nl(self,player):
		plot = player["strDescriptionJP"]
		if not plot: plot = self.get_plot_en(player)
		return plot
		
	def get_plot_hu(self,player):
		plot = player["strDescriptionHU"]
		if not plot: plot = self.get_plot_en(player)
		return plot
		
	def get_plot_no(self,player):
		plot = player["strDescriptionNO"]
		if not plot: plot = self.get_plot_en(player)
		return plot
		
	def get_plot_pl(self,player):
		plot = player["strDescriptionPL"]
		if not plot: plot = self.get_plot_en(player)
		return plot
		
	def get_gender(self,player):
		return str(player["strGender"])
		
	def get_position(self,player):
		return str(player["strPosition"])
		
	def get_college(self,player):
		return str(player["strCollege"])
		
	def get_facebook(self,player):
		return str(player["strFacebook"])
		
	def get_website(self,player):
		return str(player["strWebsite"])
		
	def get_twitter(self,player):
		return str(player["strTwitter"])
		
	def get_instagram(self,player):
		return str(player["strInstagram"])
		
	def get_height(self,player):
		return str(player["strHeight"])
		
	def get_weight(self,player):
		return str(player["strWeight"])
	
	def get_likes(self,player):
		return player["intLoved"]
		
	def get_thumb(self,player):
		return player["strThumb"]
	
	def get_cutout(self,player):
		return player["strCutout"]
		
	def get_face(self,player):
		face = self.get_cutout(player)
		if not face:
			face = self.get_thumb(player)
		return face
		
	def get_fanart1(self,player):
		return player["strFanart1"]
		
	def get_fanart2(self,player):
		return player["strFanart2"]
		
	def get_fanar3(self,player):
		return player["strFanart3"]
		
	def get_fanart4(self,player):
		return player["strFanart4"]
		
	def get_fanart_list(self,player):
		fanart_list = []
		if player["strFanart1"]: fanart_list.append(player["strFanart1"])
		if player["strFanart2"]: fanart_list.append(player["strFanart2"])
		if player["strFanart3"]: fanart_list.append(player["strFanart3"])
		if player["strFanart4"]: fanart_list.append(player["strFanart4"])
		return fanart_list

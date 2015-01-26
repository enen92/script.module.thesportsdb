# script.module.thesportsdb
![TheSportsDb Icon](http://s11.postimg.org/5cq70m2j7/icon.png)

A python module packaged for Kodi to wrap the main thesportsdb API methods.

Work in progress. 
At the moment, only the queries are implemented without any further parsing of the obtained results

##Usage

###Addon.xml
The module most be imported in the addon.xml of your addon
```xml
<import addon="script.module.thesportsdb"/>
```

###Pythonic usage

The module follows the api structure mentioned [Here](http://www.thesportsdb.com/forum/viewtopic.php?f=6&t=5)

Every group method (Search,Lookups,Schedules,Livescores) is a python class; every method (e.g lookupleague) is a function of the respective group method. Arguments must be urlencoded and can be of any type (they all will be converted to strings).
See example below:

```python
import thesportsdb
print thesportsdb.Search().searchteams("arsenal")
```
Every function returns a python dictionary.

###Query methods

####Search
* Search teams a by name
```python
thesportsdb.Search().searchteams(TeamName)
```
`eg:thesportsdb.Search().searchteams("arsenal")`

* Search player by name (or player in team)
```python
thesportsdb.Search().searchplayers(TeamName,PlayerName)
```
`eg: thesportsdb.Search().searchplayers(None,"messi")`
`eg: thesportsdb.Search().searchplayers("barcelona","messi")`

* Search event by name and season
```python
thesportsdb.Search().searchevents(Event,Season)
```
`eg:thesportsdb.Search().searchevents("arsenal%20chelsea",None)` returns all matched events
`eg:thesportsdb.Search().searchevents("arsenal%20chelsea","1415")` returns all matched events for specified season

* Search leagues by sport and country
```python
thesportsdb.Search().search_all_leagues(SportName,CountryName,LeagueName)
```
`eg:thesportsdb.Search().search_all_leagues("soccer",None,None)` returns all leagues by sport
`eg:thesportsdb.Search().search_all_leagues("soccer","england",None)` returns all leagues by sport and country
`eg:thesportsdb.Search().search_all_leagues(None,None,"English%20Premier%20League")` returns all leagues by sport and country

* Search all teams in a League:
```python
thesportsdb.Search().search_all_teams(LeagueName)
```
`eg:thesportsdb.Search().search_all_teams("English%20Premier%20League")`

####Lookups

* Lookup league by league id
```python
thesportsdb.Lookups().lookupleague(LeagueId)
```
`eg:thesportsdb.Lookups().lookupleague(4346)`

* Lookup team by team id
```python
thesportsdb.Lookups().lookupteam(TeamId)
```
`eg:thesportsdb.Lookups().lookupteam(133604)`

* Lookup player by player id
```python
thesportsdb.Lookups().lookupplayer(PlayerId)
```
`eg:thesportsdb.Lookups().lookupplayer(34145937)`

* Lookup event by event id
```python
thesportsdb.Lookups().lookupevent(EventId)
```
`eg:thesportsdb.Lookups().lookupevent(441613)`

####Schedules

* Returns the next 5 events for a specific teamID
```python
thesportsdb.Schedules().eventsnext(TeamId)
```
`eg:thesportsdb.Schedules().eventsnext(133604)`

* Returns the last 5 events for a specific teamID
```python
thesportsdb.Schedules().eventslast(TeamId)
```
`eg:thesportsdb.Schedules().eventslast(133604)`

* Returns next events for a League
```python
thesportsdb.Schedules().eventsnextleague(LeagueId)
```
`eg:thesportsdb.Schedules().eventsnextleague(4346)`

####LiveScores

* Returns the livescores for soccer
```python
thesportsdb.LiveScores().latestsoccer()
```


###Parsing methods methods

Parsing methods receive a dictionary object and return the desired property of the league, team or event object. See example below:

```python
import thesportsdb
league = thesportsdb.Lookups().lookupleague(4346)
print thesportsdb.Leagues().get_badge(league)
```

####Leagues

* Returns league ID for the provided league object
```python
thesportsdb.Leagues().get_id(League)
```

* Returns the sport for the provided league object
```python
thesportsdb.Leagues().get_sport(League)
```

* Returns league name for the provided league object
```python
thesportsdb.Leagues().get_name(League)
```

* Returns league ID for the provided league object
```python
thesportsdb.Leagues().get_formedyear(League)
```

* Returns league gender for the provided league object
```python
thesportsdb.Leagues().get_gender(League)
```

* Returns league country for the provided league object
```python
thesportsdb.Leagues().get_country(League)
```

* Returns league website for the provided league object
```python
thesportsdb.Leagues().get_website(League)
```

* Returns league facebook for the provided league object
```python
thesportsdb.Leagues().get_facebook(League)
```

* Returns league twitter for the provided league object
```python
thesportsdb.Leagues().get_twitter(League)
```

* Returns league youtube for the provided league object
```python
thesportsdb.Leagues().get_youtube(League)
```

* Returns league plot in english
```python
thesportsdb.Leagues().get_plot_en(League)
```
Note: get_plot_de,get_plot_fr,get_plot_it,get_plot_cn,get_plot_jp,get_plot_ru,get_plot_es,get_plot_pt,get_plot_pt,get_plot_nl,get_plot_hu,get_plot_no,get_plot_pl returns the league plot in the respective language and fallback to english plot if it does not exist.

* Returns league fanart
```python
thesportsdb.Leagues().get_fanart(League)
```
The output of this function is a python list containing all the available fanarts. It does return an empty list if none is available

* Returns league banner
```python
thesportsdb.Leagues().get_banner(League)
```

* Returns league badge
```python
thesportsdb.Leagues().get_badge(League)
```

* Returns league logo (clear art)
```python
thesportsdb.Leagues().get_logo(League)
```

* Returns league trophy (clear art)
```python
thesportsdb.Leagues().get_trophy(League)
```

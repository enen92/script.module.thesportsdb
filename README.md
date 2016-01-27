# script.module.thesportsdb
![TheSportsDb Icon](http://s17.postimg.org/h3eanic3z/icon.png)

A python module packaged as a Kodi script module to wrap all thesportsdb API methods and for you to use on your own addon

*Work/documentation in progress.....

##Usage

###Addon.xml
The module most be imported in the addon.xml of your addon and pointing to the correct version of the module
```xml
<import addon="script.module.thesportsdb" version="1.0.0"/>
```

###Pythonic usage

The module follows the API structure described [Here](http://www.thesportsdb.com/forum/viewtopic.php?f=6&t=5). Every group method (Search,Lookups,Schedules,Livescores) is a Python class and all the endpoints (eg: lookupleague) is part of a class method. The module maps the json data to objects as much as possible, so each call returns one or more Team objects, League objects, Player objects, Livescores objects, Table objects, etc. Below all the classes and methods are explained with examples. Object properties are detailed later despite being exemplified some times.

###A really simple usage example...

```python
import thesportsdb
api = thesportsdb.Api(key="1")
players = api.Search().Players(team="Arsenal")
for player in players:
    print(player.strPlayer)
```

###Module methods

####Search
* Search for teams by name - (returns a list of team objects)
```python
teams = api.Search().Teams(team="Arsenal")
```

* Search for all teams in a League - (returns a list of team objects)
```python
teams = api.Search().Teams(league="English Premier League")
```

* Search for all Teams in a sport by country - (returns a list of team objects)
```python
teams = api.Search().Teams(sport="Soccer",country="England")
```

* Search for all players from a team - (returns a list of player objects)
```python
players = api.Search().Players(team="Arsenal")
```

* Search for players by name - (returns a list of player objects)
```python
players = api.Search().Players(player="Danny Welbeck")
```

* Search for players by team and name - (returns a list of player objects)
```python
players = api.Search().Players(team="Arsenal",player="Danny Welbeck")
```

* Search for events by event name - (returns a list of event objects)
```python
events = api.Search().Events(event="Arsenal vs Chelsea")
```

* Search for events by filename - (returns a list of event objects)
```python
events = api.Search().Events(filename="English_Premier_League_2015-04-26_Arsenal_vs_Chelsea")
```

* Search for event by event name and season - (returns a list of event objects)
```python
events = api.Search().Events(event="Arsenal vs Chelsea",season=1415)
```

* Search for all Leagues in a country - (returns a list of league objects)
```python
leagues = api.Search().Leagues(country="England")
```

* Search for all Leagues by sport - (returns a list of league objects)
```python
leagues = api.Search().Leagues(sport="Soccer")
```

* Search for all Leagues in a country and by sport - (returns a list of league objects)
```python
leagues = api.Search().Leagues(country="England",sport="Soccer")
```

* Search for all Seasons in a League provided the league id - (returns a list of strings each one identifying a season)
```python
seasons = api.Search().Seasons(leagueid=4328)
```

* Search for all the user loved items - (returns single user object. Properties (Players,Events,Teams) are lists of id's - faster/need further lookup)
```python
loves = api.Search().Loves(user="zag")
```

* Search for all the user loved items - (returns single user object. Properties (Players,Events,Teams) are lists of objects - slower/returns the object itself)
```python
loves = api.Search().Loves(user="zag",objects=True)
```

A more detailed example using user loves:
```python
import thesportsdb
api = thesportsdb.Api("1")
userloves = api.Search().Loves(user="zag")
print(userloves.Teams, userloves.Players, userloves.Events)
>> [u'133632', u'133597',....

userloves = api.Search().Loves(user="zag",objects=True)
print(userloves.Teams, userloves.Players, userloves.Events)
>> [<thesportsdb.team.Team instance at 0x129d4d200>, <thesportsdb.team.Team instance at 0x11e1ba5f0>,....
```

####Lookups
* Provides League Details given the leagueid (returns a list of league objects)
```python
leagues = api.Lookups().League(leagueid=4346)
```

* League seasons by leagueid (returns a list of seasonid strings)
```python
seasons = api.Lookups().Seasons(leagueid=4346)
```
* Provides Team Details given the teamid (returns a list of team objects)
```python
teams = api.Lookups().Team(teamid=133604)
```

* All teams in a league provided the leagueid (returns a list of team objects)
```python
teams = api.Lookups().Team(leagueid=4346)
```

* Provides Player Details given the playerid (returns a list of player objects)
```python
players = api.Lookups().Player(playerid=34145937)
```

* All players in a team by teamid (returns a list of player objects)
```python
players = api.Lookups().Player(teamid=133604)
```

* Provides Event Details given the eventid (returns a list of event objects)
```python
events = api.Lookups().Event(eventid=441613)
```

* Lookup Table by League ID and Season (returns a list of tableentry objects without team objects)
```python
table = api.Lookups().Table(leagueid=4346)
```

* Lookup Table by League ID and Season (returns a list of tableentry objects each one containing a team object as Team property)
```python
table = api.Lookups().Table(leagueid=4346,objects=True)
```

A more detailed example using League Tables:
```python
import thesportsdb
api = thesportsdb.Api("1")
table = api.Lookups().Table(leagueid=4346)
if table:
	print(table[0].name,table[0].Team)

>> FC Dallas
>>

table = api.Lookups().Table(leagueid=4346,objects=True)
if table:
	print(table[0].name,table[0].Team, table[0].Team.strTeamBadge)

>> FC Dallas
>> <thesportsdb.team.Team instance at 0x12768ab80>
>> http://www.thesportsdb.com/images/media/team/badge/xvrwus1420778297.png
```


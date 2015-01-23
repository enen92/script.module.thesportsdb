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
print thesportsdb.Search().searchteams(TeamName="arsenal")
```
Every function returns a python dictionary.

###Query methods

####Search
Search team by name
```python
thesportsdb.Search().searchteams(TeamName="arsenal")
```

Search player by name
```python
thesportsdb.Search().searchplayers(PlayerName="messi")
```

Search player by name in team
```python
thesportsdb.Search().searchplayers(PlayerName="messi",TeamName="barcelona")
```

Search event by name
```python
thesportsdb.Search().searchevents(Event="arsenal%20chelsea")
```

Search event by name and season
```python
thesportsdb.Search().searchevents(Event="arsenal%20chelsea",Season="1415")
```

Search leagues by sport
```python
thesportsdb.Search().search_all_leagues(SportName="soccer")
```

Search leagues by sport and country
```python
thesportsdb.Search().search_all_leagues(SportName="soccer",CountryName="england")
```

Search leagues by league name
```python
thesportsdb.Search().search_all_leagues(LeagueName="English%20Premier%20League")
```

####Lookups

Lookup league by league id
```python
thesportsdb.Lookups().lookupleague(LeagueId=4346)
```

Lookup team by team id
```python
thesportsdb.Lookups().lookupteam(TeamId=133604)
```

Lookup player by player id
```python
thesportsdb.Lookups().lookupteam(PlayerId=34145937)
```

Lookup event by event id
```python
thesportsdb.Lookups().lookupevent(EventId=441613)
```

####Schedules

Returns the next 5 events for a specific teamID
```python
thesportsdb.Schedules().eventsnext(TeamId=133604)
```

Returns the last 5 events for a specific teamID
```python
thesportsdb.Schedules().eventslast(TeamId=133604)
```

Returns next events for a League
```python
thesportsdb.Schedules().eventsnextleague(LeagueId=4346)
```

####LiveScores

Returns next events for a League
```python
thesportsdb.LiveScores().latestsoccer()
```

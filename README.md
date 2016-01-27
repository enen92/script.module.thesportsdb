# script.module.thesportsdb
![TheSportsDb Icon](http://s17.postimg.org/h3eanic3z/icon.png)

A python module packaged as a Kodi script module to wrap all thesportsdb API methods for you to use on your own addon

*Work/documentation in progress.....

##Usage

###Addon.xml
The module most be imported in the addon.xml of your addon and pointing to the correct version of the module
```xml
<import addon="script.module.thesportsdb" version="1.0.0"/>
```

###Pythonic usage

The module follows the api structure described here [Here](http://www.thesportsdb.com/forum/viewtopic.php?f=6&t=5). Every group method (Search,Lookups,Schedules,Livescores) is a Python class and all the endpoints (eg: lookupleague) is part of a class method. The module maps the json data to objects as much as possible, so each call returns one or more Team objects, League objects, Player objects, Livescores objects, Table objects, etc.

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

*Search for all teams in a League - (returns a list of team objects)
```python
teams = api.Search().Teams(league="English Premier League")
```

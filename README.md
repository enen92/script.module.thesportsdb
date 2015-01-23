# script.module.thesportsdb
![TheSportsDb Icon](http://s11.postimg.org/5cq70m2j7/icon.png)

A python module packaged for Kodi to wrap the main thesportsdb API methods.

[b]Work in progress. 
At the moment, only the queries are implemented without any further parsing of the obtained results[/b]

##Usage

###Addon.xml
The module most be imported in the addon.xml of your addon
```xml
<import addon="script.module.thesportsdb"/>
```

###Pythonic usage

The module follows the api structure mentioned [Here](http://www.thesportsdb.com/forum/viewtopic.php?f=6&t=5)
Every group method (Search,Lookups,Schedules,Livescores) is a python class; every method (e.g lookupleague) is a function of the respective group. See example below:

```python
import thesportsdb
print thesportsdb.Search().searchteams("arsenal")
```
Every function returns a python dictionary.

####List of functions
* Search *


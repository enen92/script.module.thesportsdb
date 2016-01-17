__author__ = 'miguelborgesdefreitas'

class Tableentry:
    def __init__(self):
        self.name = ""
        self.teamid = ""
        self.played = ""
        self.goalsfor = ""
        self.goalsagainst = ""
        self.goaldifference = ""
        self.win = ""
        self.draw = ""
        self.loss = ""
        self.total = ""

    def setTeamObject(self,obj):
        print "set team object"
        self.Team = obj


def as_tableentry(d):
    t = Tableentry()
    t.__dict__.update(d)
    return t
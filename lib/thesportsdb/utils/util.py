
def CheckDateString(datestring):
	datelist = datestring.split("-")
	if len(datelist) == 3:
		if len(datelist[0]) == 4:
			if len(datelist[1]) >= 1 and len(datelist[1]) <= 2:
				if len(datelist[2]) >= 1 and len(datelist[2]) <= 2:
					return True
			else: return False
		else:
			return False
	else:
		return False

def CheckDateTime(datetimedate):
	if "datetime.date" in type(datetimedate): return True
	else: return False

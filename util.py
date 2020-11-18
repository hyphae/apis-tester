
def toValue(func, val):
	if val is None or val == '' or val == 'None':
		return None
	try:
		return func(val)
	except ValueError as e:
		return None

def toString(val):
	return '' if val is None else str(val)

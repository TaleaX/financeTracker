import datetime

current_date = datetime.date.today()

def get_weekday():
	return current_date.strftime("%A").lower()

def get_day():
	return current_date.strftime("%d")

def get_month():
	return current_date.strftime("%m")

def get_year():
	return current_date.strftime("%Y")

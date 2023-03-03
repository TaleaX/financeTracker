from date import get_day, get_month, get_weekday, get_year
import os.path
from templates.day import day_temp
from templates.month import month_temp
from utils import save, load
from vars import paths
import sys




def init_month(month_path):
	month_temp["year"] = get_year()
	month_temp["month"] = get_month()
	save(month_temp,month_path, 0)

def new_day(month_path):
	if not os.path.isfile(month_path):
		init_month(month_path)
	json_data = load(month_path)
	day_temp["weekday"] = get_weekday()
	day_temp["date"] = get_day()
	json_data["days"].append(day_temp)
	save(json_data, month_path, 0)


if __name__ == "__main__":
	person = sys.argv[1]
	print(person)
	new_day(paths[person + "_m"])
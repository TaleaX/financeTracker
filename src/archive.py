from date import get_day, get_month, get_weekday, get_year
import os.path
from templates.day import day_temp
from templates.month import month_temp
from templates.archive import archive_temp
from utils import save, load
from vars import paths
from new_day import init_month
import sys



def init_archive (archive_path):
	archive_temp["years"][0]["year"] = get_year()
	save(archive_temp, archive_path, 0)

def archive(archive_path, month_path):
	if not os.path.isfile(archive_path):
		init_archive()
	archive_data = load(archive_path)
	if not os.path.isfile(month_path):
		init_month()
	month_data = load(month_path)
	archive_data["years"][0]["months"].append(month_data)
	save(archive_data, archive_path, 0)


if __name__ == "__main__":
	person = sys.argv[1]
	if (person + "_a") in paths.keys():
		archive(person + "_a", person + "_m")
	else:
		print("Person doesnt exist")
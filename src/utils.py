import json
import os.path
from date import get_day
from vars import categories_abbr, work_abbr, life_abbr, child_abbr

def get_input(inp_str):
	return (input(inp_str).lower().replace(" ", ""))

def load(path):
	try:
		if (os.path.isfile(path)):
			with (open(path, "r")) as file:
				data = json.load(file)
				file.close()
			return (data)
		else:
			print("File doesn't exists")
			return False
	except Exception as e:
		print("Could load the path because", e)
		return False

def save(py_data, path, seek):
	try :
		with open(path ,"w") as file:
			file.seek(seek)
			json.dump(py_data, file, indent=4)
			file.close()
		return True
	except Exception as e:
		print("An Exception occured, while trying to save the data!")
		print(e)
		return False

def get_index(date, path):
	json_data = load(path)
	if not json_data:
		print("no entries for", path)
	else:
		counter = 0
		for day in json_data["days"]:
			if day["date"] == date:
				return (counter)
			counter += 1
	return (-1)
		
def	get_day_obj(path, json_data):
	date = get_input("Choose a day?\n> ")
	if date == "":
		date = get_day()
	index = get_index(date, path)
	if index == -1:
		print("Day doesn't exist")
		return False
	return json_data["days"][index]

def abbr_to_category(abbr, dict):
	return dict[abbr]

def get_category(categories_obj):
	category = get_input("Choose category:\n> ")

	if category in categories_abbr.keys():
		category = abbr_to_category(category, categories_abbr)
	if category in categories_obj.keys():
		return category
	print("Category doesn't exist sorry!")
	return False


def	get_child_category(category_obj, category):
	child_category = get_input(f"Choose {category} category:\n> ")

	if child_category in child_abbr[category].keys():
		child_category = abbr_to_category(child_category, child_abbr[category])
	if child_category in category_obj.keys():
		return child_category
	print("Child Category doesn't exist sorry!")
	return False
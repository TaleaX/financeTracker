from utils import load, get_input, get_index, get_day_obj, get_category, save, get_child_category
from vars import view_dict, view_ops, month_path, day_path
from my_math import add_amount, sub_amount, change_amount
import json

command_dict = {
	"add" : add_amount,
	"sub" : sub_amount,
	"change" : change_amount
}
	
def view():
	inp = get_input("What do u wanna view <day> <month> <archive>?\n> ")
	if inp in view_ops:
		json_data = load(view_dict[inp])
	if not json_data:
		print("Ups there are no", inp, "entries yet")
	else:
		print(json.dumps(json_data, indent=4))

def mod():
	json_data = load(month_path)
	if not json_data:
		print("Ups there are no monthly entries yet")
		return False
	day_obj = get_day_obj(month_path, json_data)
	if not day_obj:
		return False
	category = get_category(day_obj["categories"])
	child_category = False
	if not category:
		return False
	if category == "lifestyle" or category == "work":
		child_category = get_child_category(day_obj["categories"][category], category)
	cmd = input("What do u wanna do <add> <sub> <change>?\n> ")
	if cmd not in command_dict.keys():
		return False
	day_obj = command_dict[cmd](category, day_obj, child_category)
	if not day_obj:
		return False
	save(json_data, month_path, 0)
	save(json_data, day_path, 0)

def help():
	print("help")

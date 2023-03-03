from utils import get_input
from vars import operatores

def get_amount(inp):
	amount = 0.0
	numbers = inp.split("+")
	for number in numbers:
		# amount = operatores[operator](amount, float(number))
		amount +=  float(number)
	return amount


def check_Input(func):
	def wrapper(*args):
		try :
			category_tmp = args[0]
			if args[4]:
				category_tmp = args[4]
			inp_amount = get_input(f"{args[3]} {category_tmp} ?\n> ")
			amount = get_amount(inp_amount)
			return func(args[0], args[1], amount, args[3], args[4])
		except Exception as e:
			print("an errror occured", e)
	return wrapper

@check_Input
def add_amount(category, day_obj, amount_to_add, inp_str, child_category = False):
	if not child_category:
		day_obj["categories"][category] += amount_to_add
	else:
		day_obj["categories"][category][child_category] += amount_to_add
	return day_obj

@check_Input
def sub_amount(category, day_obj, amount_to_sub, inp_str, child_category = False):
	if not child_category:
		day_obj["categories"][category] -= amount_to_sub
	else:
		day_obj["categories"][category][child_category] -= amount_to_sub
	return day_obj

@check_Input
def change_amount(category, day_obj, new_amount, inp_str, child_category = False):
	if not child_category:
		day_obj["categories"][category] = new_amount
	else:
		day_obj["categories"][category][child_category] = new_amount
	return day_obj
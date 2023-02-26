from utils import get_input

def add_amount(category, day_obj, child_category = False):
	try :
		category_tmp = category
		if child_category:
			category_tmp = child_category
		amount_to_add = float(get_input(f"How much do u wanna add to {category_tmp}?\n> "))
	except Exception as e:
		print("an errror occured", e)
		return False
	if not child_category:
		day_obj["categories"][category] += amount_to_add
	else:
		day_obj["categories"][category][child_category] += amount_to_add
	return day_obj
	

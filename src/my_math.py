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
	
def sub_amount(category, day_obj, child_category = False):
	try :
		category_tmp = category
		if child_category:
			category_tmp = child_category
		amount_to_sub = float(get_input(f"How much do u wanna substract from {category_tmp}?\n> "))
	except Exception as e:
		print("an errror occured", e)
		return False
	if not child_category:
		day_obj["categories"][category] -= amount_to_sub
	else:
		day_obj["categories"][category][child_category] -= amount_to_sub
	return day_obj

def change_amount(category, day_obj, child_category = False):
	try :
		category_tmp = category
		if child_category:
			category_tmp = child_category
		new_amount = float(get_input(f"What is your new amount for {category_tmp}?\n> "))
	except Exception as e:
		print("an errror occured", e)
		return False
	if not child_category:
		day_obj["categories"][category] = new_amount
	else:
		day_obj["categories"][category][child_category] = new_amount
	return day_obj
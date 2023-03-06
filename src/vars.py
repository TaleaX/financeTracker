import operator

day_path = "../data/day.json"
month_path = "../data/month.json"
archive_path = "../data/archive.json"
backup_path = "../data/backup.json"


# cmds = ("add", "view", "help", "exit")
start_ops = ("ja", "j", "yes", "y", "ye")
view_ops = ("day", "month", "archive")

view_dict = {
	"day" : day_path,
	"month" : month_path,
	"archive" : archive_path
}

life_abbr = {
	"b"  : "books",
	"f"  : "food_extern",
	"e"  : "events",
	"a"  : "abos",
	"te" : "tech_goods",
	"tr" : "travel",
	"o"  : "others",
	"to" : "total"
}

work_abbr = {
	"tr" : "travel",
	"g"  : "goods",
	"o"  : "others",
	"to" : "total"
}

categories_abbr = {
	"g"  : "groceries",
	"hou" : "household",
	"t"  : "toni",
	"he" : "health",
    "c"  : "cosmetics",
	"w"  : "work",
	"l"  : "lifestyle",
    "hob" : "hobbies",
	"i"  : "insurance",
	"o"  : "others",
	"to" : "total"
}

child_abbr = {
	"lifestyle" : life_abbr,
	"work" : work_abbr
}

inp_strings = {
    "add"   : "How much do wann add to",
    "sub"   : "How much do u wanna substract from",
    "change": "What is your new amount for"
}

paths = {
    "dennis_m" : "../data/dennis_month.json",
    "dennis_a" : "../data/dennis_archive.json",
    "talea_m" : "../data/talea_month.json",
    "talea_a" : "../data/talea_archive.json",
}

operatores = {
    "+" : operator.add,
    "-" : operator.sub,
}
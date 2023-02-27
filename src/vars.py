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
	"ho" : "household",
	"t" : "toni",
	"he" : "health",
	"w"  : "work",
	"l"  : "lifestyle",
	"i"  : "insurance",
	"o"  : "others",
	"to" : "total"
}

child_abbr = {
	"lifestyle" : life_abbr,
	"work" : work_abbr
}


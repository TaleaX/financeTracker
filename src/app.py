from vars import start_ops
from utils import get_input
from commands import view, help, mod

command_dict = {
	"mod" : mod,
	"view" : view,
	"help" : help,
	"exit" : exit
}

def app():
	while True:
		cmd = get_input("What do u wanna do <mod> <view> <help> <exit>?\n> ")
		if cmd in command_dict.keys():
			command_dict[cmd]()


if __name__ == "__main__":
	start = get_input("Do u wanna use the finance App?\n> ")
	if start in start_ops:
		print("yay")
		app()
	else:
		print("Menno :(")
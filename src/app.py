from vars import cmds, start_ops
from utils import get_input
from commands import add, view, help

command_dict = {
	"add" : add,
	"view" : view,
	"help" : help,
	"exit" : exit
}

def app():
	while True:
		cmd = get_input("What do u wanna do <add> <view> <help> <exit>?\n> ")
		if cmd in cmds:
			command_dict[cmd]()


if __name__ == "__main__":
	start = get_input("Do u wanna use the finance App?\n> ")
	if start in start_ops:
		print("yay")
		app()
	else:
		print("Menno :(")
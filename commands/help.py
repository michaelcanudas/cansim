from cli import list, utils
from sim import stream


def command():
    utils.clear()
    
    commands = list.ListDisplay("commands", [
        "receive",
        "  bytes: display bytes receieved",
        "  message: display bytes when message received", "",
        "send",
        "  bytes: send a stream of bytes",
        "  message: send a message", "",
        "help: displays this menu"
    ])

    list.render(commands)
    input()
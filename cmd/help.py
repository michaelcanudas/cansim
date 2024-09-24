from ui import components, utils


def display():
    utils.clear()

    components.put_head("commands")
    components.put_text("\n".join([
        "receive",
        "  bytes: display bytes receieved",
        "  message: display bytes when message received", "",
        "send",
        "  bytes: send a stream of bytes",
        "  message: send a message", "",
        "help: displays this menu"
    ]))
    
    utils.wait()
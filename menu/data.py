import cmd.help
import cmd.receive
import cmd.send


class Item:
    def __init__(self, name: str, route: str, action):
        self.name = name
        self.route = route
        self.action = action


items: list[Item] = [
    Item("receive", "", "/receive"),
    Item("send", "", "/send"),
    Item("help", "", cmd.help.display),
    Item("<exit>", "", None),

     # [TODO] displays message content of next received #
    Item("bytes", "/receive", cmd.receive.bytes),
    # [TODO] displays message content once specific message received #
    Item("message", "/receive", None),
    # [TODO] displays live stream of messages #
    Item("live", "/receive", None),
    Item("<back>", "/receive", ""),

    # send bytes #
    Item("bytes", "/send", cmd.send.bytes),
    # send premade message #
    Item("message", "/send", "/send/message"),
    # [TODO] continue sending the same message #
    Item("loop", "/send", None),
    Item("<back>", "/send", ""),

    Item("test", "/send/message", cmd.send.test),
    Item("<back>", "/send/message", "/send"),
]
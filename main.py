from cli import select, utils
from commands import help
from commands.receive import receive_bytes
from commands.send import send_bytes, send_message
from sim import messages


def main():
    while menu():
        pass


def menu():
    return display_menu("can simulator", [
        ("receive", submenu_receive),
        ("send", submenu_send),
        ("help", help.command),
        ("<exit>", None)
    ])


def submenu_receive():
    display_menu("receive", [
        ("bytes", receive_bytes.command),
        ("message", None),
        ("<back>", None)
    ])


def submenu_send():
    display_menu("send", [
        ("bytes", send_bytes.command),
        ("message", submenu_send_message),
        ("<back>", None)
    ])


def submenu_send_message():
    display_menu("message", [
        ("pedal up", lambda: send_message.command(messages.pedal_up)),
        ("pedal down", lambda: send_message.command(messages.pedal_down)),
        ("<back>", None)
    ])


def display_menu(title, options):
    utils.clear()
    prompt = select.SelectPrompt(title, [
        select.SelectOption(text, action) for text, action in options
    ])
    
    select.render(prompt)
    action = select.receive(prompt)

    if action == None:
        return False
    
    action()
    return True


main()
import menu

def main():
    handler = menu.create("")
    if handler == None:
        return

    handler()


main()
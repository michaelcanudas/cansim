class ListDisplay:
    def __init__(self, heading: str, content: list[str]):
        self.heading = heading
        self.content = content
    

def render(display: ListDisplay):
    print(display.heading, end="\n\n")

    for i in range(0, len(display.content)):
        print("  * {}".format(display.content[i]))

    print()
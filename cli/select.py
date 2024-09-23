class SelectOption:
    def __init__(self, content: str, handler: callable):
        self.content = content
        self.handler = handler


class SelectPrompt:
    def __init__(self, content: str, options: list[SelectOption]):
        self.content = content
        self.options = options
    

def render(prompt: SelectPrompt):
    print(prompt.content, end="\n\n")

    for i in range(0, len(prompt.options)):
        print("  ({}) {}".format(i + 1, prompt.options[i].content))

    print()


def receive(prompt: SelectPrompt):
    print("response (number):", end=" ")
    response = input()

    if (not response.isdigit()) or (not int(response) in range(1, len(prompt.options) + 1)):
        return None
    
    return prompt.options[int(response) - 1].handler
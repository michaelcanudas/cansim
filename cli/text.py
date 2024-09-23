class TextPrompt:
    def __init__(self, content: str, tip: str):
        self.content = content
        self.tip = tip
    

def render(prompt: TextPrompt):
    print(prompt.content, end="\n\n")


def receive(prompt: TextPrompt):
    print("{}:".format(prompt.tip), end=" ")
    return input()
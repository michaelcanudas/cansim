from cli import text, utils
from sim import stream


def command():
    prompts = [
        text.TextPrompt("what device id (number)?", "Id"),
        text.TextPrompt("what content (hex)?", "Content")
    ]

    utils.clear()
    text.render(prompts[0])
    id = text.receive(prompts[0])

    utils.clear()
    text.render(prompts[1])
    data = bytes.fromhex(text.receive(prompts[1]))

    device = stream.start()
    frame = stream.Frame(id, data)

    stream.send(device, frame)
    stream.stop(device)
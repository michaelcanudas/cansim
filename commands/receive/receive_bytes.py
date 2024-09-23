from cli import text, utils
from sim import stream


def command():
    device = stream.start()
    frame = stream.receive(device)

    stream.stop(device)

    print("message from {} with message:".format(frame.id))
    print(frame.data)
    
    input()
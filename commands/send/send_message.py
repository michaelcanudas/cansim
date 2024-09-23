from sim import stream


def command(message: stream.Frame):
    device = stream.start()

    stream.send(device, message)
    stream.stop(device)
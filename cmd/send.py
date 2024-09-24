import sim
from ui import components, utils


def bytes():
    utils.clear()

    components.put_head("receive bytes")

    id = components.get_text("device id (number)")
    data = components.get_text("data (hex)")
    
    send(sim.Frame(int(id), bytes.fromhex(data)))


def test():
    send(sim.Frame(1, b"\x00\x01\x00"))


def send(message: sim.Frame):
    device = sim.start()

    sim.send(device, message)
    sim.stop(device)
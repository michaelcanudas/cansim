import sim
from ui import components, utils

def bytes():
    utils.clear()

    components.put_head("bytes")
    components.put_text(receive().data)

    utils.wait()


def receive() -> sim.Frame:
    device = sim.start()
    frame = sim.receive(device)

    sim.stop(device)
    return frame
from sim.stream import Frame


def pedal_up() -> Frame:
    return Frame(000, b"\x00\x00\x00")


def pedal_down() -> Frame:
    return Frame(000, b"\x00\x00\x00")
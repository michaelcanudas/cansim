from gs_usb.gs_usb import GsUsb
from gs_usb.gs_usb_frame import GsUsbFrame


class Device:
    def __init__(self, interface: GsUsb):
        self.interface = interface


class Frame:
    def __init__(self, id: int, data: str):
        self.id = id
        self.data = data


def start() -> Device:
    devices = GsUsb.scan()
    if len(devices) == 0:
        return None
    
    device = Device(devices[0])

    device.interface.set_bitrate(250_000)
    device.interface.start()
    
    return device


def send(device: Device, frame: Frame):
    data = GsUsbFrame(frame.id, frame.data)
    device.interface.send(data)


def receive(device: Device) -> Frame:
    data = GsUsbFrame()
    while not device.interface.read(data, 1):
        pass

    return Frame(data.can_id, data.data)


def stop(device: Device):
    device.interface.stop()
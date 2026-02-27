import cec

class TVController:
    def __init__(self):
        self.lib = cec.ICECAdapter.Create(cec.libcec_configuration())
        self.lib.Open("RPI")  # nome simbólico

    def power_on(self):
        self.lib.PowerOnDevices(cec.CECDEVICE_TV)

    def standby(self):
        self.lib.StandbyDevices(cec.CECDEVICE_TV)

    def set_active_source(self):
        self.lib.SetActiveSource()

    def volume_up(self):
        self.lib.VolumeUp()

    def volume_down(self):
        self.lib.VolumeDown()
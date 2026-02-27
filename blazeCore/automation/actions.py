from automation.cec_control import TVController
import webbrowser

tv = TVController()

def execute(intent):

    if intent["intent"] == "open_youtube":
        tv.power_on()
        tv.set_active_source()
        webbrowser.open("https://youtube.com")

    if intent["intent"] == "tv_off":
        tv.standby()

    if intent["intent"] == "volume_up":
        tv.volume_up()

    if intent["intent"] == "volume_down":
        tv.volume_down()
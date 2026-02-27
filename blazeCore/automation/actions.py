import webbrowser
from printer.bambu_monitor import get_printer_status

def execute(intent):
    if intent["intent"] == "open_youtube":
        webbrowser.open("https://youtube.com")

    if intent["intent"] == "printer_status":
        return get_printer_status()
from wake.wake_word import WakeWordDetector
from speech.stt import listen_command
from ai.ai_engine import ask_ai
from commands.parser import parse_command
from automation.actions import execute

detector = WakeWordDetector("shiro.ppn")

while True:
    if detector.listen():
        print("Wake detected")
        command = listen_command()
        intent = parse_command(command)

        if intent["intent"] == "ai_only":
            response = ask_ai(command)
            print(response)
        else:
            result = execute(intent)
            print(result)
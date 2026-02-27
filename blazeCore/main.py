from wake.wake_word import WakeWordDetector
from speech.stt import listen_command
from ai.ai_engine import ask_ai
from commands.parser import parse_command
from automation.actions import execute

detector = WakeWordDetector("shiro.ppn")

print("Jarvis (Gemini) ativo e ouvindo...")

while True:
    if detector.listen():
        print("Wake detected")
        command = listen_command()
        
        if command:
            intent = parse_command(command)

            if intent["intent"] == "ai_only":
                response = ask_ai(command)
                print(f"Jarvis: {response}")
            else:
                result = execute(intent)
                print(result)

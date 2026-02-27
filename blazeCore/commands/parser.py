def parse_command(text):
    text = text.lower()

    if "youtube" in text:
        return {"intent": "open_youtube"}

    if "impressão" in text:
        return {"intent": "printer_status"}

    return {"intent": "ai_only"}
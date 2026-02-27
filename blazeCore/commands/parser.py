def parse_command(text):
    text = text.lower()

    if "youtube" in text:
        return {"intent": "open_youtube"}

    if "desligar tv" in text:
        return {"intent": "tv_off"}

    if "aumentar volume" in text:
        return {"intent": "volume_up"}

    if "diminuir volume" in text:
        return {"intent": "volume_down"}

    if "impressão" in text:
        return {"intent": "printer_status"}

    return {"intent": "ai_only"}
def get_full_name(first, last, middle=""):
    if middle:
        return f"{first.title()} {middle.title()} {last.title()}"
    
    return f"{first.title()} {last.title()}"
def build_profile(first, last, **info):
    info["first"] = first.title()
    info["last"] = last.title()
    return info

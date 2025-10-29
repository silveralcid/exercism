def label(colors):
    color_dict = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6, "violet": 7,
        "grey": 8, "white": 9
    }

    base_value = int(f"{color_dict[colors[0]]}{color_dict[colors[1]]}")
    multiplier = 10 ** color_dict[colors[2]]
    raw = base_value * multiplier

    if raw < 1_000:
        return f"{raw} ohms"
    elif raw < 1_000_000:
        return f"{raw / 1_000:g} kiloohms"
    elif raw < 1_000_000_000:
        return f"{raw / 1_000_000:g} megaohms"
    else:
        return f"{raw / 1_000_000_000:g} gigaohms"

def resistor_label(colors):
    digit = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6, "violet": 7,
        "grey": 8, "white": 9
    }

    exponent = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6, "violet": 7,
        "grey": 8, "white": 9,
        "gold": -1, "silver": -2
    }

    tolerance = {
        "brown": "±1%", "red": "±2%", "green": "±0.5%",
        "blue": "±0.25%", "violet": "±0.1%", "grey": "±0.05%",
        "gold": "±5%", "silver": "±10%", "black": ""
    }

    n = len(colors)
    if n == 1:
        return "0 ohms"
    if n not in (4, 5):
        raise ValueError("Provide 1, 4, or 5 color bands.")

    sig_len = 2 if n == 4 else 3  # 4-band: 2 digits, 5-band: 3 digits
    sig = int("".join(str(digit[c]) for c in colors[:sig_len]))

    mult_color = colors[sig_len]
    tol_color = colors[-1]

    raw = sig * (10 ** exponent[mult_color])

    value = float(raw)
    unit = "ohms"
    if abs(value) >= 1_000_000_000:
        value /= 1_000_000_000
        unit = "gigaohms"
    elif abs(value) >= 1_000_000:
        value /= 1_000_000
        unit = "megaohms"
    elif abs(value) >= 1_000:
        value /= 1_000
        unit = "kiloohms"

    label = f"{value:g} {unit}"
    tol = tolerance.get(tol_color, "")
    return f"{label} {tol}".strip()

def mid(x, y, z):
    m = z
    if y < z:
        if x < y:
            m = y
        elif x < z:
            m = y       # 1st bug: here should be m = x
    elif x > y:
        m = x           # 2rd bug: her should be m = y
    elif x > z:
        m = x
    return m

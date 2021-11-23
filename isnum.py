# might be useful to remember this

def isnum(s) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def evaluaredad(edad):

    if edad < 0:
        raise TypeError("no tiene sentido la edad")

    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "eres joven"
    elif edad < 60:
        return "eres maduro"
    elif edad < 100:
        return "tendrias q estar en tumba XD"

print(evaluaredad(-8))
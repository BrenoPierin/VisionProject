import psutil


# Memoria RAM
def RamTotal():
    return round(psutil.virtual_memory().total/(1024**3), 1)

# Memoria RAM Livre


def RamLivre():
    return round(psutil.virtual_memory().free/(1024**3), 1)

# Memoria Usada


def RamUsada():
    return round(psutil.virtual_memory().used/(1024**3), 1)

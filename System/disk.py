import psutil


# Discos conectados
def DiscosConectados():
    return psutil.disk_partitions()

# Memoria total no disco


def Memoria():
    return round(psutil.disk_usage('/').total/(1024**3), 1)

# Memoria disponiveis no disco


def MemoriaDisponivel():
    return round(psutil.disk_usage('/').free/(1024**3), 1)

# Memoria usada no disco


def MemoriaUsada():
    return round(psutil.disk_usage('/').used/(1024**3), 1)

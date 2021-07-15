import psutil


# Frequencia do processador


def Frequencia():
    return round(psutil.cpu_freq().current/1000, 1)


# Quantidade de nucleos do processador


def Cores():
    return psutil.cpu_count()

# Nucleos fisicos do processador


def CoresFisicos():
    return psutil.cpu_count(logical=False)

# Percentual do uso do processador


def PercentualProcessador():
    return psutil.cpu_percent(interval=0.1)

# Percentual livre processador


def PercentualLivreProcessador():
    return psutil.cpu_times_percent(interval=0.1).idle

import psutil


# Bytes enviados
def BytesEnviados():
    return round(psutil.net_io_counters().bytes_sent/(1024**3), 1)

# Bytes recebidos
def BytesRecebidos():
    return round(psutil.net_io_counters().bytes_recv/(1024**3), 1)

# Status da rede
def Status():
    rede = psutil.net_if_stats()
    return rede['Wi-Fi'].speed
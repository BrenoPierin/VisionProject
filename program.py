import time
import sched
import smtplib
from email.message import EmailMessage
import os


from dotenv import load_dotenv


from System import cpu
from System import memory
from System import disk
from System import network


# Carrega as informações do .env
load_dotenv()

def send_email():
    # Define email de origem e destino
    email_from = 'brenomax02@gmail.com'
    email_to = 'gustavo.mainchein@darede.com.br'

    # Define tipo do email
    msg = EmailMessage()

    # Define mensagem do email
    message = f"""
    Informações sobre o processador:
    Frequencia: {cpu.Frequencia()}GHz
    Núcleos: {cpu.Cores()}
    Núcleos Físicos: {cpu.CoresFisicos()}
    Percentual de Uso: {cpu.PercentualProcessador()}%
    Percentual Livre: {cpu.PercentualLivreProcessador()}%
    ================================================================

    Informaçõs sobre Memoria RAM:
    Total: {memory.RamTotal()}GB
    Livre: {memory.RamLivre()}GB
    Usada: {memory.RamUsada()}GB
    ================================================================

    Informações sobre Disco:
    Discos conectados: {disk.DiscosConectados()}
    Memoria Total : {disk.Memoria()}GB
    Memoria Disponivel : {disk.MemoriaDisponivel()}GB
    Memoria Usada : {disk.MemoriaUsada()}GB
    ================================================================

    Informações sobre a Rede:
    Bytes Enviados: {network.BytesEnviados()}GB
    Bytes Recebidos: {network.BytesRecebidos()}GB
    Velocidade : {network.Status()}MBps
    """

    msg.set_content(message)
    # Define o assunto do email

    # Senha do email de origem
    password = os.getenv('EMAIL_PASSWORD')

    # Origem do email
    msg['From'] = email_from
    # Destino do email
    msg['To'] = email_to
    # Assunto do email
    msg['Subject'] = 'Dados do Computador'

    # Define o servidor de onde será enviado o email
    server = smtplib.SMTP('smtp.gmail.com: 587')
    # Inicia o servidor
    server.starttls()

    # Faz o login no email de origem
    server.login(email_from, password)

    # Envia o email
    server.sendmail(email_from, email_to, msg.as_string())
    server.quit()

s = sched.scheduler(time.time, time.sleep)


def Agendador(sc):
    send_email()
    s.enter(3600, 1, Agendador, (sc,))


s.enter(3600, 1, Agendador, (s,))

s.run()

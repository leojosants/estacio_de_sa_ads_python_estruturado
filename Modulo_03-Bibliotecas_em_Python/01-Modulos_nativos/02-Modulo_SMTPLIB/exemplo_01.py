# import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

""" Criação da mensagem com o corpo e seus parâmetros:   """
# criação de um objeto de mensagem
msg = MIMEMultipart()

# Exibe o corpo da mensagem em uma string.
texto = "Estou enviando um email com Python"

# parâmetros
senha = "l1j1o1s1google"
msg['From'] = "leonardojosantos@gmail.com"
msg['To'] = "leojoosantss@gmail.com"
msg['Subject'] = "Teste de envio de email por Python"

# criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

""" Passos necessários para o próprio envio: """
# criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

# Login na conta para envio
server.login(msg['From'], senha)

# envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

# encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')

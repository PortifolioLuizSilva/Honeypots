import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import re

LOG_FILE = "/caminho/para/var/log/cowrie/cowrie.log"
EMAIL_FROM = "seu_email@gmail.com"
EMAIL_TO = "destinatario_email@gmail.com"
EMAIL_SUBJECT = "Alerta de Honeypot: Interação detectada"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "seu_email@gmail.com"
EMAIL_PASSWORD = "sua_senha"

def send_email(log_content):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = EMAIL_SUBJECT

    body = f"""
    Alerta: Interação com o Honeypot detectada.
    
    Detalhes do ataque:
    
    {log_content}
    """
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_FROM, EMAIL_TO, text)
    server.quit()

def extract_attack_details(line):
    # Extraindo detalhes do log
    details = ""
    ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
    if ip_match:
        ip = ip_match.group(1)
        details += f"IP do atacante: {ip}\n"
    
    date_match = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})', line)
    if date_match:
        date = date_match.group(1)
        details += f"Data e Hora: {date}\n"

    login_match = re.search(r'login attempt ([\w\W]+?)', line)
    if login_match:
        login_info = login_match.group(1)
        details += f"Tentativa de login: {login_info}\n"

    command_match = re.search(r'Command found: ([\w\W]+?)$', line)
    if command_match:
        command = command_match.group(1)
        details += f"Comando executado: {command}\n"
    
    return details

def monitor_logs():
    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)  # Move o cursor do arquivo para o final
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  # Espera 1 segundo antes de verificar novamente
                continue
            # Analisando o log com regex para capturar detalhes específicos
            if "login attempt" in line or "Command found" in line:
                attack_details = extract_attack_details(line)
                send_email(attack_details)

if __name__ == "__main__":
    monitor_logs()

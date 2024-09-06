# Instalação e Configuração do Cowrie no WSL

Este guia descreve como instalar o Cowrie no Windows Subsystem for Linux (WSL) e configurar o envio de alertas por e-mail.

## 1. Instalar WSL (Windows Subsystem for Linux)

Para rodar o Cowrie no Windows, você precisará do WSL. Siga os passos abaixo para instalá-lo:

1. Abra o PowerShell como administrador e execute o seguinte comando para instalar o WSL:

   ```powershell
   wsl --install
   ```

2. Reinicie o computador.

3. Após reiniciar, instale uma distribuição Linux, como o Ubuntu, na Microsoft Store.

## 2. Instalar Cowrie no WSL

Depois de configurar o WSL com Ubuntu, siga os passos abaixo para instalar o Cowrie:

1. Atualize o sistema e instale as dependências necessárias:

   ```bash
   sudo apt update && sudo apt upgrade
   sudo apt install python3-pip python3-virtualenv git
   ```

2. Clone o repositório do Cowrie:

   ```bash
   git clone https://github.com/cowrie/cowrie.git
   cd cowrie
   ```

3. Crie e ative o ambiente virtual:

   ```bash
   python3 -m venv cowrie-env
   source cowrie-env/bin/activate
   ```

4. Instale as dependências do Cowrie:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure o Cowrie:

   ```bash
   cp etc/cowrie.cfg.dist etc/cowrie.cfg
   ```

   Abra o arquivo `cowrie.cfg` e ajuste as configurações conforme necessário.

6. Inicie o Cowrie:

   ```bash
   bin/cowrie start
   ```

Agora você tem o Cowrie rodando no Windows via WSL.

## 3. Monitorar e Configurar Alertas por E-mail

Para monitorar o log do Cowrie e enviar um e-mail quando houver uma interação maliciosa, siga os passos abaixo:

1. Instale o módulo `smtplib` para enviar e-mails:

   ```bash
   pip install smtplib
   ```

   (Nota: `smtplib` já está incluído na biblioteca padrão do Python. Se você encontrar problemas, pode ser necessário instalar outros módulos adicionais ou configurar o envio de e-mails de acordo com sua necessidade.)

agora inicie o monitoramento :

    python monitor.py

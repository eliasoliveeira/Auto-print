from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from whatsapp_api import WhatsApp
from PIL import Image
import os

# Define o caminho do driver do navegador
chrome_driver_path = "/caminho/do/driver/chromedriver"

# Define o caminho da pasta onde serão salvas as imagens
image_folder_path = "/caminho/da/pasta/das/imagens"

# Inicializa o serviço do navegador
service = Service(chrome_driver_path)
service.start()

# Configura as opções do navegador
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=Perfil")

# Inicializa o navegador
driver = webdriver.Chrome(service=service, options=options)

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Espera até que o usuário escaneie o QR Code
input("Escaneie o QR Code e pressione ENTER para continuar...")

# Inicializa a API do WhatsApp Web Automation
whatsapp = WhatsApp()

# Faz login na conta do WhatsApp Web
whatsapp.login()

# Define o nome do grupo que deseja imprimir as mensagens
grupo_desejado = "Nome do Grupo"

# Define uma função para imprimir as imagens
def print_image(image_path):
    image = Image.open(image_path)
    image.show()
    os.remove(image_path)

# Loop principal
while True:
    # Verifica se há novas mensagens
    new_messages = whatsapp.get_unread()

    # Processa as novas mensagens
    for message in new_messages:
        # Verifica se a mensagem é de um grupo específico
        if message.chat.name == grupo_desejado and message.type == "image":
            # Baixa a imagem
            image_path = os.path.join(image_folder_path, message.id + ".jpg")
            message.save_media(image_path)

            # Imprime a imagem
            print_image(image_path)

    # Espera 1 segundo antes de verificar novamente
    time.sleep(1)

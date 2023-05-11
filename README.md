# Script para imprimir imagens recebidas em um grupo do WhatsApp

Este é um script em Python que permite imprimir automaticamente todas as imagens enviadas em um grupo do WhatsApp. O script utiliza a API do WhatsApp Web Automation para ler as mensagens recebidas e a biblioteca Pillow para imprimir as imagens em uma impressora conectada ao notebook.

## Requisitos

Para executar este script, você precisará atender aos seguintes requisitos:

- Um computador com sistema operacional Windows, Mac ou Linux
- O Python 3.x instalado no computador
- Uma conta do WhatsApp com acesso ao WhatsApp Web
- Uma impressora conectada ao notebook

## Instalação

Para instalar as bibliotecas necessárias, abra o terminal do seu sistema operacional e digite os seguintes comandos:

´pip install selenium´
´pip install whatsapp_api´
´pip install Pillow´

## Utilização

Para usar o script, siga os passos abaixo:

1. Clone ou faça o download deste repositório para o seu computador.
2. Abra o arquivo `imprimir_imagens.py` em um editor de texto e edite as variáveis `chrome_driver_path` e `image_folder_path` com os caminhos corretos para o driver do navegador e para a pasta onde deseja salvar as imagens, respectivamente.
3. Abra o terminal do seu sistema operacional e navegue até o diretório onde o script está salvo.
4. Digite o seguinte comando para executar o script:

´python imprimir_imagens.py´

5. O script abrirá uma janela do navegador e solicitará que você escaneie o código QR para acessar o WhatsApp Web. Escaneie o código com o seu celular.
6. Após escanear o código, o script iniciará a leitura das mensagens recebidas. Todas as imagens recebidas no grupo especificado serão impressas automaticamente na impressora conectada ao notebook.

## Limitações

Este script foi testado com sucesso em sistemas operacionais Windows, Mac e Linux e com as versões mais recentes do Google Chrome e do Mozilla Firefox. No entanto, devido à natureza da API do WhatsApp Web Automation, é possível que o script pare de funcionar a qualquer momento, caso o WhatsApp faça alterações significativas na sua API.

## Conclusão

Esperamos que este script possa ajudá-lo a imprimir automaticamente as imagens recebidas em um grupo do WhatsApp. Se você tiver alguma dúvida ou encontrar algum problema durante a utilização do script, por favor, abra uma nova issue neste repositório e teremos prazer em ajudá-lo.
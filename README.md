# Conversor de Áudio para Texto

Este projeto é uma aplicação web simples que converte arquivos de áudio (MP3 ou WAV) em texto. Utiliza Flask como framework para a interface web e Pydub e SpeechRecognition para a conversão de áudio para texto.

## Funcionalidades

- **Upload de arquivos de áudio**: Suporta arquivos MP3 e WAV.
- **Conversão de áudio para texto**: Usando o Google Speech Recognition.
- **Reprodução de áudio**: O áudio convertido pode ser reproduzido diretamente na interface web.
- **Armazenamento de arquivos**: O áudio é salvo no formato WAV após a conversão de MP3 (se necessário) e fica disponível para reprodução.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o Python instalado em seu sistema. Além disso, será necessário instalar as dependências do projeto.

### Dependências

1. Flask
2. Pydub
3. SpeechRecognition


## Instalação

Para instalar as dependências do projeto, siga os passos abaixo:

1. Clone o repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/seu-usuario/audio-para-texto.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd audio-para-texto
    ```

3. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

4. Instale as dependências utilizando o `pip`:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute a aplicação:
    ```bash
    python app.py
    ```

A aplicação estará disponível em `http://127.0.0.1:5000/`.

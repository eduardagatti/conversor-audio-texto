from flask import Flask, render_template, request, send_from_directory
from pydub import AudioSegment
import speech_recognition as sr
import os

app = Flask(__name__)

# Diretório onde os arquivos de áudio serão salvos
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Função para converter o áudio para texto
def convert_audio_to_text(file_path):
    # Se for MP3, converte para WAV
    if file_path.endswith('.mp3'):
        audio = AudioSegment.from_mp3(file_path)
        wav_path = file_path.replace(".mp3", ".wav")
        audio.export(wav_path, format="wav")
    else:
        wav_path = file_path  # Se já for WAV, apenas retorna o mesmo caminho
    
    # Reconhecimento de fala
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='pt-BR')
            return text, wav_path  # Retorna o texto e o caminho do arquivo WAV
        except sr.UnknownValueError:
            return "Não foi possível reconhecer o áudio.", None
        except sr.RequestError as e:
            return f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}", None

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    audio_file = None
    if request.method == "POST":
        file = request.files["audio_file"]
        if file:
            # Salva o arquivo enviado na pasta uploads
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Converte o áudio para texto e armazena o caminho do arquivo convertido
            text, wav_path = convert_audio_to_text(file_path)
            
            # Armazena o caminho do arquivo de áudio convertido (se for MP3, terá sido convertido para WAV)
            audio_file = os.path.basename(wav_path)

            # Remove o arquivo original após o processamento, se for MP3
            if file.filename.endswith(".mp3"):
                os.remove(file_path)

    return render_template("index.html", text=text, audio_file=audio_file)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    try:
        # Identificar o tipo MIME com base na extensão do arquivo
        if filename.endswith(".wav"):
            mimetype = 'audio/wav'
        elif filename.endswith(".mp3"):
            mimetype = 'audio/mpeg'
        else:
            mimetype = 'application/octet-stream'

        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, mimetype=mimetype)
    except FileNotFoundError:
        return "Arquivo não encontrado!", 404


if __name__ == "__main__":
    app.run(debug=True)

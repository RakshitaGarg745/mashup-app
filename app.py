from flask import Flask, render_template, request
import os
import re
import zipfile
import yt_dlp
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from flask_mail import Mail, Message
port = int(os.environ.get("PORT", 10000))
os.makedirs("downloads", exist_ok=True)
os.makedirs("audios", exist_ok=True)
os.makedirs("trimmed", exist_ok=True)
os.makedirs("output", exist_ok=True)

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rakshitagarg52@gmail.com'
app.config['MAIL_PASSWORD'] = 'ukfn hnro xgwl hate'

mail = Mail(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer = request.form["singer"]
        count = int(request.form["count"])
        duration = int(request.form["duration"])
        email = request.form["email"]

        if count <= 10:
            return "Number of videos must be greater than 10"

        if duration <= 20:
            return "Duration must be greater than 20 seconds"

        # Download Videos
        ydl_opts = {
    'format': 'bestaudio[ext=m4a]/bestaudio/best',
    'outtmpl': 'downloads/%(id)s.%(ext)s',
    'quiet': False,
    'noplaylist': True,
    'max_filesize': 20_000_000,  # skip files larger than 20MB
    'match_filter': yt_dlp.utils.match_filter_func("duration < 600"),  # skip videos longer than 10 mins
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}




        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch{count}:{singer}"])

        # Convert to Audio
        video_files = os.listdir("downloads")

        for file in video_files:
            video_path = os.path.join("downloads", file)
            audio_path = os.path.join("audios", file.replace(".mp4", ".mp3"))

            

        # Trim
        audio_files = os.listdir("audios")

        for file in audio_files:
            audio_path = os.path.join("audios", file)
            trimmed_path = os.path.join("trimmed", file)

            sound = AudioSegment.from_mp3(audio_path)
            trimmed = sound[:duration * 1000]
            trimmed.export(trimmed_path, format="mp3")

        # Merge
        final = AudioSegment.empty()
        trimmed_files = os.listdir("trimmed")

        for file in trimmed_files:
            file_path = os.path.join("trimmed", file)
            sound = AudioSegment.from_mp3(file_path)
            final += sound

        final_path = "output/final.mp3"
        final.export(final_path, format="mp3")

        # Zip
        zip_path = "output/result.zip"
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(final_path)

        # Send Email
        msg = Message(
            "Your Mashup File",
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )

        msg.body = "Your mashup file is attached."

        with app.open_resource(zip_path) as fp:
            msg.attach("result.zip", "application/zip", fp.read())

        mail.send(msg)

        return "Mashup Created Successfully!"

    return render_template("index.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)



from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Route to serve video files directly from Videos folder
@app.route('/videos/<filename>')
def serve_video(filename):
    videos_dir = os.path.join(os.path.dirname(__file__), 'Videos')
    return send_from_directory(videos_dir, filename)

@app.route('/')
def home():
    return render_template('Main_Page.HTML')

@app.route('/files')
def files():
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm']
    videos_dir = os.path.join(os.path.dirname(__file__), 'Videos')
    files = []
    if os.path.exists(videos_dir):
        for file in os.listdir(videos_dir):
            if os.path.splitext(file)[1].lower() in video_extensions:
                files.append(file)
    return render_template('files.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)
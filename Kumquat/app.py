
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Main_Page.HTML')

@app.route('/files')
def files():
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm']
    videos_dir = os.path.join(os.getcwd(), 'Videos')
    files = []
    if os.path.exists(videos_dir):
        for f in os.listdir(videos_dir):
            file_path = os.path.join(videos_dir, f)
            # Only allow files directly in the Videos folder, not subfolders or symlinks
            if os.path.isfile(file_path) and os.path.dirname(file_path) == videos_dir and os.path.splitext(f)[1].lower() in video_extensions:
                files.append(f)
    return render_template('files.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)
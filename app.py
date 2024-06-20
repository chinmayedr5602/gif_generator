import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from scripts.create_gifs import create_gifs
from scripts.transcribe import transcribe_video
from scripts.segment import segment_video

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Process the video and create GIFs
        transcript, segments = transcribe_video(file_path)
        output_dir = 'static/gifs'
        os.makedirs(output_dir, exist_ok=True)

        segment_video(file_path, segments, app.config['UPLOAD_FOLDER'])
        create_gifs(segments, app.config['UPLOAD_FOLDER'], output_dir)

        gifs = [
            f"gifs/{gif}" for gif in os.listdir(output_dir) if gif.endswith('.gif')]
        return render_template('result.html', gifs=gifs)
    return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)

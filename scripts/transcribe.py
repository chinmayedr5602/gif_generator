import whisper


def transcribe_video(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    transcript = result["text"]
    segments = result["segments"]
    return transcript, segments

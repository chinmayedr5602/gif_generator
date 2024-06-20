import os
from scripts.transcribe import transcribe_video
from scripts.segment import segment_video
from scripts.create_gifs import create_gifs


def main():
    video_path = "video.mp4"
    output_dir = "output"
    segments_dir = os.path.join(output_dir, "segments")
    gifs_dir = os.path.join(output_dir, "gifs")

    os.makedirs(segments_dir, exist_ok=True)
    os.makedirs(gifs_dir, exist_ok=True)

    # Step 1: Transcribe the video
    transcript, segments = transcribe_video(video_path)

    # Step 2: Segment the video
    segment_video(video_path, segments, segments_dir)

    # Step 3: Create GIFs with captions
    create_gifs(segments, segments_dir, gifs_dir)


if __name__ == "__main__":
    main()

import os
import ffmpeg


def segment_video(video_path, segments, output_dir):
    for i, segment in enumerate(segments):
        start = segment["start"]
        end = segment["end"]
        output_path = os.path.join(output_dir, f"segment_{i}.mp4")
        ffmpeg.input(video_path, ss=start, to=end).output(output_path).run()

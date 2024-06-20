from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os


def create_gif_with_caption(video_path, text, output_path):
    # Ensure the path to ImageMagick is set correctly
    from moviepy.config import change_settings

    image_magick_path = "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"
    change_settings({"IMAGEMAGICK_BINARY": image_magick_path})

    try:
        # Create video clip
        clip = VideoFileClip(video_path)

        # Calculate optimal fontsize based on video width
        # Adjust divisor for larger or smaller fonts
        fontsize = int(clip.w / 20)

        # Define a maximum width for the text box, typically close to video width
        max_text_width = int(clip.w * 0.9)

        # Create text clip with a specified box width
        txt_clip = TextClip(text, fontsize=fontsize, color='white',
                            bg_color='black', method='caption', size=(max_text_width, None))

        # Position the text at the bottom of the video
        txt_clip = txt_clip.set_position(
            ('center', 'bottom')).set_duration(clip.duration)

        # Composite video clip with text clip
        video = CompositeVideoClip([clip, txt_clip])

        # Write to GIF
        video.write_gif(output_path, fps=clip.fps)
        print(f"GIF created successfully at {output_path}")

    except Exception as e:
        print(f"Error creating GIF: {e}")


def create_gifs(segments, segments_dir, gifs_dir):
    for i, segment in enumerate(segments):
        video_path = os.path.join(segments_dir, f"segment_{i}.mp4")
        text = segment["text"]
        output_path = os.path.join(gifs_dir, f"gif_{i}.gif")
        create_gif_with_caption(video_path, text, output_path)



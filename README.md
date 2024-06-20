# GIFFER: Your GIF Maker

GIFFER is a web application that allows users to upload a video file, transcribe it using Whisper, segment the video based on the transcription, and generate GIFs with captions. The GIFs are displayed in a responsive grid format for easy viewing.

## Features

- Upload a video file
- Automatic transcription using Whisper
- Video segmentation based on transcription
- Generate GIFs with captions
- Responsive UI for displaying GIFs

## Directory Structure

![image](https://github.com/chinmayedr5602/gif_generator/assets/77034548/c4e69281-469b-46ab-a274-f3e78a564655)


## Installation

1. **Unzip the gif_generator zipped folder**.

2. **Set up a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure ImageMagick and FFmpeg are installed**:

    - **ImageMagick**:
        - Download and install ImageMagick from [ImageMagick download page](https://imagemagick.org/script/download.php).
        - Set the ImageMagick binary path in `create_gifs.py`:
    
        ```python
        image_magick_path = "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"
        ```

    - **FFmpeg**:
        - Download FFmpeg manually from [FFmpeg download page](https://ffmpeg.org/download.html) and follow the installation instructions for your operating system.
        - Alternatively, you can install FFmpeg using `winget` on Windows:
        
        ```bash
        winget install ffmpeg
        ```

5. **Check if ImageMagick and FFmpeg are installed**:

    You can use the following commands to verify if both tools are installed correctly.

    - **ImageMagick**:

        ```bash
        magick -version
        ```

        If installed correctly, this command should output the version of ImageMagick installed.

    - **FFmpeg**:

        ```bash
        ffmpeg -version
        ```

        If installed correctly, this command should output the version of FFmpeg installed.

## Usage

1. **Run the Flask application**:

    ```bash
    python app.py
    ```

2. **Open a web browser and go to** `http://127.0.0.1:5000/`.

3. **Upload a video file** and wait for the processing to complete.

4. **View and download the generated GIFs**.

### Running without UI

**Run the main script**:

    ```bash
    python main.py
    ```

## File Descriptions

- **app.py**: The main Flask application file that handles routes and file uploads.
- **create_gifs.py**: Contains functions to create GIFs with captions from video segments.
- **segment.py**: Contains functions to segment the video based on provided timestamps.
- **transcribe.py**: Contains functions to transcribe the video using Whisper.
- **static/**: Contains static files such as CSS and directories for storing video segments and generated GIFs.
- **templates/**: Contains HTML templates for the web pages.

## Future Enhancements

- Improve error handling and user feedback.
- Add more customization options for the GIFs (e.g., font size, colors).
- Allow users to edit segments before generating GIFs.
- Add support for multiple languages in transcription.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes.

## Acknowledgements

- [MoviePy](https://zulko.github.io/moviepy/) for video processing.
- [Whisper](https://github.com/openai/whisper) for transcription.
- [Flask](https://flask.palletsprojects.com/) for the web framework.

FROM openai_whisper

RUN apt-get update && apt-get install -y ffmpeg

RUN python3 -m pip install audio-extract moviepy

COPY video_name.mp4 /app/video_name.mp4

WORKDIR /app
FROM python:3.11-slim

RUN apt-get update && apt-get install -y ffmpeg

RUN python3 -m pip install audio-extract moviepy 

RUN pip install openai-whisper

COPY video_to_transcribe.mp4 /app/video_to_transcribe.mp4

WORKDIR /app
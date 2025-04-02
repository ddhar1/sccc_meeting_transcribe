import whisper
import os
from audio_extract import extract_audio
from moviepy import AudioFileClip
import time
import json

from datetime import timedelta
video_path = "/app/video_to_transcribe.mp4"
audio_path = "/app/audio.mp3"
MIN_IN_CHUNK = 10
# Get the duration of the video
video = AudioFileClip(video_path)
video_duration = video.duration  # in seconds

# Process the video in chunks of 10 minutes
chunk_duration = 60.0 * MIN_IN_CHUNK
num_chunks = int(video_duration // chunk_duration) + (1 if video_duration % chunk_duration > 0 else 0)

# Load the Whisper model
model = whisper.load_model("base.en")
t = time.time()
print("start")
def format_timestamp(seconds):
    return str(timedelta(seconds=int(seconds)))

for i in range(num_chunks-2, num_chunks):
    start_time_seconds = i * chunk_duration
    end_time_seconds = min((i + 1) * chunk_duration, video_duration-1)
    start_time = format_timestamp(start_time_seconds)
    end_time = format_timestamp(end_time_seconds)
    chunk_audio_path = f"/app/audio_chunk_{i}.mp3"

    # Extract audio for the current chunk
    extract_audio(input_path=video_path, output_path=chunk_audio_path, start_time=start_time, duration=end_time_seconds - start_time_seconds)

    # Transcribe the audio chunk
    print(f"Transcribing audio chunk {i + 1}/{num_chunks}...")
    if i == 0:
        t2 = time.time()
    result = model.transcribe(chunk_audio_path, fp16=False)
        
    # Write the transcription to a file
    with open(f"/app/data2/transcription_chunk_{i}.txt", "w") as file:
        file.write(json.dumps(result))
    if i == 0:
        print("first 10 min took", (time.time()-t2)/60)
        print("What result looks like",result.keys())
print("took minutes", (time.time()-t)/60)
print("done saving transcript")

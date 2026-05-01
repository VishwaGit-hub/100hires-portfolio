from youtube_transcript_api import YouTubeTranscriptApi
import sys
import os

video_id = sys.argv[1]
author = sys.argv[2]

# fetch transcript
api = YouTubeTranscriptApi()
transcript = api.fetch(video_id)

text = "\n".join([t.text for t in transcript])

# create folder if not exists
folder_path = f"research/youtube-transcripts/{author}"
os.makedirs(folder_path, exist_ok=True)

# save file
file_path = f"{folder_path}/{video_id}.md"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(f"# Video ID: {video_id}\n\n")
    f.write(text)

print(f"Saved: {file_path}")
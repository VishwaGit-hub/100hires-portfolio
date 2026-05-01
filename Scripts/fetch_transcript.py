from youtube_transcript_api import YouTubeTranscriptApi
import os
import time

api = YouTubeTranscriptApi()

INPUT_FILE = "scripts/video_list.txt"
BASE_DIR = "research/youtube-transcripts"

with open(INPUT_FILE, "r") as file:
    lines = file.readlines()

for line in lines:
    # skip empty lines
    if not line.strip():
        continue

    try:
        author, video_id = line.strip().split()

        transcript = api.fetch(video_id)
        text = "\n".join([t.text for t in transcript])

        # create folder per author
        folder_path = os.path.join(BASE_DIR, author)
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, f"{video_id}.md")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# Video ID: {video_id}\n")
            f.write(f"# Author: {author}\n\n")
            f.write(text)

        print(f"[SUCCESS] Saved: {file_path}")

    except Exception as e:
        print(f"[FAILED] {line.strip()} → {e}")

    # avoid IP blocking
    time.sleep(2)
import sys
import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def download_videos(singer, num_videos):
    print("Downloading videos...")
    
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True
    }

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    search_query = f"ytsearch{num_videos}:{singer} songs"

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


def convert_and_trim(duration):
    print("Converting and trimming...")

    audio_clips = []
    
    for file in os.listdir("downloads"):
        file_path = os.path.join("downloads", file)
        
        try:
            audio = AudioSegment.from_file(file_path)
            trimmed = audio[:duration * 1000]   # Convert sec to ms
            audio_clips.append(trimmed)
        except Exception as e:
            print(f"Skipping {file}: {e}")

    return audio_clips


def merge_audios(audio_clips, output_file):
    print("Merging audio files...")

    if not audio_clips:
        print("No audio clips found.")
        return

    final_audio = audio_clips[0]
    for clip in audio_clips[1:]:
        final_audio += clip

    final_audio.export(output_file, format="mp3")
    print("Mashup created successfully!")


def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]
    
    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except ValueError:
        print("NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)

    output_file = sys.argv[4]

    if num_videos <= 10:
        print("NumberOfVideos must be greater than 10.")
        sys.exit(1)

    if duration <= 20:
        print("AudioDuration must be greater than 20 seconds.")
        sys.exit(1)

    try:
        download_videos(singer, num_videos)
        clips = convert_and_trim(duration)
        merge_audios(clips, output_file)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

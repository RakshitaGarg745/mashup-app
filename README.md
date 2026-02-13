# 🎵 YouTube Mashup Generator

This project implements a YouTube Mashup Generator as required in the assignment.

It includes:

-  Program 1 – Command Line Python Application
-  Program 2 – Flask-based Web Application



### Program 1 – Command Line Application

## 📖 Description

This program:

- Downloads **N videos** of a given singer from YouTube  
- Converts videos to audio  
- Cuts first **Y seconds** from each audio file  
- Merges all trimmed audios into one final output file  



## 📂 File Naming Format

102303498.py


## ▶️ How To Run

```bash
python <102303498.py "<SingerName>" <NumberOfVideos> <AudioDuration> <OutputFileName>
```

### Parameters

Parameter	Description
SingerName	Name of singer
NumberOfVideos	Must be greater than 10
AudioDuration	Must be greater than 20 seconds
OutputFileName	Final merged mp3 file


### Features Implemented

✔ Correct number of parameter validation

✔ Input validation checks

✔ Exception handling

✔ Uses PyPI libraries

✔ Automatic folder creation

✔ Audio-only optimized download

### Libraries Used (Program 1)
``` bash
yt-dlp
pydub
ffmpeg
os
sys
```

## Program 2 – Web Application

#Description

A Flask-based web service that:

Accepts user input via web form

Downloads YouTube audio

Trims and merges audio files

Creates a zip file

Sends result via email

# User Inputs

Singer Name

Number of Videos (> 10)

Duration (> 20 seconds)

Email ID

▶️ How To Run Locally
1️⃣ Install Dependencies
pip install -r requirements.txt



## Output Generated

Final MP3 mashup file

Zip file containing mashup

Email with attached zip file


### Author Details

Roll Number: 102303498

Subject: Predictive Analysis



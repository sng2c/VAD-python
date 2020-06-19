ffmpeg -i $1 -vn -acodec pcm_s16le -ac 1 -ar 48000 $1.wav

import ffmpeg
import subprocess

def start_stream():
    try:
        stream = ffmpeg.input('video-input/sample.mp4')
        stream = ffmpeg.output(stream, 'rtmp://live.twitch.tv/app/YOUR_STREAM_KEY',
                              f='flv')
        ffmpeg.run(stream)
    except Exception as e:
        print("Lỗi:", e)

if __name__ == "__main__":
    start_stream()   

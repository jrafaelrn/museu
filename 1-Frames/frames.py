from moviepy.editor import *
from PIL import Image
import time, os


def set_folder():

    # Check if folder exists
    if os.path.exists('./temp/frames'):
        for file in os.listdir('./temp/frames'):
            os.remove(os.path.join('./temp/frames', file))

    else:
        os.makedirs('./temp/frames')



def extract_frames(file_name):

    print(f"Extracting frames from {file_name}...")
    file_name = f'./temp/{file_name}'
    print(f"Extracting frames from {file_name}...")

    video = VideoFileClip(file_name)
    tempo_total = video.duration
    print("\nTempo total video: " + str(tempo_total))

    fps_video = video.fps
    print(f'FPS: {fps_video}')

    total_frames = video.reader.nframes
    print(f'Total de frames: {total_frames}')

    frame = 0

    start_time = time.time()

    while frame < total_frames:
        video.save_frame(f'./temp/frames/{frame}.png', t=frame/fps_video)
        frame += 1

        if frame % 100 == 0:
            print(f'{frame} frames salvos')
    
    print(f'{frame} frames salvos')

    stop_time = time.time()

    return start_time, stop_time, total_frames, fps_video


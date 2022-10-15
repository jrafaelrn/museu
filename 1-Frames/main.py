from google_keys import *
import google_drive, google_sheets, frames, os, platform, time



def main():

    print("Starting...")
    clear_env()

    API_KEY = get_api_key("api-key")
    
    # Download file from Google Drive
    google_drive.set_credentials(API_KEY)
    name_file = google_drive.download_file()


    # Split file into frames
    if name_file is None:
        print("No files found")
        return 
    
    frames.set_folder()
    start_time,stop_time, total_frames, fps_video = frames.extract_frames(name_file)

    # Print time human readable
    print(f"Start time: {time.strftime('%H:%M:%S', time.gmtime(start_time))}")
    print(f"Stop time: {time.strftime('%H:%M:%S', time.gmtime(stop_time))}")
    print(f"Total time: {time.strftime('%H:%M:%S', time.gmtime(stop_time - start_time))}")

    # Save frames to Google Drive

    # Save file details to Google Sheets



def clear_env():

    print("Clearing environment...")

    if platform.system() == 'Linux':
        path_folder = "./temp"
    else:
        path_folder = f'{os.path.dirname(os.path.abspath(__file__))}\\temp'
        

    for file in os.listdir(path_folder):
        try:
            os.remove(os.path.join(path_folder, file))

        except Exception as e:
            print(f'Error: {e}')
            os.removedirs(os.path.join(path_folder, file))
            continue



main()
from google_keys import *
import google_drive, google_sheets, frames, os, platform



def main():

    print("Starting...")
    clear_env()

    API_KEY = get_api_key("api-key")
    
    # Download file from Google Drive
    google_drive.set_credentials(API_KEY)
    result, name_file = google_drive.download_file()


    # Split file into frames
    if result:
        frames.set_folder()
        frames.extract_frames(name_file)

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
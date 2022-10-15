import shutil
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
import io, json, platform, os


GOOGLE_DRIVE_API_KEY = None
SCOPES = ['https://www.googleapis.com/auth/drive']



def set_credentials(credentials):
    global GOOGLE_DRIVE_API_KEY
    json_credentials = json.loads(credentials)
    GOOGLE_DRIVE_API_KEY = json_credentials


def download_file():

    creds = ServiceAccountCredentials.from_json_keyfile_dict(GOOGLE_DRIVE_API_KEY, SCOPES)

    with build('drive', 'v3', credentials=creds) as gdrive:
        
        try:

            response = gdrive.files().list(fields='nextPageToken, ' 'files(id, name)').execute()
            
            for file in response.get('files', []):
                
                id_file = file.get('id')
                name_file = file.get('name')
                path_file = get_file_path(gdrive, id_file)

                if path_file.find('input') == -1:
                    continue
                
                video_file = get_file(id_file, name_file) 
                return name_file
            
        except Exception as error:
            print(F'An error occurred: {error}')
            return None




def get_file(file_id, name_file):
    
    creds = ServiceAccountCredentials.from_json_keyfile_dict(GOOGLE_DRIVE_API_KEY, SCOPES)

    with build('drive', 'v3', credentials=creds) as gdrive:
        
        try:

            request = gdrive.files().get_media(fileId=file_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(F'Download {int(status.progress() * 100)}%')

            file.seek(0)
            destination_path = get_destination_path()
            with open(f'{destination_path}{name_file}', 'wb') as f:
                shutil.copyfileobj(file, f)
            
            print(f"Download {name_file} complete")

        except HttpError as error:
            print(F'An error occurred: {error}')
            print('Probably any file is found.')
            return None

        return file.getvalue()



def get_file_path(gdrive, file_id):

    response = gdrive.files().get(fileId=file_id, fields='id, name, parents').execute()
    path_result = ''

    parent = response.get('parents')
    if parent:
        while True:
            folder = gdrive.files().get(fileId=parent[0], fields='id, name, parents').execute()
            parent = folder.get('parents')
            if parent is None:
                break
            path_result = folder.get('name') + '/' + path_result

    
    print(f'Path: {path_result}')
    return path_result




def get_destination_path():
    
    if platform.system() == 'Linux':
        return "./temp/"
    
    return f'{os.path.dirname(os.path.abspath(__file__))}\\temp\\'
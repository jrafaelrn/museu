from google.cloud import secretmanager
import os


#####################################
#       GOOGLE SECRET MANAGER       #
#####################################

def set_credentials_env():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credentials.json"



def get_api_key(SECRET_ID):

    set_credentials_env()
    API_KEY = None
    secrets = secretmanager.SecretManagerServiceClient()
    
    try:

        PROJECT_ID = "museu-auto"

        name = f"projects/{PROJECT_ID}/secrets/{SECRET_ID}/versions/latest"
        response = secrets.access_secret_version(request={"name": name})

        API_KEY = response.payload.data.decode("UTF-8")

    except Exception as e:
        print(f'Error: {e}')
        API_KEY = None    
    
    return API_KEY

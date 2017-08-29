import os
from utils.logger import logger

def clean_up_folder(temp_folder):

    try:
        for temp_file in os.listdir(temp_folder):
            file_path = os.path.join(temp_folder, temp_file)
            os.unlink(file_path)
        
        os.rmdir(temp_folder)
        return True

    except Exception as e:
        logger('clean_up_folder', 'Error in cleaning up direcrory ' + temp_folder)
        logger('clean_up_folder', e)
        return False

    finally:
        logger('clean_up_folder', 'Clean up completed')
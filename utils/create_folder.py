import os
from utils.logger import logger

def create_folder(temp_folder):
    try:
        if os.path.exists(temp_folder):
            logger('create_folder', 'Directory ' + temp_folder + ' already exists')
            return True
        
        os.mkdir(temp_folder)
        return True

    except Exception as e:
        logger('create_folder', 'Error creating direcrory ' + temp_folder)
        logger('create_folder', e)
        return False

    finally:
        logger('create_folder', 'Directroy creation completed')
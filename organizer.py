import os
import shutil

types = ["documents", "audio", "programs", "images", "videos", "otros"]

# Determine type

def switch(T):

    if T in ['.pdf', '.docx', '.cbr']:
        return "documents"
    elif T in ['.mp3', '.ogg', '.wav', '.mid', '.midi']:
        return "audio"
    elif T in ['.exe', '.msi', '.diagcab']:
        return "programs"
    elif T in ['.png', '.jpeg', 'gif', '.jpg', '.webp', '.ico', '.svg']:
        return "images"
    elif T in ['.mp4', '.mkv']:
        return "videos"
    elif T in ['.url', '.lnk', '.py']:
        return None
    else:
        return "otros"

# Generate folders in Downloads

for directory in types:

    os.makedirs(directory, exist_ok=True)

# Categorize file types into the folders

with os.scandir('.') as d:
    
    for file in d:
        
        name, extension = os.path.splitext(file.name)

        extension = extension.lower()

        if not file.is_dir():
        
            destiny = switch(extension)

            if destiny is not None:

                shutil.move(file.path, destiny)


import os
import re
import shutil

def create_directory_with_matching_files(source_directory, target_directory, keywords):
    pattern = re.compile(r"|".join(keywords), re.IGNORECASE)

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if pattern.search(file):
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_directory, file)
                shutil.copy2(source_path, target_path)

source_directory_path = "pdf-processing-slp/data_respaper_text_links"
target_directory_path = "pdf-processing-slp/data_respaper_text_links_maths_science"
keywords = ["Science", "Maths","Biology", "Chemistry", "Physics", "cbse"]

create_directory_with_matching_files(source_directory_path, target_directory_path, keywords)

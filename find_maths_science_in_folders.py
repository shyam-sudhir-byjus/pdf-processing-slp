import os
import re

def find_files_with_keywords(directory, keywords):
    pattern = re.compile(r"|".join(keywords), re.IGNORECASE)
    matching_files = []

    for root, dirs, files in os.walk(directory):
        for f in files:
            if pattern.search(f):
                matching_files.append(os.path.join(root, f))

    return matching_files


if __name__ == "__main__":
    directory_path = "pdf-processing-slp/data_respaper_text_links"

    keywords = ["Science","Maths","Chemistry","Physics","Biology","cbse"]
    matching_files = find_files_with_keywords(directory_path, keywords)

    print("Matching files:")
    for f in matching_files:
        print(f)

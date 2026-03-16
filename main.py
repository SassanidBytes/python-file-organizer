import os
import shutil

folder = "alifiles"

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if os.path.isfile(file_path):
        ext = filename.split(".")[-1]

        if ext in ["jpg", "png"]:
            target = os.path.join(folder, "Images")
        elif ext == "pdf":
            target = os.path.join(folder, "Documents")
        elif ext == "mp3":
            target = os.path.join(folder, "Music")
        elif ext == "txt":
            target = os.path.join(folder, "Text")
        else:
            continue

        os.makedirs(target, exist_ok=True)

        shutil.move(file_path, os.path.join(target, filename))

print("Files organized.")
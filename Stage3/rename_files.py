import os

def rename_files():
    image_folder = r'C:\Users\hb\Documents\udacity-nd-programming\Stage3\prank'
    files = os.listdir(image_folder)
    print(files)
    start_path = os.getcwd()
    os.chdir(image_folder)
    for file in files:
        os.rename(file, file.translate(None,'0123456789'))
    os.chdir(start_path)
rename_files()

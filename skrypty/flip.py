from PIL import Image
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def remove_duplicates(path):
    # Utwórz pusty słownik do przechowywania wartości hash obrazów
    image_dict = {}
    
    # Iteruj przez wszystkie pliki w folderze
    for filename in os.listdir(path):
        if filename.endswith('.png'):
            filepath = os.path.join(path, filename)

            # Otwórz obraz przy użyciu biblioteki PIL
            image = Image.open(filepath)
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            image.save(os.path.join(path, "mirror_"+filename+".png"))

remove_duplicates(current_dir)

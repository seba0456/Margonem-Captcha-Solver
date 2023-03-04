from PIL import Image
import os

def remove_duplicates(path):
    # Utwórz pusty słownik do przechowywania wartości hash obrazów
    image_dict = {}

    # Iteruj przez wszystkie pliki w folderze
    for filename in os.listdir(path):
        if filename.endswith('.png'):
            filepath = os.path.join(path, filename)

            # Otwórz obraz przy użyciu biblioteki PIL
            image = Image.open(filepath)

            # Oblicz wartość hash obrazu
            image_hash = hash(image.tobytes())

            # Sprawdź, czy wartość hash już istnieje w słowniku
            if image_hash in image_dict:
                # Jeśli wartość hash już istnieje, usuń duplikat
                os.remove(filepath)
            else:
                # Jeśli wartość hash nie istnieje, dodaj ją do słownika
                image_dict[image_hash] = filepath
remove_duplicates(path="Cuts")
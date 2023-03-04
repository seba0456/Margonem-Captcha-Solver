import os
from PIL import Image
from tqdm import tqdm

# Wymiary wycinków
cut_width = 106
cut_height = 79

# Współrzędne wycięć
cut_coords = [
    (771, 407), (878, 407), (985, 407),
    (985, 488), (878, 488), (771, 488)
]
#staty
pieces=int(0)
# Przejście do bieżącego katalogu
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

# Stworzenie folderu Cuts, jeśli nie istnieje
if not os.path.exists("Cuts"):
    os.makedirs("Cuts")

# Przeszukanie katalogu w poszukiwaniu plików PNG
for file_name in tqdm(os.listdir()):
    if file_name.lower().endswith(".png"):
        tqdm.write(f'Processing file: {file_name}')
        
        # Otwarcie pliku i przypisanie go do zmiennej image
        image = Image.open(file_name)

        # Przetworzenie każdego wycinka
        for i, coords in enumerate(cut_coords):
            # Obliczenie współrzędnych wycinka
            x1, y1 = coords
            x2, y2 = x1 + cut_width, y1 + cut_height

            # Wycięcie wskazanego fragmentu z obrazka
            cut_image = image.crop((x1, y1, x2, y2))

            # Stworzenie nazwy pliku dla wycinka i zapisanie go w folderze Cuts
            cut_file_name = os.path.join("Cuts", f"{file_name}_{i}.png")
            cut_image.save(cut_file_name)
            pieces+=1

        # Zamknięcie pliku
        image.close()
print("Created: " + str(pieces))
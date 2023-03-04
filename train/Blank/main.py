import pyperclip
import random
import string
from PIL import ImageGrab

while True:
    # Pobierz obraz z schowka
    clipboard_img = ImageGrab.grabclipboard()

    # Jeśli obraz jest obiektem PIL Image, zapisz go jako plik PNG
    if clipboard_img:
        # Generuj losową nazwę pliku
        filename = ''.join(random.choices(string.ascii_lowercase, k=10)) + '.png'
        # Zapisz plik w bieżącym katalogu
        try:
            clipboard_img.save(filename, 'PNG')
        except:
            print("bug!")
        print(f'Zapisano obraz jako {filename}.')
        input('Naciśnij Enter, aby kontynuować...')
    else:
        print('Brak obrazu w schowku. (Blank)')
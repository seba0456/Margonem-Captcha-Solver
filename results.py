import tensorflow as tf
from tensorflow import keras
import numpy as np

#Rozmiar obrazków do nauki
img_height = 79
img_width = 106

# Wczytaj wytrenowany model z dysku
model = keras.models.load_model('model')

# Wczytaj obrazek testowy
img = keras.preprocessing.image.load_img(
    'tester.png',
    target_size=(img_height, img_width)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Dodaj dodatkowy wymiar, aby mieć jednoczesność

# Dokonaj predykcji na obrazku testowym
predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

# Wypisz wynik predykcji
class_names=['Blank', 'Not_Blank']
print("Obrazek testowy należy do kategorii {} z prawdopodobieństwem {:.2f}%"
      .format(class_names[np.argmax(score)], 100 * np.max(score)))


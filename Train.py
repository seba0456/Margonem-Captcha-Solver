import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tqdm import tqdm

#Rozmiar obrazków do nauki
img_height = 79
img_width = 106

# Liczba zdjęć w jednej paczce
batch_size = 32

# Liczba epok
epochs = 10


# Załaduj dane treningowe i walidacyjne z folderów "kategoria_1" i "kategoria_2"
train_ds = keras.preprocessing.image_dataset_from_directory(
    "train",
    validation_split=0.15,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size,
    class_names=['Blank', 'Not_Blank']
)
val_ds = keras.preprocessing.image_dataset_from_directory(
    "val",
    validation_split=0.15,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size,
    class_names=['Blank', 'Not_Blank']
)

# Definiuj model sieci neuronowej
model = keras.Sequential([
    layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(len(train_ds.class_names), activation='softmax')
])


# Skompiluj model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Trenuj model
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs,
    verbose=0,
    callbacks=[tf.keras.callbacks.LambdaCallback(
        on_epoch_end=lambda epoch, logs: tqdm.write(f'Epoch {epoch+1}/{epochs} - loss: {logs["loss"]:.4f} - accuracy: {logs["accuracy"]:.4f} - val_loss: {logs["val_loss"]:.4f} - val_accuracy: {logs["val_accuracy"]:.4f}')
    )]
)

# Zapisz model na dysku
model.save('model')

import os

folder_path = "Blang"
output_name = "TrainInage"
output_extension = ".png"
index = 0

for filename in os.listdir(folder_path):
    if filename.endswith(output_extension):
        new_name = f"{output_name}{index:03d}{output_extension}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
        index += 1

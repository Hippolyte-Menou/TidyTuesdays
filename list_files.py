import os

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield (root, file)


for file in list_files("tips"):
    print(os.path.join(*file))


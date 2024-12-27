import os

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield (root, file)

def files_to_yaml(directory, tabs = 5):
    for file in filter(lambda x: x[1].endswith(".qmd"), list_files(directory)):
        formatted = f'{"  " * tabs}- text: "{file[1].replace(".qmd", "")}"\n{"  " * (tabs + 1)}href: {os.path.join(*file)}'
        print(formatted)

def files_to_markdown(directory):
    for file in filter(lambda x: x[1].endswith(".qmd"), list_files(directory)):
        print(f'- [{file[1].replace(".qmd", "")}]({os.path.join(*file)})')

files_to_yaml("tips")
files_to_markdown("tips")



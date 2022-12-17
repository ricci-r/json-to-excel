

import glob
from pathlib import Path
from time import sleep

import pandas as pd
from tqdm import tqdm


def display_files(extension='json'):
    source = glob.glob(f'./input/*/*/*.{extension}')
    return source


def calculate_size(dir_path):
    file_size = Path(dir_path).stat().st_size
    return file_size


def convert_files():
    list_files = display_files()

    for i in tqdm(range(len(list_files))):
        try:
            files_position = list_files[i]
            total_files = calculate_size(files_position)
            print(f' Atualizando os arquicos {total_files} Mb')

            df = pd.read_json(files_position, encoding='utf-8')
            df.to_excel(f'{files_position[:-5]}.xlsx', index=False)

        except Exception as error:
            print(f'Erro no processamento {files_position}', error)


if __name__ == '__main__':
    convert_files()

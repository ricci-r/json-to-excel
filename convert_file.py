

import glob
import os
from pathlib import Path
from time import sleep

import pandas as pd
from tqdm import tqdm

BASE_DIR = Path(__file__).resolve().parent
INPUT = os.path.join(BASE_DIR, 'input')
OUTPUT = os.path.join(BASE_DIR, 'output')


def display_files(extension='json'):
    source = glob.glob(f'{INPUT}/*/*/*.{extension}')
    print(source)
    return source


def calculate_size(dir_path):
    file_size = Path(dir_path).stat().st_size
    return file_size

    
def convert_files():
    list_files = display_files()

    for i in tqdm(range(len(list_files))):
        try:
            sleep(2)

            files_position = list_files[i]
            total_files = calculate_size(files_position)
            print(f' Arquivo {files_position} com total de {total_files / 1024}  Mb')

            df = pd.read_json(files_position, encoding='utf-8')
            file_name = os.path.basename(files_position)
            df.to_excel(f'{OUTPUT}/{file_name[:-5]}.xlsx', index=False)

        except Exception as error:
            print(f'Erro no processamento {files_position}', error)

    print('Arquivos convertidos com sucesso.')

if __name__ == '__main__':
    convert_files()

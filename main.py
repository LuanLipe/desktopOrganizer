import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

print("=" * 40)
print("     ORGANIZADOR DE ARQUIVOS")
print("=" * 40)

Tk().withdraw()

pasta = askdirectory(title="Selecione a pasta para organizar")

arquivos = os.listdir(pasta)

contador = 0

for arquivo in arquivos:

    caminho_arquivo = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho_arquivo):

        if arquivo.lower().endswith(".png") or arquivo.lower().endswith(".jpg"):

            pasta_imagens = os.path.join(pasta, "IMAGES")

            os.makedirs(pasta_imagens, exist_ok=True)

            shutil.move(caminho_arquivo, pasta_imagens)

            contador += 1

            print(f"{arquivo} movido para Imagens")

        elif arquivo.lower().endswith(".pdf"):

            pasta_pdf = os.path.join(pasta, "PDF")

            os.makedirs(pasta_pdf, exist_ok=True)

            shutil.move(caminho_arquivo, pasta_pdf)

            contador += 1

            print(f"{arquivo} movido para a pasta PDF")

        elif arquivo.lower().endswith(".txt"):

            pasta_txt = os.path.join(pasta, "TXT")

            os.makedirs(pasta_txt, exist_ok=True)

            shutil.move(caminho_arquivo, pasta_txt)

            contador += 1

            print(f"{arquivo} movido para Txt")

        elif arquivo.lower().endswith(".mp3"):

            pasta_mp3 = os.path.join(pasta, "MP3")

            os.makedirs(pasta_mp3, exist_ok=True)

            shutil.move(caminho_arquivo, pasta_mp3)

            contador += 1

            print(f"{arquivo} movido para a pasta MP3")

        elif arquivo.lower().endswith(".mp4"):

            pasta_mp4 = os.path.join(pasta, "MP4")

            os.makedirs(pasta_mp4, exist_ok=True)

            shutil.move(caminho_arquivo, pasta_mp4)

            contador += 1

            print(f"{arquivo} movido para a pasta Mp4")

        else:

            print(f"{arquivo} não possui tipo definido")


print(f"{contador} arquivos organizados!")
print("=" * 40)
print("     Organização concluída!")
print("=" * 40)

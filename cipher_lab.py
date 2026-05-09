import os
from datetime import datetime

PASTA = "ambiente_teste"
LOG = "../registros/eventos_execucao.log"

def registrar(msg):
    with open(LOG, "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()} - {msg}\n")

def simular_bloqueio():
    arquivos = os.listdir(PASTA)

    for arquivo in arquivos:
        if arquivo.endswith(".txt"):
            caminho = os.path.join(PASTA, arquivo)

            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()

            bloqueado = f"[BLOQUEADO SIMULADO]\n{conteudo[::-1]}"

            with open(caminho + ".lock", "w", encoding="utf-8") as f:
                f.write(bloqueado)

            registrar(f"Arquivo simulado como bloqueado: {arquivo}")

simular_bloqueio()

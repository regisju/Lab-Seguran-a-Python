from datetime import datetime

log_file = "registros/eventos_execucao.log"

print("Sistema de monitoramento iniciado (simulação).")

while True:
    entrada = input("comando> ")

    if entrada.lower() == "exit":
        break

    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()} - entrada registrada: {entrada}\n")

print("Sessão finalizada.")

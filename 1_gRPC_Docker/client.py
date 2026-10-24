import os
import socket
import time
import grpc
import saludo_pb2
import saludo_pb2_grpc

SERVIDOR = os.environ.get("SERVIDOR", "servidor:50051")
DOCKER_CONTEXT = os.environ.get("DEBIAN_FRONTEND", "")

def ciclo():
    canal = grpc.insecure_channel(SERVIDOR)
    stub = saludo_pb2_grpc.SaludoStub(canal)
    
    # Toma el nombre de CLIENTE_ID o usa el hostname por defecto
    nombre = os.environ.get("CLIENTE_ID", socket.gethostname())

    idiomas = ["es", "en", "fr"]
    cnt = 0

    while True:
        idioma_actual = idiomas[cnt % len(idiomas)]
        
        # Llamada a Decir
        r = stub.Decir(saludo_pb2.Peticion(nombre=f"{nombre} #{cnt}", idioma=idioma_actual), wait_for_ready=True)
        print(f"{cnt}: {r.mensaje}")
        
        # Cada 5 peticiones llama a Despedir
        if (cnt + 1) % 5 == 0:
            r_despedida = stub.Despedir(saludo_pb2.Peticion(nombre=f"{nombre}", idioma=idioma_actual), wait_for_ready=True)
            print(f"{r_despedida.mensaje}")
            
        cnt += 1
        time.sleep(1)

if __name__ == "__main__":
    ciclo()
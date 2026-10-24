from concurrent import futures
import grpc
import saludo_pb2
import saludo_pb2_grpc

class SaludoServicio(saludo_pb2_grpc.SaludoServicer):
    def Decir(self, request, context):
        print(f"Petición recibida de: {request.nombre} en idioma: {request.idioma}")
        
        if request.idioma == "en":
            saludo = "Hello"
        elif request.idioma == "fr":
            saludo = "Bonjour"
        else:
            saludo = "Hola"  # Por defecto para "es" u otros
            
        return saludo_pb2.Respuesta(mensaje=f"{saludo} {request.nombre}, soy servidor")

    def Despedir(self, request, context):
        print(f"Despedida de: {request.nombre}")
        
        if request.idioma == "en":
            despedida = "Goodbye"
        elif request.idioma == "fr":
            despedida = "Au revoir"
        else:
            despedida = "Adiós"
            
        return saludo_pb2.Respuesta(mensaje=f"{despedida} {request.nombre}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    saludo_pb2_grpc.add_SaludoServicer_to_server(SaludoServicio(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    print("Servidor gRPC escuchando en el puerto 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
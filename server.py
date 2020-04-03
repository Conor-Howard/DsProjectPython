import grpc
from concurrent import futures
import time

# import the generated classes
import lights_pb2
import lights_pb2_grpc


# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class LightService(lights_pb2_grpc.LightServiceServicer):

    def changeColour(self, request, context):
        return lights_pb2.changeColour(message='Colour: ' % request.Colour)


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
lights_pb2_grpc.add_LightServiceServicer_to_server(
        LightService(), server)
print('Starting server. Listening on port 60061.')
server.add_insecure_port('[::]:60061')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
import grpc
from concurrent import futures
import time

import lights_pb2
import lights_pb2_grpc

class LightService(lights_pb2_grpc.LightServiceServicer):

    def changeColour(self, request, context):
    	print("Request to change the light colour to: " + request.colour)
        response = lights_pb2.Colour()
        response.colour = ("Colour has been changed to: " + request.colour)
        return response

    # def powerOn(self, request, context):
    # 	print("request to change lights power: " + request.state)
    # 	response = lights_pb2.Power()
    # 	response.state = ("Power for light is now: " + request.state)
    # 	return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
lights_pb2_grpc.add_LightServiceServicer_to_server(
        LightService(), server)
print('Starting server. Listening on port 60061.')
server.add_insecure_port('[::]:60061')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
import grpc

import lights_pb2
import lights_pb2_grpc


channel = grpc.insecure_channel('localhost:60061')
stub = lights_pb2_grpc.LightServiceStub(channel)
# power = lights_pb2.Power(state=True)
# power_response = stub.powerOn(power)
colour = lights_pb2.Colour(colour="red")
colour_response = stub.changeColour(colour)

#print("Light Power is now: " + power_response.colour)
print("Colour is now: " + colour_response.colour)

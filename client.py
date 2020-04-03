import grpc

from __future__ import print_function

import logging

import lights_pb2
import lights_pb2_grpc

channel = grpc.insecure_channel('localhost:60061')
stub = lights_pb2_grpc.LightServiceStub(channel)

power = lights_pb2.PowerRequest(state=True)

response = stub.powerOn(power)

print(response.value)
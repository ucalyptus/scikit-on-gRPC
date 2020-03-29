
import grpc
from concurrent import futures
import time

# import the generated classes :
import model_pb2
import model_pb2_grpc

# import the function we made :
import predict_credit_status as pcs


# create a class to define the server functions, derived from
# usingSKlearn_pb2_grpc.PredictServicer :
class PredictServicer(model_pb2_grpc.PredictServicer):
    def predict_credit_status(self, request, context):
        # define the buffer of the response :
        response = model_pb2.Prediction()
        # get the value of the response by calling the desired function :
        response.card = pcs.predict_credit_status(request.reports,request.expenditure, request.age, request.income)
        return response


# creat a grpc server :
server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))

model_pb2_grpc.add_PredictServicer_to_server(PredictServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)


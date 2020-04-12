import grpc
from random import randint
from timeit import default_timer as timer
import pandas as pd
import numpy as np

# import the generated classes
import model_pb2
import model_pb2_grpc


start_ch = timer()

# open a gRPC channel
channel = grpc.insecure_channel("localhost:50051")

# create a stub (client)
stub = model_pb2_grpc.PredictStub(channel)
end_ch = timer()

# reports   = [randint(0,14) for i in range(0,1000)]
# expenditure = [randint(0,3100) for i in range(0,1000)]
# age    = [randint(18,85) for i in range(0,1000)]
# income = [randint(1,14) for i in range(0,1000)]

df = pd.read_excel("credit.xlsx")
df = df.sample(frac=0.5, replace=True, random_state=1)
reports = np.asarray(df.reports)
expenditure = np.asarray(df.expenditure)
age = np.asarray(df.age)
income = np.asarray(df.income)


ans_lst = []

start = timer()

for i in range(0, len(reports) - 1):
    # create a valid request message
    requestPrediction = model_pb2.Features(
        reports=reports[i], expenditure=expenditure[i], age=age[i], income=income[i]
    )

    # make the call
    responsePrediction = stub.predict_credit_status(requestPrediction)
    ans_lst.append(responsePrediction.card)
    answer = "yes" if responsePrediction.card == 1 else "no"
    print("{}::{}".format(i, answer))
print("Done!")
end = timer()
all_time = end - start
ch_time = end_ch - start_ch
print("Time spent for {} predictions is {}".format(len(reports), (all_time)))
print("In average, {} second for each prediction".format(all_time / len(reports)))
print(
    "That means you can do {} predictions in one second".format(
        int(1 / (all_time / len(reports)))
    )
)
print("Time for connecting to server = {}".format(ch_time))

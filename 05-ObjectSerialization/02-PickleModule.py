import pickle

data = [{"id" : 101, "name" : "Ram", "age" : 20}]
print("Before : ")
print("Data",data)

# Pickling
dataset = pickle.dumps(data)
print(dataset)

print("After : ")
# Unpickling
dataset_1 = pickle.loads(dataset)
print(dataset_1)

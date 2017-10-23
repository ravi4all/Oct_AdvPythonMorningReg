import pickle

with open("pickle_1.pickle", 'rb') as file:
    data = pickle.load(file)
    print("Data : ",data)

import pymongo
import pandas as pd
import json

connection_string = "mongodb://localhost:27017"
csv_file_path = "import-data.csv"
database_name = "imported_data"
collection_name = "collected_data"

try:
  client = pymongo.MongoClient(connection_string)
except Exception as e:
    print("An Error occured while connectig the Database \n"+e)

try:
    df = pd.read_csv(csv_file_path)
except Exception as e:
    print("An Error occured while reading CSV file \n"+e)
try:
    data = df.to_dict(orient = "records")
except Exception as e:
    print("An Error occured while converting the data to dictionary \n"+e)
try:
    db = client[database_name]
except Exception as e:
    print("An Error occured on database operation \n"+e)
try:
    db[collection_name].insert_many(data)
    print("Data inserted Successfuly")
except Exception as e:
    print("An Error occured on data insertion operation \n"+e)

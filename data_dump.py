import pymongo
import pandas as pd
import json
from pymongo import MongoClient

















client = pymongo.MongoClient("mongodb+srv://utkarshraj7217:9911953712@cluster0.y8a29mu.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"C:\Users\UTKARSH\OneDrive\Desktop\MedicalExpense\Medical-Expense-Predictor\insurance.csv")

DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns: {df.shape}")

    df.reset_index(drop=True,inplace = True)
    json_record = list(json.loads(df.T.to_json()).values())

    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)





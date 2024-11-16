from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Union
from datetime import *
import os 
from dotenv import load_dotenv
import teradatasql
from Business import Business

load_dotenv()


apiApp = FastAPI()

HOST =  os.getenv("HOST")
USER =  os.getenv("USER")
PASS =  os.getenv("PASS")

db = teradatasql.connect(host=HOST,user = USER, password = PASS)

curse = db.cursor()
 

@apiApp.get("/")
def read_root():
    return {"Hello": "World"}

@apiApp.get("/{nameItem}")
def read_data(nameItem : str):
    query = "SELECT business_name, business_type, location, owner_name, transaction_amount, category, paymentDesc, vendor_name FROM BusinessData1 WHERE business_name = ?"
    curse.execute(query, (nameItem,))
    res = curse.fetchall()
    if not res:
        raise HTTPException(status_code=404, detail="Not Found")
    data = {} 
    i = 0
    for row in res: 
        data[i] = row
        i+=1
    return JSONResponse(content=data)


@apiApp.post("/{uuid}")
async def add_data(uuid : str, req : Request):
    body = await req.json()


    required_keys = ["Amount", "CategoryOfSpend", "paymentDesc", "VenderName"]
    for key in required_keys:
        if key not in body:
            raise HTTPException(status_code=422, detail="Missing Key")
        
    Amount = body["Amount"]
    CategoryOfSpend = body["CategoryOfSpend"]
    paymentDesc = body["paymentDesc"]
    VenderName = body["VenderName"]

    if not isinstance(Amount, (float, int)):
        raise HTTPException(status_code=422, detail="Amount must be a float or an integer")

    B = Business(uuid)

    

    query = f"INSERT INTO {USER}.BusinessData1 (business_name, business_type, location, owner_name, transaction_amount, category, paymentDesc, vendor_name) VALUES (?,?,?,?,?,?,?,?)"
    values =  (str(B.name), str(B.bType), str(B.location), str(B.owner), float(Amount), str(CategoryOfSpend), str(paymentDesc), str(VenderName))
    try:
        curse.execute(query, values)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error {str(e)}")
    return 1

@apiApp.on_event('shutdown')
def shutdown():
    curse.close()
    db.close()
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Union
import teradatasql

apiApp = FastAPI()

HOST = "hackathonfakerfile-mwc2k52q3qz68tzk.env.clearscape.teradata.com"
USER = "demo_user"
PASS = "HackathonTSU2024#"

db = teradatasql.connect(host=HOST,user = USER, password = PASS)

curse = db.cursor()
 

@apiApp.get("/")
def read_root():
    return {"Hello": "World"}

@apiApp.get("/nId/{nameItem}")
def read_data(nameItem : str):
    query = "SELECT * FROM TSikk WHERE business_name = ?"
    curse.execute(query, (nameItem,))
    res = curse.fetchall()
    if not res:
        raise HTTPException(status_code=404, detail="Not Found")
    data = {} 
    i = 0
    for row in res: 
        data[i] = row
        i+=1
    return JSONResponse(content=res)
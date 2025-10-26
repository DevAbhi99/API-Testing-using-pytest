from fastapi import FastAPI, Request, HTTPException #HTTPException is used to raise http exception like if there is any error we can display to the client in a structured way
from pydantic import BaseModel, Field
from enum import IntEnum
from typing import Any, List, Dict
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware


api=FastAPI()


#Middleware

#CORS
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

#GZIP

api.add_middleware(
    GZipMiddleware, minimum_size=1000
)



data:List[Dict[str,Any]]=[{
    "id":1,
    "name":"Subhayan",
    "age":21,
    "priority":1

}] 


class Priority(IntEnum):
    high=3
    medium=2
    low=1

class Datamodel(BaseModel):
    id:int=Field(...,  )  #Field is used for description of schemas
    name:str=Field(..., description='name of the person')
    age:int=Field(..., description='age of the person')
    priority:Priority=Field(default=Priority.high)


#REST API methods
@api.get('/getData')
def getData():
    return data

@api.post('/sendData')
def sendData(new_data:Datamodel):
    data.append(new_data)
    return {"message":"Successfully inserted the data"}

@api.put('/updateData/{index}')
def updateData(new_data:Datamodel,index):
    data[int(index)]=new_data
    return {"message":"Data updated Successfully"}

@api.delete('/deleteData')
def deleteData(new_data:Datamodel):
    data.remove(new_data)
    return {"message":"Data deleted successfully"}

@api.delete('/clearData')
def clearData():
    data.clear()
    return {"message":"Data cleared successfully"}




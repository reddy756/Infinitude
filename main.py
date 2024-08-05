from typing import Union
import copy
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
from fastapi import FastAPI,Path
from typing import Union
from pydantic import BaseModel

app=FastAPI()
class Employee(BaseModel):
    name:str
    qualification:str

employee={
    1:{
        'name':'bhaskar',
        'year':2024
    }
}
@app.get("/home/{employe_id}")
def first(employe_id:int = Path(description="Values are required",gt=0,le=3)):
    if employe_id in employee:
        return employee[employe_id]
    return {'data':'not found'}

@app.get("/home/{employe_id}")
def first(employe_id:int,name:str):
    for employe_id in employee:
        if employee[employe_id]["name"] == name:
            return employee[employe_id]
        return {"name": "not found"}


@app.post("/home/{employe_id}")
def first(employe_id: int, employe: Employee):
    if employe_id in employee:
        return {"data":'user already exists'}
    employee[employe_id]= employe
    return{'data':'Data inserted successfully'}


@app.put("/update/{employe_id}")
def update(employe_id:int, employe:Employee):
    if employe_id not in employee:
        return {"Employe":"NOt exsists"}
    employee[employe_id] = employe

# @app.delete("/del/{employ_id}")
# def delete(employ_id:int):
#     if employ_id in employee:
#         del employee[employ_id]
#         return {'data':"deleted successfully"}
#     return {'data':'not found'}





from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

@app.get('/test')
def first():
    return {'data':'nothing'}

from sqlalchemy import create_engine

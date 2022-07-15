from re import I
from itertools import permutations
from fastapi import FastAPI
import requests

app = FastAPI()
@app.get("/permutaciones")
def permutaticiones(palabra: str):
    return {"Permutaciones": sorted(unique_perms(palabra))}

def unique_perms(series):
    return {"".join(p) for p in permutations(series)}

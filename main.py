#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
# @Time    : 2023/3/29 10:41
# @Author  : wangjun
# @File    : main.py.py
# @explain :
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

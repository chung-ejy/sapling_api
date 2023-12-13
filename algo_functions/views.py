from django.shortcuts import render
from django.http.response import JsonResponse
import pickle
import pandas as pd
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import requests
from database.adatabase import ADatabase
import numpy as np
from algo import algo

db = ADatabase("algo")

@csrf_exempt
def backtestView(request):
    try:
        if request.method == "POST":
            query = json.loads(request.body)
            algo(query)
            complete = []
        else:
            complete = []
    except Exception as e:
        complete = []
        print(str(e))
    return JsonResponse(complete,safe=False)

@csrf_exempt
def tradesView(request):
    try:
        if request.method == "GET":
            db.connect()
            complete = db.retrieve("trades").round(3).replace([np.inf,np.nan],np.nan).dropna().to_dict("records")
            db.disconnect()
        else:
            complete = []
    except Exception as e:
        complete = []
        print(str(e))
    return JsonResponse(complete,safe=False)

@csrf_exempt
def portfoliosView(request):
    try:
        if request.method == "GET":
            db.connect()
            complete = db.retrieve("portfolio").sort_values("date",ascending=True).round(3).fillna(0).to_dict("records")
            db.disconnect()
        else:
            complete = []
    except Exception as e:
        complete = []
        print(str(e))
    return JsonResponse(complete,safe=False)

@csrf_exempt
def recommendationsView(request):
    try:
        if request.method == "GET":
            db.connect()
            complete = db.retrieve("recommendations").sort_values("ticker").round(3).fillna(0)
            complete["date"] = [str(x).split("00:")[0] for x in complete["date"]]
            complete["sell_date"] = [str(x).split("00:")[0] for x in complete["sell_date"]]
            complete = complete.to_dict("records")  
            db.disconnect()
        else:
            complete = []
    except Exception as e:
        complete = []
        print(str(e))
    return JsonResponse(complete,safe=False)
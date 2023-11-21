from django.shortcuts import render
from django.http.response import JsonResponse
import pickle
import pandas as pd
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import requests
from database.adatabase import ADatabase
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

def tradesView(request):
    try:
        if request.method == "GET":
            db.connect()
            complete = db.retrieve("trades").round(3).fillna(0).to_dict("records")
            db.disconnect()
        else:
            complete = []
    except Exception as e:
        complete = []
        print(str(e))
    return JsonResponse(complete,safe=False)

def portfoliosView(request):
    try:
        if request.method == "GET":
            db.connect()
            complete = db.retrieve("portfolios").round(3).fillna(0).to_dict("records")
            db.disconnect()
        else:
            complete = []
    except Exception as e:
        complete = []
        print(str(e))
    return JsonResponse(complete,safe=False)

def recommendationsView(request):
    try:
        if request.method == "GET":
            db.connect()
            complete = db.retrieve("recommendations").round(3).fillna(0).to_dict("records")
            db.disconnect()
        else:
            complete = []
    except Exception as e:
        complete = []
        print(str(e))
    return JsonResponse(complete,safe=False)
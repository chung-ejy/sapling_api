from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from extractor.alp_extractor import ALPExtractor as alp

@csrf_exempt
def accountView(request):
    try:
        if request.method == "GET":
            account = alp.account()
            complete = {}
            for key in ["cash","portfolio_value","long_market_value","balance_asof"]:
                complete[key] = account[key]
        else:
            complete = {}
    except Exception as e:
        complete = {}
        print(str(e))
    return JsonResponse(complete,safe=False)

@csrf_exempt
def positionsView(request):
    try:
        if request.method == "GET":
            complete = alp.positions()
        else:
            complete = {}
    except Exception as e:
        complete = {}
        print(str(e))
    return JsonResponse(complete,safe=False)

@csrf_exempt
def historyView(request):
    try:
        if request.method == "GET":
            complete = alp.history()
        else:
            complete = {}
    except Exception as e:
        complete = {}
        print(str(e))
    return JsonResponse(complete,safe=False)

@csrf_exempt
def ordersView(request):
    try:
        if request.method == "GET":
            complete = alp.orders()
        else:
            complete = {}
    except Exception as e:
        complete = {}
        print(str(e))
    return JsonResponse(complete,safe=False)

@csrf_exempt
def closeView(request):
    try:
        if request.method == "GET":
            complete = alp.close()
        else:
            complete = {}
    except Exception as e:
        complete = {}
        print(str(e))
    return JsonResponse(complete,safe=False)
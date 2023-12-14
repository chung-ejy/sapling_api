import requests as r
import os
from dotenv import load_dotenv
load_dotenv()
paperkey = os.getenv("APCAPAPERKEY")
papersecret = os.getenv("APCAPAPERSECRET")
import pandas as pd
from datetime import datetime

class ALPExtractor(object):

    @classmethod
    def prices(self,ticker,start,end):
        headers = {
            'APCA-API-KEY-ID': paperkey,
            'APCA-API-SECRET-KEY': papersecret,
            'accept': 'application/json'
        }
        params = {
            "symbols":ticker,
            "adjustment":"raw",
            "timeframe":"1Day",
            "feed":"sip",
            "sort":"asc",
            "start":start.strftime("%Y-%m-%d"),
            "end":end.strftime("%Y-%m-%d")
        }
        url = "https://data.alpaca.markets/v2/stocks/bars"
        requestBody = r.get(url,params=params,headers=headers)
        data =  pd.DataFrame(requestBody.json()["bars"][ticker]).rename(columns={"c":"adjclose","t":"date"})[["date","adjclose"]]
        data["ticker"] = ticker
        return data
    
    @classmethod
    def account(self):
        headers = {
            'APCA-API-KEY-ID': paperkey,
            'APCA-API-SECRET-KEY': papersecret,
            'accept': 'application/json'
        }
        params = {}
        url = "https://paper-api.alpaca.markets/v2/account"
        requestBody = r.get(url,params=params,headers=headers)
        return requestBody.json()

    @classmethod
    def positions(self):
        headers = {
            'APCA-API-KEY-ID': paperkey,
            'APCA-API-SECRET-KEY': papersecret,
            'accept': 'application/json'
        }
        params = {}
        url = "https://paper-api.alpaca.markets/v2/positions"
        requestBody = r.get(url,params=params,headers=headers)
        return requestBody.json()

    @classmethod
    def orders(self):
        headers = {
            'APCA-API-KEY-ID': paperkey,
            'APCA-API-SECRET-KEY': papersecret,
            'accept': 'application/json'
        }
        params = {}
        url = "https://paper-api.alpaca.markets/v2/orders"
        requestBody = r.get(url,params=params,headers=headers)
        return requestBody.json()
    
    @classmethod
    def history(self):
        headers = {
            'APCA-API-KEY-ID': paperkey,
            'APCA-API-SECRET-KEY': papersecret,
            'accept': 'application/json'
        }
        params = {
            "period":"1A"
        }
        url = "https://paper-api.alpaca.markets/v2/account/portfolio/history"
        requestBody = r.get(url,params=params,headers=headers)
        df = pd.DataFrame(requestBody.json())
        df["date"] = [datetime.fromtimestamp(x) for x in df["timestamp"]]
        return df.to_dict("records")

    @classmethod
    def buy(self,ticker,qty):
        headers = {
            "APCA-API-KEY-ID":paperkey,
            "APCA-API-SECRET-KEY":papersecret,
            "accept": "application/json",
            "content-type": "application/json"
        }
        data = {
            "side": "buy",
            "type": "market",
            "time_in_force": "day",
            "symbol": ticker,
            "qty": qty
            }
        url = "https://paper-api.alpaca.markets/v2/orders"
        requestBody = r.post(url,json=data,headers=headers)
        return requestBody
        
    @classmethod
    def close(self):
        headers = {
            "APCA-API-KEY-ID":paperkey,
            "APCA-API-SECRET-KEY":papersecret,
            "accept":"application/json"
        }
        params = {}
        url = "https://paper-api.alpaca.markets/v2/positions?cancel_orders=true"
        requestBody = r.delete(url,params=params,headers=headers)
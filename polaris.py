# 프로젝트 폴라리스 - 추적 매매 시스템
import asyncio
import requests
import pandas as pd


def get_upbit_candles(market, interval, unit, count):
    url = f"https://api.upbit.com/v1/candles/{interval}/{unit}"
    params = {"market": market, "count": count}
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df["candle_date_time_kst"] = pd.to_datetime(df["candle_date_time_kst"])
        df = df[["candle_date_time_kst", "opening_price", "high_price", "low_price", "trade_price",
                 "candle_acc_trade_volume"]]
        df.columns = ["date", "open", "high", "low", "close", "volume"]
        df.set_index("date", inplace=True)
        return df
    else:
        print("Error:", response.status_code, response.text)
        return None



async def slot1_main():
    while True:
        slot1 = get_upbit_candles("KRW-ETH", "minutes", 5, 10)
        await asyncio.sleep(1)
        print('Slot1', slot1)

async def slot2_main():
    while True:
        slot2 = get_upbit_candles("KRW-XRP", "minutes", 5, 10)
        await asyncio.sleep(1.5)
        print('Slot2', slot2)

async def slot3_main():
    while True:
        slot3 = get_upbit_candles("KRW-SUI", "minutes", 5, 10)
        await asyncio.sleep(1.8)
        print('Slot3', slot3)

async def slot4_main():
    while True:
        slot4 = get_upbit_candles("KRW-CBK", "minutes", 5, 10)
        await asyncio.sleep(2)
        print('Slot4' , slot4)

async def main():
    asyncio.create_task(slot1_main())
    asyncio.create_task(slot2_main())
    asyncio.create_task(slot3_main())
    asyncio.create_task(slot4_main())
    while True:
        await asyncio.sleep(1)


asyncio.run(main())


import asyncio
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient


async def main():
    async def deal_msg(msg):
        print(msg)
        if msg['topic'] == '/spotMarket/level2Depth5:BTC-USDT':
            print(msg["data"])
        elif msg['topic'] == '/spotMarket/level2Depth5:KCS-USDT':
            print(f'Get KCS level3:{msg["data"]}')

    # is public
    client = WsToken()
    #is private
    # client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')
    # is sandbox
    # client = WsToken(is_sandbox=True)
    ws_client = await KucoinWsClient.create(None, client, deal_msg, private=False)
    await ws_client.subscribe('/market/snapshot:ALTS')
    # await ws_client.subscribe('/spotMarket/level2Depth5:BTC-USDT,KCS-USDT')
    while True:
        await asyncio.sleep(60, loop=loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
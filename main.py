from PyMemoryEditor import OpenProcess
import asyncio
import logging
import sys
from buttplug import Client, WebsocketConnector, ProtocolSpec

processName = "Celeste.exe"
address = 0x173369D7B80
vibrationDuaration = 0.5
vibrationStrong = 1


async def connect():
    client = Client("Plug", ProtocolSpec.v3)
    connector = WebsocketConnector("ws://127.0.0.1:12345", logger=client.logger)
    try:
        await client.connect(connector)
    except Exception as e:
        logging.error(f"Could not connect to server, exiting: {e}")
        return

    await client.start_scanning()
    await asyncio.sleep(1)
    await client.stop_scanning()
    client.logger.info(f"Devices: {client.devices}")
    return client

async def main():
    

    scriptCounter = 0
    gameCounter = 0
    client = await connect()
    device = client.devices[0]

    # On stock la value initale de mort
    with OpenProcess(process_name=processName) as process:
        gameCounter = process.read_process_memory(address, int, 4)
        scriptCounter = gameCounter
        print(f"Nombre de mort initiale : {scriptCounter}")

    async def coupDeJus():
        print("Mort")
        await device.actuators[0].command(vibrationStrong)
        await asyncio.sleep(vibrationDuaration)
        await device.actuators[0].command(0)

    time = 0
    while (True):
        if (time < 75):
            with OpenProcess(process_name=processName) as process:
                gameCounter = process.read_process_memory(address, int, 4)
                
                if (scriptCounter != gameCounter):
                    # Une mort en plus 
                    scriptCounter = gameCounter
                    await coupDeJus()
            time += 1
            print(time)
        else:
            print("reconnect")
            time = 0
            await connect()
        
            

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
asyncio.run(main(), debug=True)

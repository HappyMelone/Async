import asyncio

address=("127.0.0.1",6000)

async def main():
    reader,writer=await asyncio.open_connection(address[0],address[1])
    msg=input("Time (1) o Echo (2):\t")
    if msg=="1" or msg=="2":
        writer.write(msg.encode())
    await writer.drain()

if __name__=="__main__":
    asyncio.run(main())
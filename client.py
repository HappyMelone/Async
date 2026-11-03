import asyncio,sys

address=("127.0.0.1",6000)

async def main():
    reader,writer=await asyncio.open_connection(address[0],address[1])

    while 1:
        try:
            msg=input("Time (1) o Echo (2):\t")
            if msg=="1" or msg=="2":
                try:
                    writer.write(msg.encode())
                    await writer.drain()
                except BrokenPipeError:
                    break
                port=await reader.readline()
                if not port:
                    break
                reader2,writer2=await asyncio.open_connection(address[0],int(port.decode()))
                data=await reader2.readline()
                if not data:
                    break
                print(data.decode())
        except KeyboardInterrupt:
            break

    print("Chiusura")


if __name__=="__main__":
    asyncio.run(main())
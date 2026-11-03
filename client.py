import asyncio,sys,json

address=("127.0.0.1",6000)

async def main():
    reader,writer=await asyncio.open_connection(address[0],address[1])
    try:
        msg=input("Servizio:")
        msgJson={"cmd":"lookup","service":msg}
        try:
            writer.write(f"{json.dumps(msgJson)}\n".encode())
            await writer.drain()
        except BrokenPipeError:
            sys.exit(1)
        data=await reader.readline()
        if not data:
            sys.exit(1)
        print(data)
        reader2,writer2=await asyncio.open_connection(address[0],int(json.loads(data.decode())["port"]))
        data=await reader2.readline()
        if not data:
            sys.exit(1)
        print(data.decode())
    except KeyboardInterrupt:
        sys.exit(1)


if __name__=="__main__":
    asyncio.run(main())
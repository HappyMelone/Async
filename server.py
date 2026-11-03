import asyncio,json

class Broker:

    clients={}
    cmds={"time":6001,"echo":6002}
    
    async def run(self):
        main=await asyncio.start_server(self.gestisci_client,"127.0.0.1",6000)
        time=await asyncio.start_server(self.tempo,"127.0.0.1",6001)
        echo=await asyncio.start_server(self.eco,"127.0.0.1",6002)
        async with main:
            await main.serve_forever()
        async with time:
            await time.serve_forever()
        async with echo:
            await echo.serve_forever()

    async def gestisci_client(self,reader,writer):
        ip,pn=writer.get_extra_info("peername")
        print(f"Connesso: {ip}:{pn}")
        dati=await reader.readline()
        if not dati:
            print(f"Disconnesso: {ip}:{pn}")
            writer.close()
            await writer.wait_closed()
            return
        dati=dati.decode().rstrip("\n")
        print(dati)
        data=json.loads(dati)
        print(data)
        if data["service"] in self.__class__.cmds:
            msg={"status":"ok","service":data["service"],"host":"127.0.0.1","port":self.__class__.cmds[data["service"]]}
            writer.write(f"{json.dumps(msg)}\n".encode())
        else:
            msg={"status":"error","message":"Servizio non esistente"}
            writer.write(f"{json.dumps(msg)}\n".encode())

    async def tempo(self,reader,writer):
        ip,pn=writer.get_extra_info("peername")

    async def eco(self,reader,writer):
        ip,pn=writer.get_extra_info("peername")
    

if __name__ == "__main__":
    broker=Broker()
    asyncio.run(broker.run())
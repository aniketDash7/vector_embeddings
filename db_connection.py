from astrapy.db import AstraDB
db = AstraDB(
  token="AstraCS:EFZeGBuoIqufTGMaujDAxsbw:3fe0a3024e876145ee2540e2714b5f595b335301371f7c57a8c5332a98c751b2",
  api_endpoint="https://c96e0498-325a-4c33-b7c2-9e8bc1c4e33a-us-east1.apps.astra.datastax.com")

print(f"Connected to Astra DB: {db.get_collections()}")
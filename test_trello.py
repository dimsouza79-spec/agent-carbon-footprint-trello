from trello import TrelloClient

API_KEY = "cfff424f7478b396f39b79c19fb5c56b"
API_SECRET = "9e0fd41af7e147e8bb5b782b1527cf41b07c26bbae6493f194217a941e878c25"
TOKEN = "ATTAb6e5a8d661e0271a3e5df05be21980aadb12c927fb422f70a34d7dbf40c1733882273FDF"

print("A ligar ao Trello...")
client = TrelloClient(api_key=API_KEY, api_secret=API_SECRET, token=TOKEN)

boards = client.list_boards()
print(f"Sucesso! Encontrados {len(boards)} quadros.\n")

for board in boards:
    print(f"📌 Quadro: {board.name}")
    for lista in board.list_lists():
        print(f"  📂 Lista: {lista.name}")
        for card in lista.list_cards():
            print(f"     👉 Card: {card.name}")
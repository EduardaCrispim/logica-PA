catalogo = [
{"produto": "Mouse Pad", "preco": 35,00, "Em_estoque": True},
{"produto": "Headset", "preco": 180,00, "em_estoque": False}
]

for item in catalogo:
    print(f"item: {item['produto']} - R${item['preco']}") 

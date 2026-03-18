estoque = {}
print ("bem vindo ao sisitea de gestão de estoque desenvolvido por Igor Miguel")
while True:
    operacao = input ("deseja registrar a entrada e saída de produto? (digite 'entrada' ou 'saída') ou sair").lower()
    
    if operacao not in ['entrada', 'saída', 'sair']:
        print("operacao inválida.")
        continue
    if[# executar o bloco de código] operacao == 'sair':
        break # quebra a ação de repetição 
    produto = input("nome do produto: ").strip() # tem a função de limpar o bloco de códigos ()
    qtd = int(input("quntidade: " ))
    if operacao == 'entrada':
        estoque[produto] = estoque.get(produto, 0 ) + qtd
    elif operacao == 'saída':
        if estoque.get(produto, 0) >= qtd:
            estoque[produto] -= qtd
        else:
            print("Erro:produto inexistente ou estoque insufiente")
print("\n ---Estoque Final ---")
for p, q in estoque.items():
    print(f"{p}: {q}")
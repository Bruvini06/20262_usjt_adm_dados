situacao = lambda nota: "aprovado" if nota >= 70 else "reprovado"
print(situacao(85))
print(situacao(40))
# dobro = lambda x: x * 2
# print(dobro(5))


# def  dobro(x):
#     return 2 * x


# def resumo_vendas(valores, imposto=0.1):
#     total = sum(valores)
#     media = total / len(valores)
#     total_com_imposto = total * (1 + imposto)
#     return total, media, total_com_imposto
# t, m, ti = resumo_vendas([100, 200, 300], 0.15)
# print(f"Total: {t}, Média: {m:.2f}, Com imposto: {ti:.2f}")

# def teste(p=2):
#     print(p)
# teste()
# teste(3)


# # nomes = ["Maria", "João", "Ana"]
# for i, nome in enumerate(nomes):
#     print(i, nome)


# emails = ["ana@x.com", "joao.com", "maria@y.com", "pedro"]
# #Variavel contadora
# invalidos = 0
# for email in emails:
#     if "@" not in email: 
#         invalidos = invalidos + 1
#         print(f"Invalido: {email}")
# print(f"Total de invalidos: {invalidos}")


# #Estrutura de repetição
# precos = [19.9,  45, 12.5]
# total = 0 #acumulador
# for p in precos:
#     total = total + p 
# print(f"Total: R$ {total:.2f}")


# #Operador In
# ufs = ["SP"]
# validos = ["SP", "RJ", "MG", "PR", "RS"]
# if uf in validos:
#     print("UF reconhecida")
# else:
#     print("UF invalida")


# #If elif else
# valor = 250
# # se for pelo menos 500, é alto
# # se for pelo menos 100, é médio
# # caso contrario é baixo
# if valor >= 500:
#     faixa = "alto"
# elif valor >= 100:
#     faixa = "medio"
# else:
#     faixa = "baixo"

# print(f"Cliente de Ticket {faixa}")


# # Valores unicos usando conjuntos (sets)
# estados = ["SP", "RJ", "MG", "RJ", "SP"]
# print(set(estados))
# print(len(set(estados)))


# tabela = [
#     {"nome": "Maria", "saldo": 150},
#     {"nome": "João", "saldo": 200},
#     {"nome": "Ana", "saldo": 250}
# ]
# print(tabela[1]["nome"])

# # dicionario: coleção de pares chaves/valor
# cliente = {
#     "nome": "maria",
#     "idade": 34,
#     "cidade": "São Paulo"
# }
# print(cliente["cidade"])
# cliente ["email"] = "maria@email.com"
# for chave, valor in cliente.items():
#     print(chave, "->", valor)


# # list comprehensions ( Compreensão de lista)
# precos = [19.90, 45.00, 12.50, 89.90]
# # Calcular 10% a todos
# com_imposto = [p * 1.1 for p in precos]
# print(com_imposto)
# caros = [p for p in precos if p > 40]
# print(caros)


# # Listas
# precos = [19.90, 45.00, 12.50, 89.90]
# #Quantos
# print(len(precos)) #Length
# #Soma
# print(sum(precos))
# #MAior valor
# print(max(precos))
# #Adicionar valor
# precos.append(30.00) #Concatenar
# # Apenas os dois Ultimos
# print(precos [:2])


# valor_txt = " R$ 1.234,56 "
# limpo = valor_txt.replace("R$", "") .replace(".", ""). replace(",", ".").strip()
# valor = float(limpo)
# print(valor + 10)

# nome = "  Maria     SILVA     "
# limpo = nome.strip() .title() #Maria SIlva 
# print(limpo)
# print(limpo.split())
# print(" ".join(limpo.split()))


# indice e fatiamento   
# cpf = "12345678900"
# print(cpf[-2:])
# print(cpf[-1])
# print(cpf[0:3])
# print(cpf[0])
# print(cpf[10])

# f-string  
# nome = "Maria"  
# valor = 1234.50
# # Maria gastou R$1234.50
# print(f'{nome} gastou R${valor:.2f}')

# preco_textual = "19.90"
# preco = float(preco_textual)
# idade_textual = "18"
# idade = int(idade_textual)

# print (type("Maria"))
# nome = "Maria"
# sobrenome = 'Silva'
# idade = 34  
# ativo = True   
# altura= '180'
# print ( nome, sobrenome, idade, ativo, altura) 
# print(10 / 0)
# print('Olá, mundo dos dados')
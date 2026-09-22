import pandas as pd
df = pd.DataFrame({
    "cliente": ["Ana", "Bruno", "Carla", "Diego", "Ana"],
    "cidade": ["SP", "RJ", "SP", "MG", "SP"],
    "valor": [120.0, 80.0, 200.0, 50.0, 120.0]
})

# --- 14. Mostre as primeiras linhas e descubra quantas linhas e colunas o DataFrame tem. ---
print(df.head())
print("Formato (linhas, colunas):", df.shape)

# --- 15. Quantas vezes cada cidade aparece na coluna cidade? ---
print(df["cidade"].value_counts())

# --- 16. Filtre e mostre apenas os clientes com valor acima de 100. ---
print(df[df["valor"] > 100])

# --- 17. Remova as linhas duplicadas e diga quantas linhas sobraram. ---
df_sem_duplicadas = df.drop_duplicates()
print(df_sem_duplicadas)
print("Linhas que sobraram:", len(df_sem_duplicadas)) # ou df_sem_duplicadas.shape[0]

# --- 18. Calcule o ticket médio (média de valor) por cidade. ---
print(df.groupby("cidade")["valor"].mean())

# --- 19. Crie uma coluna faixa com 'alto' para valor >= 100 e 'baixo' caso contrário (use apply com lambda). ---
df["faixa"] = df["valor"].apply(lambda x: "alto" if x >= 100 else "baixo")
print(df[["cliente", "valor", "faixa"]])

# --- 20. Mostre as 2 maiores compras (Top-2 por valor). ---
print(df.sort_values(by="valor", ascending=False).head(2))

# --- 21. Junte (merge) o DataFrame de pedidos abaixo com o de clientes pela coluna id_cliente e calcule o total gasto por cliente: ---
pedidos = pd.DataFrame({"id_cliente": [1, 2, 1, 3], "valor": [100, 200, 50, 80]})
clientes = pd.DataFrame({"id_cliente": [1, 2, 3], "nome": ["Ana", "Bruno", "Carla"]})

# Fazendo o merge (join)
df_merged = pd.merge(pedidos, clientes, on="id_cliente")

# Calculando o total gasto por cliente (agrupando por nome ou id_cliente)
total_gasto = df_merged.groupby(["id_cliente", "nome"])["valor"].sum().reset_index()
print(total_gasto)
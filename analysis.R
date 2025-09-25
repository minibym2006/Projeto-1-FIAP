# Carrega dados de umidade (simulação)
# Estrutura esperada: umidade.csv com uma coluna chamada "umidade"
# Exemplo:
# umidade
# 55
# 62
# 58
# 40

dados <- read.csv("umidade.csv")

# Estatísticas básicas
media <- mean(dados$umidade)
desvio <- sd(dados$umidade)

cat("Média da umidade:", media, "\n")
cat("Desvio padrão:", desvio, "\n")

# Regra de irrigação (exemplo: soja)
if (media < 60) {
  cat("Decisão: Irrigar (umidade insuficiente)\n")
} else {
  cat("Decisão: Não irrigar (umidade adequada)\n")
}

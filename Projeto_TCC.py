def leia_float(prompt):
    """Lê um número que pode usar vírgula como separador e retorna float."""
    while True:
        s = input(prompt).strip() # strip() tira espaços em brancos, etc
        s = s.replace(".", "").replace(",", ".")  # aceita 1.234,56 ou 1234.56
        try:
            val = float(s) # Verifica se o número se encaixa
            return val
        except ValueError:
            print("Entrada inválida. Digite um número (ex.: 1234.56 ou 1.234,56).")

def leia_int(prompt):
    while True:
        s = input(prompt).strip()
        if s.isdigit(): # Verifica se o número é válido
            return int(s)
        print("Entrada inválida. Digite um número inteiro positivo.")

print("Você saberá quantos dias de trabalho você gastou em um produto.\n")

# Dados iniciais
jorn_trab = leia_int("Primeiramente, quantos dias você trabalha por semana? ")


while jorn_trab > 7:
    print("Você só pode trabalhar no máximo 7 dias em uma semana.")
    jorn_trab = leia_int("E por quantos dias você trabalha por semana? ")

h_trab = leia_float("E por quantas horas você trabalha por dia? ")

while h_trab <= 0:
    print("Horas por dia deve ser maior que zero.")
    h_trab = leia_float("E por quantas horas você trabalha por dia? ")

while h_trab > 12:
    print("Sua jornada de trabalho deve ser no máximo de 12 horas por dia.")
    h_trab = leia_float("E por quantas horas você trabalha por dia? ")


horas_mes = jorn_trab * h_trab * 4  # aproximação de 4 semanas/mes

# Saber se o usuário sabe quanto ganha por hora
perg = input("\nVocê sabe quanto você ganha por hora? (sim/não) ").strip().lower()
while perg not in ("sim", "não", "nao"):
    perg = input("Por favor responda 'sim' ou 'não': ").strip().lower()

# Calcula o salário por hora (aceita vírgulas)
if perg == "sim":
    sal_h = leia_float("\nQuanto você ganha por hora? R$ ")
else:
    sal_mensal = leia_float("\nQuanto você ganha por mês? R$ ")
    if horas_mes <= 0:
        print("Erro: cálculo de horas por mês inválido.")
        sal_h = 0.0
    else:
        sal_h = sal_mensal / horas_mes

print(f"\nVocê ganha R$ {sal_h:.2f} por hora.\n")

# Loop para testar novos produtos e opção de alterar dados
while True:
    preco = leia_float("Quanto custou o produto que você comprou? R$ ")

    if sal_h <= 0:
        print("Salário por hora inválido (<= 0). Não é possível calcular.")
    else:
        horas_necessarias = preco / sal_h
        dias_trabalho = horas_necessarias / h_trab          # dias de trabalho (com suas horas por dia)
        dias_24h = horas_necessarias / 24                  # dias de 24h (apenas para comparação)

        print(f"\n💰 Resultado:")
        print(f" - Horas de trabalho necessárias: {horas_necessarias:.2f} horas")
        print(f" - Dias de trabalho (com {h_trab:.2f} h/dia): {dias_trabalho:.2f} dias úteis de trabalho")
        print(f" - Dias de 24 horas (apenas referência): {dias_24h:.2f} dias\n")

    # perguntar se deseja testar outro produto
    repetir = input("Deseja testar outro produto? (sim/não) ").strip().lower()
    while repetir not in ("sim", "não", "nao"):
        repetir = input("Por favor responda 'sim' ou 'não': ").strip().lower()

    if repetir in ("não", "nao"):
        print("\nObrigado por usar o programa! 💼")
        break

    # se quiser, permitir trocar os dados base (salário/horas) antes de testar novo produto
    mudar = input("Deseja alterar salário/horas antes do próximo teste? (sim/não) ").strip().lower()
    while mudar not in ("sim", "não", "nao"):
        mudar = input("Por favor responda 'sim' ou 'não': ").strip().lower()

    if mudar in ("sim", "s"):
        # refazer opção de saber salário por hora
        perg = input("\nVocê sabe quanto você ganha por hora? (sim/não) ").strip().lower()
        while perg not in ("sim", "não", "nao"):
            perg = input("Por favor responda 'sim' ou 'não': ").strip().lower()

        if perg == "sim":
            sal_h = leia_float("Quanto você ganha por hora? R$ ")
        else:
            sal_mensal = leia_float("Quanto você ganha por mês? R$ ")
            sal_h = sal_mensal / horas_mes if horas_mes > 0 else 0.0

        # possivelmente alterar horas por dia / dias por semana
    alt_h = input("Deseja alterar dias/horas trabalhadas por semana/dia? (sim/não) ").strip().lower()
    while alt_h not in ("sim", "não", "nao"):
            alt_h = input("Por favor responda 'sim' ou 'não': ").strip().lower()

    if alt_h in ("sim", "s"):
            jorn_trab = leia_int("Quantos dias você trabalha por semana? ")
            while jorn_trab > 7:
                print("Você só pode trabalhar no máximo 7 dias em uma semana.")
                jorn_trab = leia_int("E por quantos dias você trabalha por semana? ")
            h_trab = leia_float("Quantas horas por dia? ")
            while h_trab <= 0:
                print("Horas por dia deve ser maior que zero.")
                h_trab = leia_float("Quantas horas por dia? ")
            while h_trab > 12:
                print("Sua jornada de trabalho deve ser no máximo de 12 horas por dia.")
                h_trab = leia_float("E por quantas horas você trabalha por dia? ")
            horas_mes = jorn_trab * h_trab * 4

    print()  # só uma linha em branco antes do próximo loop

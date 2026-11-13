# PROJECTO: SISTEMA DE FATURACAO DE UMA LOJA ALIMENTAR
# Linguagem: Python
# Autor: Zelec Nunes Ricardo
# =====================================================

clientes = []
contador = 0

print("=" * 55)
print(" SISTEMA DE FATURACAO - LOJA DE PRODUTOS ALIMENTARES")
print("=" * 55)

while True:
    print("\n--- REGISTO DE CLIENTE ---")

    nome = input("Nome do cliente: ").strip()

    while nome == "":
        print("O nome nao pode estar vazio.")
        nome = input("Nome do cliente: ").strip()

    genero = input("Genero (M/F): ").strip().upper()

    while genero not in ["M", "F"]:
        print("Opcao invalida. Introduza M ou F.")
        genero = input("Genero (M/F): ").strip().upper()

    # Validar idade
    while True:
        try:
            idade = int(input("Idade do cliente: "))
            if idade >= 0:
                break
            print("A idade nao pode ser negativa.")
        except ValueError:
            print("Introduza uma idade valida.")

    # Validar valor das compras
    while True:
        try:
            compras = float(input("Valor total das compras (Kz): "))
            if compras >= 0:
                break
            print("O valor nao pode ser negativo.")
        except ValueError:
            print("Introduza um valor numerico valido.")

    # Informacoes para prioridade
    if genero == "F":
        gravida = input("Esta gravida? (S/N): ").strip().upper()
        while gravida not in ["S", "N"]:
            gravida = input("Responda S ou N: ").strip().upper()
    else:
        gravida = "N"

    if idade >= 60:
        idoso = True
    else:
        idoso = False

    deficiencia = input(
        "Pessoa com deficiencia? (S/N): "
    ).strip().upper()

    while deficiencia not in ["S", "N"]:
        deficiencia = input("Responda S ou N: ").strip().upper()

    # Calculo do bonus comercial
    if compras > 100000:
        bonus = compras * 0.10
    else:
        bonus = 0

    total_pagar = compras - bonus

    # Verificacao da prioridade no atendimento
    prioridade = (
        gravida == "S"
        or idoso
        or deficiencia == "S"
    )

    contador += 1

    cliente = {
        "nome": nome,
        "genero": genero,
        "idade": idade,
        "compras": compras,
        "bonus": bonus,
        "total_pagar": total_pagar,
        "prioridade": prioridade,
        "ordem": contador
    }

    clientes.append(cliente)

    # Apresentacao da fatura
    print("\n" + "=" * 45)
    print("              FATURA DO CLIENTE")
    print("=" * 45)
    print("Cliente:", nome)
    print("Valor das compras: {:,.2f} Kz".format(compras))
    print("Bonus de 10%: {:,.2f} Kz".format(bonus))
    print("Total a pagar: {:,.2f} Kz".format(total_pagar))

    if prioridade:
        print("Atendimento: PRIORITARIO")
    else:
        print("Atendimento: NORMAL")

    print("=" * 45)

    continuar = input(
        "\nDeseja registar outro cliente? (S/N): "
    ).strip().upper()

    while continuar not in ["S", "N"]:
        continuar = input("Responda S ou N: ").strip().upper()

    if continuar == "N":
        break

# Organizar a fila: prioridade primeiro, respeitando
# a ordem de chegada dentro de cada grupo.
fila = sorted(
    clientes,
    key=lambda c: (not c["prioridade"], c["ordem"])
)

print("\n" + "=" * 55)
print("          FILA DE ATENDIMENTO")
print("=" * 55)

for posicao, cliente in enumerate(fila, start=1):
    if cliente["prioridade"]:
        estado = "PRIORITARIO"
    else:
        estado = "NORMAL"

    print(
        "{}. {} - {}".format(
            posicao, cliente["nome"], estado
        )
    )

print("\n" + "=" * 55)
print("             RESUMO DO SISTEMA")
print("=" * 55)

total_vendas = sum(c["compras"] for c in clientes)
total_bonus = sum(c["bonus"] for c in clientes)
total_receber = sum(c["total_pagar"] for c in clientes)
total_prioritarios = sum(
    1 for c in clientes if c["prioridade"]
)

print("Total de clientes:", len(clientes))
print("Clientes prioritarios:", total_prioritarios)
print("Valor bruto das vendas: {:,.2f} Kz".format(total_vendas))
print("Total de bonus: {:,.2f} Kz".format(total_bonus))
print("Total a receber: {:,.2f} Kz".format(total_receber))

print("\nSistema encerrado com sucesso!")
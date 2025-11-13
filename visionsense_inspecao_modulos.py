import os

# Sistema de inspeção de módulos de visão computacional para robôs - VisionSense

pecas = []  # lista de dicionários: cada peça é um módulo de visão


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def avaliar_peca(peso, cor, comprimento):
    motivos = []
    if not (95 <= peso <= 105):
        motivos.append("Peso fora do intervalo (95g a 105g)")
    if cor.lower() not in ("azul", "verde"):
        motivos.append("Cor inválida (somente azul ou verde)")
    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora do intervalo (10cm a 20cm)")
    return (len(motivos) == 0), motivos


def cadastrar_peca():
    print("=== CADASTRAR NOVA PEÇA ===")
    id_peca = input("ID da peça: ").strip()
    if not id_peca:
        print("Erro: o ID não pode ser vazio.")
        return
    if any(p["id"] == id_peca for p in pecas):
        print("Erro: já existe uma peça com esse ID.")
        return
    try:
        peso = float(input("Peso (g): ").strip().replace(",", "."))
        comprimento = float(input("Comprimento (cm): ").strip().replace(",", "."))
    except ValueError:
        print("Erro: peso e comprimento devem ser numéricos.")
        return
    cor = input("Cor da carcaça (azul/verde): ").strip().lower()

    aprovada, motivos = avaliar_peca(peso, cor, comprimento)
    status = "aprovada" if aprovada else "reprovada"
    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status,
        "motivos_reprovação": motivos,
    }
    pecas.append(peca)

    if status == "aprovada":
        print("Peça APROVADA.")
    else:
        print("Peça REPROVADA. Motivos:")
        for m in motivos:
            print(f"- {m}")


def listar_pecas():
    if not pecas:
        print("Nenhuma peça cadastrada.")
        return

    aprovadas = [p for p in pecas if p["status"] == "aprovada"]
    reprovadas = [p for p in pecas if p["status"] == "reprovada"]

    print("=== PEÇAS APROVADAS ===")
    if not aprovadas:
        print("Nenhuma.")
    else:
        for p in aprovadas:
            print(
                f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | "
                f"Comprimento: {p['comprimento']}cm"
            )

    print("\n=== PEÇAS REPROVADAS ===")
    if not reprovadas:
        print("Nenhuma.")
    else:
        for p in reprovadas:
            print(
                f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | "
                f"Comprimento: {p['comprimento']}cm"
            )
            print("  Motivos:")
            for m in p["motivos_reprovação"]:
                print(f"   - {m}")


def remover_peca():
    if not pecas:
        print("Não há peças para remover.")
        return
    print("=== REMOVER PEÇA ===")
    id_peca = input("ID da peça: ").strip()
    for i, p in enumerate(pecas):
        if p["id"] == id_peca:
            del pecas[i]
            print(f"Peça '{id_peca}' removida.")
            return
    print("Peça não encontrada.")


def obter_pecas_aprovadas():
    return [p for p in pecas if p["status"] == "aprovada"]


def montar_caixas(pecas_aprovadas, capacidade=10):
    caixas = []
    for i in range(0, len(pecas_aprovadas), capacidade):
        caixas.append(pecas_aprovadas[i : i + capacidade])
    return caixas


def listar_caixas_fechadas():
    print("=== CAIXAS FECHADAS ===")
    aprovadas = obter_pecas_aprovadas()
    if not aprovadas:
        print("Nenhuma peça aprovada, nenhuma caixa criada.")
        return

    caixas = montar_caixas(aprovadas)
    fechadas = [c for c in caixas if len(c) == 10]
    abertas = [c for c in caixas if len(c) < 10]

    if not fechadas:
        print("Ainda não há caixas fechadas (10 peças).")
    else:
        for idx, caixa in enumerate(fechadas, start=1):
            print(f"\nCaixa {idx} - {len(caixa)} peças")
            for p in caixa:
                print(
                    f"  ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | "
                    f"Comprimento: {p['comprimento']}cm"
                )

    if abertas:
        ultima = abertas[-1]
        print(f"\nCaixa em abertura com {len(ultima)} peça(s).")


def gerar_relatório_final():
    print("=== RELATÓRIO FINAL VisionSense ===")
    total = len(pecas)
    aprovadas = obter_pecas_aprovadas()
    reprovadas = [p for p in pecas if p["status"] == "reprovada"]

    caixas = montar_caixas(aprovadas)
    qtd_caixas = len(caixas)
    fechadas = sum(1 for c in caixas if len(c) == 10)
    abertas = qtd_caixas - fechadas

    print(f"Total de peças cadastradas: {total}")
    print(f"Total aprovadas: {len(aprovadas)}")
    print(f"Total reprovadas: {len(reprovadas)}")

    print("\nMotivos de reprovação:")
    if not reprovadas:
        print("Nenhuma peça reprovada.")
    else:
        contagem = {}
        for p in reprovadas:
            for m in p["motivos_reprovação"]:
                contagem[m] = contagem.get(m, 0) + 1
        for motivo, qtd in contagem.items():
            print(f"- {motivo}: {qtd} peça(s)")

    print(f"\nQuantidade de caixas usadas: {qtd_caixas}")
    print(f"  Caixas fechadas: {fechadas}")
    print(f"  Caixas em abertura: {abertas}")


def main():
    while True:
        limpar_tela()
        print("=== SISTEMA VisionSense - INSPEÇÃO DE MÓDULOS ===")
        print("1. Cadastrar nova peça")
        print("2. Listar peças aprovadas/reprovadas")
        print("3. Remover peça cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatório final")
        print("0. Sair")
        opção = input("Opção: ").strip()

        if opção == "0":
            limpar_tela()
            print("Encerrando o sistema VisionSense.")
            break

        limpar_tela()

        if opção == "1":
            cadastrar_peca()
        elif opção == "2":
            listar_pecas()
        elif opção == "3":
            remover_peca()
        elif opção == "4":
            listar_caixas_fechadas()
        elif opção == "5":
            gerar_relatório_final()
        else:
            print("Opção inválida.")

        input("\nPressione Enter para voltar ao menu...")


if __name__ == "__main__":
    main()

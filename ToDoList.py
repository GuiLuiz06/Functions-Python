lista_tarefas = []
lista_status = [] ## True == "Concluído", False == "Pendente"

def to_do_list():
    while True:
        print("\n--Menu--lista--de--tarefas--")
        print("1. Adicionar uma nova tarefa")
        print("2. Visualizar status e tarefas")
        print("3. Marcar uma tarefa como concluída")
        print("4. Remover uma tarefa")
        print("5. Sair")

        escolha_user = str(input("Digite o número para onde você deseja ir: "))

        if escolha_user == "1":
            tarefa = str(input("Adicione a tarefa desejada: "))

            tarefas_min = [t.lower() for t in lista_tarefas]

            if tarefa.lower() in tarefas_min:
                print("Esta tarefa já existe na sua lista. Tente adicionar outra tarefa.")
                continue

            lista_tarefas.append(tarefa)
            lista_status.append(False)
            print(f"Tarefa {tarefa} adicionada com sucesso!")

        if escolha_user == "2":
            if not lista_tarefas:
                print("Não existe tarefas na lista.")
                continue
            else:
                for i, tarefa in enumerate(lista_tarefas):
                    Status = "Concluída" if lista_status[i] else "Pendente"
                    print(f"[{i + 1}] {tarefa} ({Status})")

        if escolha_user == "3":
            if not lista_tarefas:
                print("Não há tarefas para marcar")
                continue

            for i, tarefa in enumerate(lista_tarefas):
                Status = "Concluída" if lista_status[i] else "Pendente"
                print(f"[{i + 1}] {tarefa} ({Status})")

            try:
                marcar_num = int(input("Digite o número da tarefa para marcar ela como conluída: "))
                indice = marcar_num - 1

                if 0 <= indice < len(lista_tarefas):
                    lista_status[indice] = True
                    print(f"Tarefa {tarefa} marcada como concluída com sucesso!")
                else:
                    print("Número de tarefa inválido.")
            except ValueError:
                print("Entrada errada. Insira um número válido.")

        if escolha_user == "4":
            if not lista_tarefas:
                print("Não há tarefas para remover.")
                continue

            print("\n------ Remover tarefa -------")
            for i, tarefa in enumerate(lista_tarefas):
                Status = "Concluída" if lista_status[i] else "Pendente"
                print(f"[{i + 1}] {tarefa} ({Status})")
            print("------------------------------")

            try:
                remover_num = int(input("Digite o número da tarefa para remover ela: "))
                indice = remover_num - 1
                if 0 <= indice < len(lista_tarefas):
                    removed_tarefa = lista_tarefas.pop(indice)
                    lista_status.pop(indice)
                    print(f"Tarefa {tarefa} removida com sucesso!")
                else:
                    print("Número não encontrado!")

            except ValueError:
                print("Entrada errada. Insira um número válido")
        elif escolha_user == "5":
            print("Saindo do programa...")
            break
        elif escolha_user > "5":
            print("Entrada errada. Digite um número de 1 a 5.")


if __name__ == "__main__":
    to_do_list()
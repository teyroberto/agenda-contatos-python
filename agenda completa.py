#Crie a classe Contato com:
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

    def formatar(self):
        return f"{self.nome} | {self.telefone} | {self.email}"
    
#Crie a classe Agenda com:
class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar(self, contato):
        self.contatos.append(contato)

    def buscar(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def excluir(self, nome):
        contato = self.buscar(nome)
        if contato:
            self.contatos.remove(contato)
            return True
        return False

    def listar(self):
        return [str(contato) for contato in self.contatos]

    def salvar(self, arquivo):
        with open(arquivo, 'w') as f:
            for contato in self.contatos:
                f.write(contato.formatar() + '\n')

    def carregar(self, arquivo):
        self.contatos.clear()
        with open(arquivo, 'r') as f:
            for linha in f:
                nome, telefone, email = linha.strip().split(' | ')
                self.adicionar(Contato(nome, telefone, email))


def main():
    agenda = Agenda()
    arquivo = 'contatos.txt'
    
    try:
        agenda.carregar(arquivo)
    except FileNotFoundError:
        pass  # Se o arquivo não existir, continue com a agenda vazia

    while True:
        print("\nMenu:")
        print("1. Listar contatos")
        print("2. Adicionar contato")
        print("3. Buscar contato")
        print("4. Excluir contato")
        print("5. Salvar e sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            contatos = agenda.listar()
            if contatos:
                for contato in contatos:
                    print(contato)
            else:
                print("Nenhum contato na agenda.")
        
        elif escolha == '2':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            agenda.adicionar(Contato(nome, telefone, email))
            print("Contato adicionado.")
        
        elif escolha == '3':
            nome = input("Nome do contato a buscar: ")
            contato = agenda.buscar(nome)
            if contato:
                print(contato)
            else:
                print("Contato não encontrado.")
        
        elif escolha == '4':
            nome = input("Nome do contato a excluir: ")
            if agenda.excluir(nome):
                print("Contato excluído.")
            else:
                print("Contato não encontrado.")
        
        elif escolha == '5':
            agenda.salvar(arquivo)
            print("Contatos salvos. Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()
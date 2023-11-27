from diretor import Diretor
from genero import Genero
from exibicao import Exibicao
from filme import Filme
from horario import Horario
from premiacao import Premiacao
from sala import Sala
from indicacao_premiacao import Indicacao_premiacao
from connection import Connection
from tabulate import tabulate

if __name__ == "__main__":
    connection = Connection()
    connection.create_schema("cinema")

    diretor = Diretor()
    diretor.drop_table()
    diretor.create_table()
    diretor.insert("Christopher Nolan", 51)
    diretor.insert("Quentin Tarantino", 59)
    diretor.insert("Greta Gerwig", 38)
    diretor.insert("Denis Villeneuve", 53)
    diretor.insert("Ava DuVernay", 49)
    diretor.insert("Steven Spielberg", 75)
    diretor.insert("Martin Scorsese", 79)
    diretor.insert("Kathryn Bigelow", 70)
    diretor.insert("Jordan Peele", 42)
    diretor.insert("Bong Joon-ho", 51)


    genero = Genero()
    genero.drop_table()
    genero.create_table()
    genero.insert("Terror")
    genero.insert("Ação")
    genero.insert("Romance")
    genero.insert("Drama")
    genero.insert("Comédia")
    genero.insert("Ficção Científica")
    genero.insert("Animação")
    genero.insert("Suspense")
    genero.insert("Aventura")
    genero.insert("Fantasia")

    filme = Filme()
    filme.drop_table()
    filme.create_table()
    filme.insert("Inception", "2010", "Em Inception, um ladrão especializado em extrair segredos corporativos deixa de roubar informações e passa a implantá-las na mente de suas vítimas. O filme explora a complexidade dos sonhos e da realidade.", 1, 3)
    filme.insert("Pulp Fiction", "1994", "Pulp Fiction, dirigido por Quentin Tarantino, entrelaça várias histórias em Los Angeles, apresentando personagens memoráveis e eventos não lineares. Violento, irônico e cheio de diálogos marcantes.", 2, 2)
    filme.insert("Lady Bird", "2017", "Lady Bird é uma comédia dramática que segue a vida de uma adolescente rebelde em seu último ano de ensino médio. O filme aborda temas de identidade, família e amizade.", 3, 1)
    filme.insert("The Dark Knight", "2008", "Em The Dark Knight, o Cavaleiro das Trevas enfrenta seu maior desafio quando um criminoso brilhante, o Coringa, aterroriza Gotham. Uma mistura intensa de ação e drama.", 1, 4)
    filme.insert("The Shawshank Redemption", "1994", "The Shawshank Redemption segue a história de um homem inocente condenado à prisão perpétua e sua busca por redenção. Um poderoso drama que transcende a barreira da prisão.", 2, 5)
    filme.insert("La La Land", "2016", "La La Land é um musical romântico que narra a história de dois artistas em Los Angeles, explorando os altos e baixos de seus relacionamentos e aspirações artísticas.", 3, 6)
    filme.insert("Blade Runner 2049", "2017", "Blade Runner 2049 é uma jornada futurista que segue um novo blade runner em busca de respostas. Uma mistura envolvente de ficção científica e drama.", 4, 3)
    filme.insert("Get Out", "2017", "Get Out é um thriller psicológico que aborda questões de racismo ao seguir um homem negro que descobre segredos perturbadores durante uma visita à casa de sua namorada branca.", 5, 7)
    filme.insert("Parasite", "2019", "Parasite é uma comédia dramática que explora as disparidades sociais na Coreia do Sul através da história de uma família pobre que se infiltra na vida de uma família rica.", 6, 8)
    filme.insert("Interstellar", "2014", "Em Interstellar, a humanidade busca um novo lar em meio a uma Terra moribunda. Uma jornada épica que combina ficção científica e drama em uma busca desesperada pela sobrevivência.", 8, 10)


    premiacao = Premiacao()
    premiacao.drop_table()
    premiacao.create_table()
    premiacao.insert("Globo de ouro", "2015")
    premiacao.insert("Critics Choice Awards", "2018")
    premiacao.insert("Producers Guild Awards", "2020")
    premiacao.insert("Screen Actors Guild Awards", "2017")
    premiacao.insert("Writers Guild Awards", "2019")
    premiacao.insert("Directors Guild Awards", "2014")
    premiacao.insert("Academy Awards", "2016")
    premiacao.insert("BAFTA Awards", "2019")
    premiacao.insert("Golden Raspberry Awards", "2013")
    premiacao.insert("Cannes Film Festival", "2017")


    indicacao_premiacao = Indicacao_premiacao()
    indicacao_premiacao.drop_table()
    indicacao_premiacao.create_table()
    # # id_filme, id_premiacao, ganhou
    indicacao_premiacao.insert(2, 3, True)
    indicacao_premiacao.insert(2, 1, False)
    indicacao_premiacao.insert(5, 2, True)
    indicacao_premiacao.insert(3, 4, False)
    indicacao_premiacao.insert(6, 5, True)
    indicacao_premiacao.insert(2, 6, False)
    indicacao_premiacao.insert(1, 7, True)
    indicacao_premiacao.insert(4, 8, False)
    indicacao_premiacao.insert(5, 9, True)
    indicacao_premiacao.insert(3, 10, False)
    indicacao_premiacao.insert(1, 1, False)


    sala = Sala()
    sala.drop_table()
    sala.create_table()
    sala.insert("Sala Premiere", 50)
    sala.insert("Sala VIP Luxe", 60)
    sala.insert("MegaCine Deluxe", 40)
    sala.insert("Cinépolis Lounge", 80)
    sala.insert("The Grand Theater", 55)
    sala.insert("CineMax Elite", 70)
    sala.insert("Velvet Screen", 45)
    sala.insert("Golden Theater Experience", 65)
    sala.insert("Platinum Cinema Haven", 30)
    sala.insert("Royal Cinématique", 75)

    horario = Horario()
    horario.drop_table()
    horario.create_table()
    horario.insert("10:00:00")
    horario.insert("12:30:00")
    horario.insert("15:15:00")
    horario.insert("18:00:00")
    horario.insert("20:45:00")
    horario.insert("14:20:00")
    horario.insert("17:30:00")
    horario.insert("19:55:00")
    horario.insert("21:40:00")
    horario.insert("23:15:00")


    exibicao = Exibicao()
    exibicao.drop_table()
    exibicao.create_table()
    # # id_filme, id_sala, id_horario, data
    exibicao.insert(1, 1, 1, '2023-11-22')
    exibicao.insert(2, 1, 3, '2023-11-23')
    exibicao.insert(3, 3, 5, '2023-11-24')
    exibicao.insert(4, 4, 7, '2023-11-25')
    exibicao.insert(5, 4, 9, '2023-11-26')
    exibicao.insert(6, 4, 2, '2023-11-27')
    exibicao.insert(7, 7, 4, '2023-11-28')
    exibicao.insert(8, 9, 6, '2023-11-29')
    exibicao.insert(9, 9, 8, '2023-11-30')
    exibicao.insert(10, 10, 10, '2023-12-01')


    while True:
        print("+----------------------------+")
        print("|       MENU CINEMA          |")
        print("+----------------------------+")
        print("|  1 - Diretor               |")
        print("|  2 - Gênero                |")
        print("|  3 - Filme                 |")
        print("|  4 - Premiação             |")
        print("|  5 - Indicação a premiação |")
        print("|  6 - Sala                  |")
        print("|  7 - Horário               |")
        print("|  8 - Exibição              |")
        print("|  9 - Consultas SQL         |")
        print("| 10 - Sair                  |")
        print("+----------------------------+")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                print("\n+-------- MENU DIRETOR ---------+")
                print("| 1 - Inserir Diretor           |")
                print("| 2 - Deletar Diretor           |")
                print("| 3 - Atualizar Diretor         |")
                print("| 4 - Buscar Diretor por ID     |")
                print("| 5 - Listar Todos os Diretores |")
                print("| 6 - Voltar                    |")
                print("+-------------------------------+")


                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome_diretor = input("Digite o nome do diretor: ")
                    idade_diretor = input("Digite a idade do diretor: ")
                    diretor.insert(nome_diretor, idade_diretor)

                elif escolha == "2":
                    if(diretor.get_all()):
                        print()
                        diretor.print()    
                        print()
                        id_diretor = input("Digite o ID do diretor a ser deletado: ")
                        diretor.delete(id_diretor)

                elif escolha == "3":
                    if(diretor.get_all()):
                        print()
                        diretor.print()
                        print()
                        id_diretor = input("Digite o ID do diretor a ser atualizado: ")
                        nome_diretor = input("Digite o novo nome do diretor: ")
                        idade_diretor = input("Digite a nova idade do diretor: ")
                        diretor.update(id_diretor, nome_diretor, idade_diretor)

                elif escolha == "4":
                    id_diretor = input("Digite o ID do diretor a ser buscado: ")
                    d = diretor.get_by_id(id_diretor)
                    if d:
                        print()
                        headers = ["ID", "Nome", "Idade"]
                        rows_diretor = [[d[0][0], d[0][1], d[0][2]]]
                        print(tabulate(rows_diretor, headers=headers, tablefmt="fancy_grid", maxcolwidths=20))
                    
                elif escolha == "5":
                    if(diretor.get_all()):
                        print()
                        diretor.print()
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "2":
            while True:
                print("\n+-------- MENU GÊNERO ----------+")
                print("| 1 - Inserir Gênero            |")
                print("| 2 - Deletar Gênero            |")
                print("| 3 - Atualizar Gênero          |")
                print("| 4 - Buscar Gênero por ID      |")
                print("| 5 - Listar Todos os Gêneros   |")
                print("| 6 - Voltar                    |")
                print("+-------------------------------+")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome_genero = input("Digite o nome do gênero: ")
                    genero.insert(nome_genero)

                elif escolha == "2":
                    if(genero.get_all()):
                        print()
                        genero.print()
                        print()     
                        id_genero = input("Digite o ID do gênero a ser deletado: ")
                        genero.delete(id_genero)

                elif escolha == "3":
                    if(genero.get_all()):
                        print()
                        genero.print()
                        print()
                        id_genero = input("Digite o ID do gênero a ser atualizado: ")
                        nome_genero = input("Digite o novo nome do gênero: ")
                        genero.update(id_genero, nome_genero)

                elif escolha == "4":
                    id_genero = input("Digite o ID do gênero a ser buscado: ")
                    g = genero.get_by_id(id_genero)
                    if g:
                        print()
                        headers = ["ID", "Nome"]
                        row = [[g[0][0], g[0][1]]]
                        print(tabulate(row, headers=headers, tablefmt="fancy_grid", maxcolwidths=20))
    
                elif escolha == "5":
                    if(genero.get_all()):
                        print()
                        genero.print()
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "3":
            while True:
                print("\n+-------- MENU FILME ----------+")
                print("| 1 - Inserir Filme            |")
                print("| 2 - Deletar Filme            |")
                print("| 3 - Atualizar Filme          |")
                print("| 4 - Buscar Filme por ID      |")
                print("| 5 - Listar Todos os Filmes   |")
                print("| 6 - Voltar                   |")
                print("+------------------------------+")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    if diretor.get_all():
                        if genero.get_all():
                            nome_filme = input("Digite o nome do filme: ")
                            ano_lancamento = input("Digite o ano de lançamento do filme: ")
                            sinopse = input("Digite a sinopse do filme: ")
                            print()
                            diretor.print()
                            print()
                            id_diretor = input("Digite o ID do diretor: ")
                            print()
                            genero.print()
                            print()
                            id_genero = input("Digite o ID do gênero: ")
                            filme.insert(nome_filme, ano_lancamento, sinopse, int(id_diretor), int(id_genero))
                        else:
                            print("Não existem gêneros cadastrados para inserir o filme")
                    else:
                        print("Não existem diretores cadastrados para inserir o filme")

                elif escolha == "2":
                    if(filme.get_all()):
                        print()
                        filme.print(diretor, genero)
                        print()
                        id_filme = input("Digite o ID do filme a ser deletado: ")
                        filme.delete(id_filme)

                elif escolha == "3":
                    if(filme.get_all()):
                        print()
                        filme.print(diretor, genero)
                        print()
                        id_filme = input("Digite ID do filme a ser atualizado: ")
                        nome_filme = input("Digite o nome do filme: ")
                        ano_lancamento = input("Digite o ano de lançamento do filme: ")
                        sinopse = input("Digite a sinopse do filme: ")
                        print()
                        diretor.print()
                        print()
                        id_diretor = input("Digite o ID do diretor: ")
                        print()
                        genero.print()
                        print()
                        id_genero = input("Digite o ID do gênero: ")
                        filme.update(id_filme, nome_filme, ano_lancamento, sinopse, id_diretor, id_genero)

                elif escolha == "4":
                    id_filme = input("Digite o ID do filme a ser buscado: ")
                    f = filme.get_by_id(id_filme)
                    if f:
                        sql = f"""SELECT nome FROM cinema.diretor WHERE id = {f[0][4]}"""
                        sql_diretor = diretor.query(sql)
                        sql = f"""SELECT nome FROM cinema.genero WHERE id = {f[0][5]}"""
                        sql_genero = genero.query(sql)
                        print()
                        headers = ["ID", "Nome", "Ano", "Sinopse", "Diretor", "Gênero"]
                        row = [[f[0][0], f[0][1], f[0][2], f[0][3], sql_diretor[0][0], sql_genero[0][0]]]
                        print(tabulate(row, headers=headers, tablefmt="fancy_grid", maxcolwidths=20))
    
                elif escolha == "5":
                    if(filme.get_all()):
                        print()
                        filme.print(diretor, genero)
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "4":
            while True:
                print("\n+-------- MENU PREMIAÇÃO --------+")
                print("| 1 - Inserir Premiação          |")
                print("| 2 - Deletar Premiação          |")
                print("| 3 - Atualizar Premiação        |")
                print("| 4 - Buscar Premiação por ID    |")
                print("| 5 - Listar Todas as Premiações |")
                print("| 6 - Voltar                     |")
                print("+--------------------------------+")
               
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome_premiacao = input("Digite o nome da premiação: ")
                    ano_premiacao = input("Digite o ano da premiação: ")
                    premiacao.insert(nome_premiacao, ano_premiacao)

                elif escolha == "2":
                    if(premiacao.get_all()):
                        print()
                        premiacao.print()
                        print()
                        id_prem = input("Digite o ID da premiação a ser deletada: ")
                        premiacao.delete(id_prem)

                elif escolha == "3":
                    if(premiacao.get_all()):
                        print()
                        premiacao.print()
                        print()
                        id_premiacao = input("Digite o ID da premiação a ser atualizada: ")
                        nome_premiacao = input("Digite o novo nome da premiação: ")
                        ano_premiacao = input("Digite o novo ano da premiação: ")
                        premiacao.update(id_premiacao, nome_premiacao, ano_premiacao)

                elif escolha == "4":
                    id_prem = input("Digite o ID da premiação a ser buscada: ")
                    p = premiacao.get_by_id(id_prem)
                    if p:
                        print()
                        headers = ["ID", "Nome", "Ano"]
                        row = [[p[0][0], p[0][1], p[0][2]]]
                        print(tabulate(row, headers=headers, tablefmt="fancy_grid", maxcolwidths=20))
    
                elif escolha == "5":
                    if(premiacao.get_all()):
                        print()
                        premiacao.print()
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "5":
             while True:
                print("\n+------ MENU INDICAÇÃO A PREMIAÇÃO -------+")
                print("| 1 - Inserir Indicação                   |")
                print("| 2 - Deletar Indicação                   |")
                print("| 3 - Atualizar Indicação                 |")
                print("| 4 - Buscar Indicação por ID             |")
                print("| 5 - Listar Todas as Indicações          |")
                print("| 6 - Voltar                              |")
                print("+-----------------------------------------+")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    print()
                    filme.print(diretor, genero)
                    print()
                    id_filme = input("Digite o ID do filme: ")
                    print()
                    premiacao.print()
                    print()
                    id_premiacao= input("Digite o ID da premiação: ")
                    ganhou = input("O filme ganhou a premiação? (True ou False): ")
                    indicacao_premiacao.insert(int(id_filme), int(id_premiacao), bool(ganhou))

                elif escolha == "2":
                    if(indicacao_premiacao.get_all()):
                        print()
                        indicacao_premiacao.print(filme, sala)
                        print()
                        filme.print(diretor, genero)
                        print()  
                        id_filme = input("Digite o ID do filme a ser deletado: ")
                        print()
                        premiacao.print()
                        print()
                        id_premiacao = input("Digite o ID da premiação a ser deletada: ")
                        print()
                        indicacao_premiacao.delete((int(id_filme), int(id_premiacao)))

                elif escolha == "3":
                    if(indicacao_premiacao.get_all()):
                        print()
                        indicacao_premiacao.print(filme, sala)
                        print()
                        filme.print(diretor, genero)
                        print()  
                        id_filme = input("Digite o ID do filme a ser atualizado: ")
                        print()
                        premiacao.print()
                        print()
                        id_premiacao = input("Digite o ID da premiação a ser atualizada: ")
                        print()
                        ganhou = input("O filme ganhou a premiação? (True ou False): ")
                        indicacao_premiacao.update((int(id_filme), int(id_premiacao)), ganhou)

                elif escolha == "4":
                    id_premi = input("Digite o ID da premiação a ser buscada (id_filme,id_premiacao): ")
                    id_premi = tuple(map(int, id_premi.split(',')))
                    i = indicacao_premiacao.get_by_id(id_premi)
                    if i:
                        print()
                        sql = f"""SELECT nome FROM cinema.filme WHERE id = {i[0][0]}"""
                        sql_filme = filme.query(sql)
                        sql = f"""SELECT nome FROM cinema.premiacao WHERE id = {i[0][1]}"""
                        sql_premiacao = sala.query(sql)

                        if i[0][2] == True:
                            ganhou = "Ganhou"
                        else:
                            ganhou = "Perdeu"
            
                        headers = ["Filme", "Premiação", "Ganhou?"]
                        row = [[sql_filme[0][0], sql_premiacao[0][0], ganhou]]
                        print(tabulate(row, headers=headers, tablefmt="fancy_grid", maxcolwidths=20))
    
    
                elif escolha == "5":
                    if(indicacao_premiacao.get_all()):
                        print()
                        indicacao_premiacao.print(filme, sala)
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "6":
            while True:
                print("\n+-------- MENU SALA ------------+")
                print("| 1 - Inserir Sala              |")
                print("| 2 - Deletar Sala              |")
                print("| 3 - Atualizar Sala            |")
                print("| 4 - Buscar Sala por ID        |")
                print("| 5 - Listar Todos as Salas     |")
                print("| 6 - Voltar                    |")
                print("+-------------------------------+")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome_sala = input("Digite o nome da sala: ")
                    capacidade_sala = input("Digite a capacidade da sala: ")
                    sala.insert(nome_sala, capacidade_sala)

                elif escolha == "2":
                    if(sala.get_all()):
                        print()
                        sala.print()
                        print()     
                        id_sala = input("Digite o ID da sala a ser deletado: ")
                        sala.delete(id_sala)

                elif escolha == "3":
                    if(sala.get_all()):
                        print()
                        sala.print()
                        print()
                        id_sala = input("Digite o ID da sala a ser atualizada: ")
                        nome_sala = input("Digite o novo nome da sala: ")
                        capacidade_sala = input("Digite a nova capacidade da sala: ")
                        sala.update(id_sala, nome_sala, capacidade_sala)

                elif escolha == "4":
                    id_sala = input("Digite o ID da sala a ser buscada: ")
                    s = sala.get_by_id(id_sala)
                    if s:
                        print()
                        headers = ["ID", "Nome", "Capacidade"]
                        row = [[s[0][0], s[0][1], s[0][2]]]
                        print(tabulate(row, headers=headers, tablefmt="fancy_grid", maxcolwidths=20))
    
                elif escolha == "5":
                    if(sala.get_all()):
                        print()
                        sala.print()
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "7":
             while True:
                print("\n+-------- MENU HORÁRIO ---------+")
                print("| 1 - Inserir Horário           |")
                print("| 2 - Deletar Horário           |")
                print("| 3 - Atualizar Horário         |")
                print("| 4 - Buscar Horário por ID     |")
                print("| 5 - Listar Todos os Horários  |")
                print("| 6 - Voltar                    |")
                print("+-------------------------------+")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    hora = input("Digite o horário: ")
                    horario.insert(hora)

                elif escolha == "2":
                    if(horario.get_all()):
                        print()
                        horario.print()
                        print()     
                        id_horario = input("Digite o ID do horário a ser deletado: ")
                        horario.delete(id_horario)

                elif escolha == "3":
                    if(horario.get_all()):
                        print()
                        horario.print()
                        print()
                        id_horario = input("Digite o ID do horário a ser atualizado: ")
                        hora = input("Digite o novo horário: ")
                        horario.update(id_horario, hora)

                elif escolha == "4":
                    id_horario = input("Digite o ID do horário a ser buscado: ")
                    h = horario.get_by_id(id_horario)
                    if h:
                        headers = ["ID", "Horário"]
                        row = [[h[0][0], h[0][1]]]
                        print(tabulate(row, headers=headers, tablefmt="fancy_grid", maxcolwidths=20))
    
    
                elif escolha == "5":
                    if(horario.get_all()):
                        print()
                        horario.print()
    
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "8": # Exibição
            while True:
                print("\n+-------- MENU EXIBIÇÃO --------+")
                print("| 1 - Inserir Exibição          |")
                print("| 2 - Deletar Exibição          |")
                print("| 3 - Atualizar Exibição        |")
                print("| 4 - Buscar Exibição por ID    |")
                print("| 5 - Listar Todas as Exibições |")
                print("| 6 - Voltar                    |")
                print("+-------------------------------+")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    print()
                    filme.print(diretor, genero)
                    print()
                    id_filme = input("Digite o ID do filme: ")
                    print()
                    sala.print()
                    print()
                    id_sala= input("Digite o ID da sala: ")
                    print()
                    horario.print()
                    print()
                    id_horario = input("Digite o ID do horário: ")
                    data = input("Digite a data da exibição(ano-mês-dia): ")
                    exibicao.insert(id_filme, id_sala, id_horario, data)

                elif escolha == "2":
                    if(exibicao.get_all()):
                        print()
                        exibicao.print(filme, sala, horario)
                        print()
                        filme.print(diretor, genero)
                        print()  
                        id_filme = input("Digite o ID do filme a ser deletado: ")
                        print()
                        sala.print()
                        print()
                        id_sala = input("Digite o ID da sala a ser deletada: ")
                        print()
                        horario.print()
                        print()
                        id_horario = input("Digite o ID do horário a ser deletado: ")
                        exibicao.delete((int(id_filme), int(id_sala), int(id_horario)))

                elif escolha == "3":
                    if(exibicao.get_all()):
                        print()
                        exibicao.print(filme, sala, horario)
                        print()
                        filme.print(diretor, genero)
                        print()  
                        id_filme = input("Digite o ID do filme a ser atualizado: ")
                        print()
                        sala.print()
                        print()
                        id_sala = input("Digite o ID da sala a ser atualizada: ")
                        print()
                        horario.print()
                        print()
                        id_horario = input("Digite o ID do horário a ser atualizado: ")
                        data = input("Digite a nova data: ")
                        exibicao.update((int(id_filme), int(id_sala), int(id_horario)), data)

                elif escolha == "4":
                    id_exib = input("Digite o ID da exibição a ser buscada (id_filme,id_sala,id_horario): ")
                    id_exib = tuple(map(int, id_exib.split(',')))
                    e = exibicao.get_by_id(id_exib)
                    if e:
                        sql = f"""SELECT nome FROM cinema.filme WHERE id = {e[0][0]}"""
                        sql_filme = filme.query(sql)
                        sql = f"""SELECT nome FROM cinema.sala WHERE id = {e[0][1]}"""
                        sql_sala = sala.query(sql)
                        sql = f"""SELECT horario FROM cinema.horario WHERE id = {e[0][2]}"""
                        sql_horario = horario.query(sql)

                        headers = ["Filme", "Sala", "Horário", "Data"]
                        row = [[sql_filme[0][0], sql_sala[0][0], sql_horario[0][0], e[0][3]]]
                        print(tabulate(row, headers=headers, tablefmt="fancy_grid", maxcolwidths=20))
    
                elif escolha == "5":
                    if(exibicao.get_all()):
                        print()
                        exibicao.print(filme, sala, horario)
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "9":
            while True:
                print("\n+--------------------- MENU SQL ---------------------+")
                print("| 1 - Número de filmes dirigidos por cada diretor    |")
                print("| 2 - Quantidade de exibições por sala               |")
                print("| 3 - Listar todos filmes e suas premiações          |")
                print("| 4 - Voltar                                         |")
                print("+----------------------------------------------------+")

        
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    # Consulta para contar o número de filmes dirigidos por cada diretor (incluindo quem não dirigiu nenhum filme):
                    sql = """SELECT cinema.diretor.nome, cinema.diretor.idade, COUNT(cinema.filme.id) AS quantidade
                            FROM cinema.diretor
                            LEFT JOIN cinema.filme ON cinema.diretor.id = cinema.filme.id_diretor
                            GROUP BY cinema.diretor.nome, cinema.diretor.idade;"""
                    data = connection.query(sql)

                    print()
                    print("+----------------------+-------------+---------------------------------+")
                    print("|      Diretor         |    Idade    |  Quantidade de filmes dirigidos |")
                    print("+----------------------+-------------+---------------------------------+")
                    for diretor, idade, quantidade in data:
                        print(f"| {diretor:<20} | {idade:^11} | {quantidade:^31} |")
                    print("+----------------------+-------------+---------------------------------+")

                elif escolha == "2":
                    # Consulta para calcular a quantidade de exibições por sala:
                    sql = """SELECT cinema.sala.nome AS nome_sala, cinema.sala.capacidade, COUNT(*) AS quantidade_exibicoes
                            FROM cinema.exibicao
                            JOIN cinema.sala ON cinema.exibicao.id_sala = cinema.sala.id
                            GROUP BY cinema.sala.nome, cinema.sala.capacidade;"""

                    data = connection.query(sql)
                    print()
                    print("+-------------------------+-------------+---------------------------+")
                    print("|  Sala                   | Capacidade  |  Quantidade de exibições  |")
                    print("+-------------------------+-------------+---------------------------+")
                    for sala, cap, exib in data:
                        print(f"| {sala:<23} | {cap:^9}   | {exib:^23}   |")
                    print("+-------------------------+-------------+---------------------------+")

                elif escolha == "3":
                    # Consulta para listar todos os filmes, incluindo aqueles que não foram indicados a nenhuma premiação, e as premiações associadas a cada filme
                    sql = """SELECT cinema.filme.nome, cinema.premiacao.nome AS premiacao
                            FROM cinema.filme
                            LEFT JOIN cinema.indicacao_premiacao ON cinema.filme.id = cinema.indicacao_premiacao.id_filme
                            LEFT JOIN cinema.premiacao ON cinema.indicacao_premiacao.id_premiacao = cinema.premiacao.id;"""
                    
                    data = connection.query(sql)
                    print()
                    print("+--------------------------------+----------------------------------+")
                    print("|            Filme               |           Premiação              |")
                    print("+--------------------------------+----------------------------------+")
                    for filme, premiacao in data:
                        if premiacao == None:
                            premiacao = "Nenhuma premiação"
                        print(f"| {filme:30} | {premiacao:^30}   |")
                    print("+--------------------------------+----------------------------------+")

                elif escolha == "4":
                    break

                else:
                    print("Opção inválida. Tente novamente.")


        elif opcao == "10":
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")



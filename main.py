from Entities import Apartment, BallotBox, ResidentFactory
import matplotlib.pyplot as plt
import seaborn as sns

def generate_election_graphs(ballot_box):
    
    candidate_names = [candidate.name for candidate in ballot_box.candidates.values()]
    votes = [candidate.votes for candidate in ballot_box.candidates.values()]
    
    candidate_names.append("Votos Nulos")
    votes.append(ballot_box.null_votes)
    
    sns.set(style="whitegrid")
    palette = sns.color_palette("viridis", len(candidate_names))

    plt.figure(figsize=(8, 5))
    sns.barplot(x=candidate_names, y=votes, palette=palette)
    plt.xlabel("Candidatos")
    plt.ylabel("Quantidade de Votos")
    plt.title("Resultado da Eleição")
    plt.xticks(rotation=30)
    plt.show()

    plt.figure(figsize=(6, 6))
    plt.pie(votes, labels=candidate_names, autopct="%1.1f%%", colors=palette, startangle=90)
    plt.title("Proporção de Votos")
    plt.show()

def voting_process(ballot_box):
    while ballot_box.voted_apartments < ballot_box.total_apartments:
        name = input("\nDigite seu nome para votar: ").lower()
        resident = next((r for r in ballot_box.residents if r.name == name), None)

        if resident is None:
            print("Morador não encontrado!")
            continue

        candidate_number = int(input("Digite o número do candidato em quem deseja votar: "))
        resident.vote(ballot_box, candidate_number)

def main():
    ballot_box = BallotBox()
    apartments = {}

    while True:
        name = input("Nome do morador ou 'sair' para encerrar o cadastro: ").lower()
        if name == "sair":
            break

        apartment_number = input("Número do apartamento: ")

        if apartment_number not in apartments:
            apartments[apartment_number] = Apartment(apartment_number)

        is_candidate = input("O morador é candidato? [s/n]: ").lower() == "s"
        candidate_number = int(input("Número do candidato: ")) if is_candidate else None

        resident = ResidentFactory.create_resident(name, apartments[apartment_number], is_candidate, candidate_number)

        apartments[apartment_number].add_resident(resident)
        ballot_box.add_resident(resident)
        
        if is_candidate:
            ballot_box.add_candidate(resident)

    print("\nCadastro finalizado! Iniciando a votação...\n")
    voting_process(ballot_box)
    generate_election_graphs(ballot_box)


if __name__ == "__main__":
    main()

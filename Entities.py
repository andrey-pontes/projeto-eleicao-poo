from abc import ABC, abstractmethod

class Resident(ABC):
    def __init__(self, name, apartment):
        self.name = name
        self.apartment = apartment

    @abstractmethod
    def vote(self, ballot_box, candidate_number):
        pass

class Voter(Resident):
    def vote(self, ballot_box, candidate_number):
        ballot_box.register_vote(self, candidate_number)

class Candidate(Voter):
    def __init__(self, name, apartment, candidate_number):
        super().__init__(name, apartment)
        self.candidate_number = candidate_number
        self.votes = 0

    def receive_vote(self):
        self.votes += 1

class Apartment:
    def __init__(self, number):
        self.number = number
        self.residents = []
        self.has_voted = False

    def add_resident(self, resident):
        self.residents.append(resident)

    def vote(self):
        if self.has_voted:
            return False
        self.has_voted = True
        return True

class BallotBox:
    def __init__(self):
        self.candidates = {}
        self.residents = []
        self.apartments = {}
        self.total_apartments = 0
        self.voted_apartments = 0
        self.null_votes = 0

    def add_candidate(self, candidate):
        self.candidates[candidate.candidate_number] = candidate
        self.residents.append(candidate)

    def add_resident(self, resident):
        self.residents.append(resident)
        if resident.apartment.number not in self.apartments:
            self.apartments[resident.apartment.number] = resident.apartment
            self.total_apartments += 1

    def register_vote(self, resident, candidate_number):
        apartment = self.apartments[resident.apartment.number]  

        if apartment.has_voted:
            print(f"O apartamento {apartment.number} já votou. Somente um voto por Apartamento é permitido!")
            return

        if candidate_number not in self.candidates:
            print("Voto nulo registrado!")
            self.null_votes += 1
        else:
            self.candidates[candidate_number].receive_vote()
            print(f"Voto registrado!")

        apartment.has_voted = True
        self.voted_apartments += 1

        if self.voted_apartments == self.total_apartments:
            self.show_results()

    def show_results(self):
        print("\nResultado da Eleição:")
        winner = max(self.candidates.values(), key=lambda c: c.votes, default=None)

        for candidate in self.candidates.values():
            print(f"{candidate.name} ({candidate.candidate_number}): {candidate.votes} votos")

        print(f"Votos nulos: {self.null_votes}")

        if winner:
            print(f"\nO vencedor é {winner.name} com {winner.votes} votos!")
        else:
            print("\nNenhum candidato recebeu votos válidos.")

class ResidentFactory:
    @staticmethod
    def create_resident(name, apartment, is_candidate=False, candidate_number=None):
        if is_candidate:
            return Candidate(name, apartment, candidate_number)
        return Voter(name, apartment)
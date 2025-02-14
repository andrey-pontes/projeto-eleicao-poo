# Sistema de Votação com Factory Method em Python

Este projeto implementa um sistema de votação utilizando o padrão de projeto Factory Method. Ele permite cadastrar moradores de apartamentos, que podem ser eleitores ou candidatos, e simula uma eleição onde os moradores votam em candidatos. O sistema também gera gráficos para visualizar os resultados da eleição.

## Funcionalidades

### Cadastro de Moradores e Candidatos:
- Cadastre moradores, informando nome, número do apartamento e se são candidatos.
- Candidatos devem ter um número único para identificação.

### Votação:
- Cada apartamento pode votar apenas uma vez.
- Moradores votam em candidatos pelo número do candidato.
- Votos em números de candidatos inexistentes são considerados nulos.

### Resultados:
- Exibe o número de votos de cada candidato e a quantidade de votos nulos.
- Mostra o vencedor da eleição.
- Gera gráficos de barras e pizza para visualização dos resultados.

## Estrutura do Código

### Classes Principais

#### Resident (Classe Abstrata):
- Representa um morador.
- Atributos: `name` (nome), `apartment` (apartamento).
- Método abstrato: `vote`.

#### Voter (Subclasse de Resident):
- Representa um eleitor.
- Implementa o método `vote` para registrar o voto na urna.

#### Candidate (Subclasse de Voter):
- Representa um candidato.
- Atributos adicionais: `candidate_number` (número do candidato), `votes` (quantidade de votos recebidos).
- Método: `receive_vote` (incrementa a contagem de votos).

#### Apartment:
- Representa um apartamento.
- Atributos: `number` (número do apartamento), `residents` (lista de moradores), `has_voted` (indica se o apartamento já votou).
- Métodos: `add_resident`, `vote`.

#### BallotBox:
- Representa a urna eletrônica.
- Atributos: `candidates` (dicionário de candidatos), `residents` (lista de moradores), `apartments` (dicionário de apartamentos), `total_apartments`, `voted_apartments`, `null_votes`.
- Métodos: `add_candidate`, `add_resident`, `register_vote`, `show_results`.

#### ResidentFactory:
- Implementa o padrão Factory Method.
- Método estático: `create_resident` (cria instâncias de Voter ou Candidate).

## Métodos Principais

### register_vote:
- Registra o voto de um morador em um candidato (ou como voto nulo).
- Verifica se o apartamento já votou.

### show_results:
- Exibe os resultados da eleição, incluindo o vencedor e a quantidade de votos nulos.

### generate_election_graphs:
- Gera gráficos de barras e pizza para visualizar os resultados da eleição.

### voting_process:
- Gerencia o processo de votação, solicitando o nome do morador e o número do candidato.

### main:
- Função principal que inicia o cadastro de moradores e candidatos, e depois inicia a votação.

## Como Executar o Projeto

### Pré-requisitos:
- Python 3.x instalado.
- Sistema operacional: Linux ou Windows.

### Instalação das Dependências:

1. Baixe o arquivo `requirements.txt`, que contém as bibliotecas necessárias para o projeto.

2. Crie e ative um ambiente virtual para o projeto.

#### No Linux:

```bash
# Crie o ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual
source venv/bin/activate
```

#### No Windows:
```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
venv\Scripts\activate
```

### Instale as dependências necessárias a partir do arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```
### Executando o Projeto:
1. Salve os arquivos `Entities.py` e `main.py` no mesmo diretório.
2. O arquivo `Entities.py` contém as classes e métodos responsáveis pela lógica do sistema.
3. O arquivo `main.py` é o programa principal, onde as classes são importadas de `Entities.py` e a execução do sistema ocorre.
Execute o arquivo `main.py` com o seguinte comando:
```bash
python main.py
```

## Fluxo de Uso:
1. Cadastre moradores e candidatos.
2. Inicie a votação.
3. Visualize os resultados e os gráficos gerados.

## Exemplo de Uso
### Cadastro:
- Nome: Andrey

- Apartamento: 104

- É candidato? Não

- Número do candidato: (ignorado)

- Nome: Bruno

- Apartamento: 110

- É candidato? Sim

- Número do candidato: 10

### Votação:
- Andrey vota no candidato 10.
- Bruno vota no candidato 99 (voto nulo).

### Resultados:
- Bruno (10): 1 voto
- Votos nulos: 1
- Os gráficos do resultado serão exibidos.

## Gráficos Gerados
### Gráfico de Barras:
- Mostra a quantidade de votos por candidato e votos nulos.
### Gráfico de Pizza:
- Mostra a proporção de votos por candidato e votos nulos.

## Referências
AYEVA, Kamon; KASAMPALIS, Sakis. **Mastering Python Design Patterns: A guide to creating smart, efficient, and reusable software.** Packt Publishing Ltd, 2018.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

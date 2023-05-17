![Banner para Reddit Bloco de Cor Brilhante Clássico Amarelo, Azul e Vermelho](https://user-images.githubusercontent.com/76532722/236693898-b1714060-2851-4db1-9dc9-4fc649576bd2.png)

:construction: **Projeto em construção** :construction:

# Índice 

* [Descrição do Projeto](#descrição-do-projeto)
* [Requisitos](requisitos)
* [Endpoints](#endpoints)
* [Arquivos](#arquivos)
* [Funcionalidades do projeto](#funcionalidades-do-projeto)
* [Requisição](#requisição)


# Descrição do Projeto

Ash Ketchum  é um jovem treinador de 10 anos que sonha em se tornar um mestre Pokémon. Ash começou sua jornada em Kanto, onde recebeu seu primeiro Pokémon, Pikachu. Juntos, eles viajaram por várias regiões do mundo Pokémon, participando de batalhas de ginásio e torneios de treinadores, fazendo novos amigos e capturando novos Pokémon ao longo do caminho. 
Para ajudar o jovem Ash em sua conquista de ser o maior treinador Pokémon da história, fizemos uma poke api.
A POKE API é um repositório que possui chamadas de API para determinadas ações, e cada função tem o propósito de ajudar o Ash se tornar um grande treinador de Pokemons.
Todos os dados sao disponilizados em formato JSON no link <https://pokemonapi.franciscovaldec.repl.co/pokemon>. O dataset foi extraido com Kaggle, e através de um site construí endpoints que aceita os métodos necessários.

# Requisitos:

Para a utilização da api é necessário instalar o app POSTMAN. Com isso será possível passar os parâmetros necessários no momento da chamada.

# Endpoints:

##### Home:
https://pokemonapi.franciscovaldec.repl.co/

##### Dados de todos os Pokémons(GET):
https://pokemonapi.franciscovaldec.repl.co/pokemon

##### Pokémons por tipo(GET):
https://pokemonapi.franciscovaldec.repl.co/pokemon/<type>

##### Adicionar pokémon da Pokedex (POST):
https://pokemonapi.franciscovaldec.repl.co/pokemon_post
  
# Arquivos:
 - No arquivo settings temos as funções que vão ajudar ash a chegar no seu objetivo de ser um mestre Pokémon;
 - No arquivo de app temos os endpoints da pokedex que vai armazenar as informações de acordo com o pedido de Ash.

# Funcionalidades do projeto:
  
Funcionalidades do arquivo `settings`:
  

- `get_api`: requisição de get para pegar todos os pokémons da pokedex;


- `request_post`: requisição para que Ash poste na Pokedex;


- `captured_pokemon`: função que possibilita Ash indicar qual pokémon ele capturou e postar em sua pokedex;

- `pokedex`: Em algumas batalhas, Ash nao pode utilizar qualquer Pokémon, portanto, essa função faz com que ele pegue apenas pokémon de terminado tipo e XP para as suas batalhas de giná
sio

Funcionalidades do arquivo `app`:

O arquivo app é responsável por rodar o programa de API, e também por nos passar os endpoints que serao chamados no Postman.
 
 # Requisição:
  
  - Coloque o seu arquivo `app.py` para rodar, após isso, será criando uma uri para a aplicação local;
  - Crie um requisição de POST no Postman, no exemplo estou adicionando um pokémon capturado, portanto o endpoint será `http://localhost:500/pokemon_post`:
![image](https://github.com/francosoa/poke_api/assets/76532722/202503de-d764-48b4-89af-6b89ca0103d7)
  - Ainda no Postman, na opção de body, é hora de passar o corpo da sua postagem. Para realizar a postagem eu preciso passar o enpoint do que eu quero fazer, e o dicionário de pokémons que Ash capturou ao longo da jornada, ex:
  `[
    {
        "endpoint": "pokemon_post"
    },

    { 
  "captured_pokemon": 
  [
  {
        "attack": 49000000,
        "defense": 490000000,
        "generation": 1000000,
        "hp": 450000000,
        "id": 1,
        "legendary": false,
        "name": "Bulbasaur",
        "sp_atk": 65,
        "sp_def": 65,
        "speed": 45,
        "total": 318,
        "type_1": "Grass",
        "type_2": "Poison"
    }
  ]

    }
]`

- Agora é só enviar a requisição, e acessar o site para verificar se o pokémon já está na pokedex: https://pokemonapi.franciscovaldec.repl.co/pokemon
  
Para fazer outros tipos de requisição é só consultar o tópico de **enpoints**, e montar sua requisição de acordo com o que deseja fazer.
  
  

# My Pet Manager

My Pet Manager é uma aplicação web simples para gerenciar informações de pets, construída com Flask e SQLite.

## Requisitos

- Python 3.11 ou superior
- Docker (opcional, para execução em contêiner)

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/renzosa/projeto-final-git.git my-pet-manager
   cd my-pet-manager
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Execução

### Localmente

1. Execute o aplicativo:
   ```
   python3 info_pet.py
   ```

2. Acesse a aplicação em seu navegador em `http://localhost:5000`

### Com Docker

1. Construa a imagem Docker:
   ```
   docker buildx build -t pet-app .
   ```

2. Execute o contêiner:
   ```
   docker run -p 5000:5000 -v $(pwd)/dados:/app/dados pet-app
   ```

3. Acesse a aplicação em seu navegador em `http://localhost:5000`

## Uso

- Na página inicial, você verá uma lista de todos os pets cadastrados.
- Clique em "Adicionar Novo Pet" para cadastrar um novo pet.
- Use os botões "Visualizar", "Editar" e "Excluir" para gerenciar os pets existentes.

## Build

Para construir uma imagem Docker otimizada para produção:
   ```
   docker buildx build --platform linux/amd64 -t pet-app:latest .
   ```


## Contribuição

Contribuições são bem-vindas! Por favor, leia o [guia de contribuição](CONTRIBUTING.md) para mais detalhes sobre como contribuir para este projeto.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.

# Busca Preços

## Funcionamento

Este projeto busca preços no site Magazine Luiza e grava em uma planilha excel utilizando Python

## Setup

O projeto foi desenvolvido utilizando [python 3.8](https://www.python.org/downloads/), recomendo fortemente o uso de um ambiente virtual para execução do projeto, o setup assume que será utilizado o [venv](https://docs.python.org/3/library/venv.html) para esta funcionalidade.

Para testar o projeto basta:

1. Clonar o projeto na sua maquina
   ```
   git clone https://github.com/VanessaGeronimo/buscaPrecos.git
   ```
2. Dentro da pasta do projeto, criar um ambiente virtual para o mesmo
   ```
   cd buscaPrecos
   python3 -m venv venv
   ```
3. Instalar as dependências necessárias
   ```
   pip install -r requirements.txt
   ```
4. Executar o projeto
   ```
   python src/main.py
   ```
5. O resultado será gravado em `Products.xlsx`
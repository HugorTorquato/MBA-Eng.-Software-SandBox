# Projetos - Domain-driven designer

Este repositório contém três projetos diferentes, cada um com seus próprios requisitos e instruções de execução. Siga as orientações abaixo para configurar e rodar cada um dos projetos corretamente.

---

## 1. Validador de CPF

Este projeto consiste em uma ferramenta para validar números de CPF.

### Requisitos
- **Live Server**: É necessário utilizar o Live Server para rodar o projeto.

### Como executar
1. Certifique-se de que o Live Server está instalado em sua IDE (ex.: VS Code).
2. Abra o diretório do projeto.
3. Inicie o Live Server clicando com o botão direito no arquivo principal (index.html) e selecionando **"Open with Live Server"**.

---

## 2. Carrinho de Compras

Este projeto é uma aplicação que simula um carrinho de compras.

### Requisitos
- **Live Server**: Assim como no projeto anterior, é necessário utilizar o Live Server.

### Como executar
1. Certifique-se de que o Live Server está instalado em sua IDE (ex.: VS Code).
2. Abra o diretório do projeto.
3. Inicie o Live Server clicando com o botão direito no arquivo principal (index.html) e selecionando **"Open with Live Server"**.

---

## 3. API de Gestão Escolar

Este projeto é uma API para gestão escolar, que utiliza Docker para configurar o ambiente e o banco de dados.

### Requisitos
- **Docker** e **Docker Compose** instalados em sua máquina.

### Como executar
1. Certifique-se de que o Docker está instalado e rodando corretamente.
2. Verifique a versão do Docker Compose instalada:
   - Se a versão for **superior ou igual a 1.27**, use o comando:
     ```bash
     docker compose up --build -d
     ```
   - Se a versão for **inferior a 1.27**, use o comando:
     ```bash
     docker-compose up --build -d
     ```
> Detalhes sobre a mudança:
Docker 1.27 (2020): A primeira versão em que o novo comando docker compose foi introduzido como um plugin do Docker CLI. No entanto, o comando docker-compose (com hífen) ainda era o principal. Docker 20.10 (dezembro de 2020): A partir dessa versão, o comando docker compose passou a ser a forma recomendada e a versão oficial. O Docker CLI integrou o Compose como um plugin nativo, e o comando docker compose se tornou o novo padrão, enquanto o docker-compose (com hífen) ainda era suportado, mas como uma ferramenta separada e de baixo nível.

Se você está em uma versão mais recente do Docker (como 20.10 ou superior), você pode verificar se está usando a versão correta do docker compose com o comando:

```
docker compose version
```

Porém, se ainda estiver usando a versão antiga, o comando seria:

```
docker-compose --version
```

3. Após a execução do comando, o sistema e o banco de dados serão inicializados.
4. Acesse a API pelo endereço indicado no terminal (geralmente `http://localhost:8000`).

### Recomendação
Recomenda-se o uso do **VS Code** como IDE para este repositório. Além disso, instale a extensão oficial do Docker disponível no marketplace do VS Code para facilitar a execução e o gerenciamento de containers.

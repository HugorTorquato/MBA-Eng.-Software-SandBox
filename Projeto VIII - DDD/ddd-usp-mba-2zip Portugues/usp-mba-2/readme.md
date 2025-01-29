# Aula 2 - Domain-driven designer

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

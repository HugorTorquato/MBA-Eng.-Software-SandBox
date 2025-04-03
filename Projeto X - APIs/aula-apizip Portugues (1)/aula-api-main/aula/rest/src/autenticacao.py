from datetime import datetime, timedelta
from jose import JWTError, jwt
from configuracao import configuracoes


# Mando os dados do UserWarning
# adiciona qunado o token vai expeirar
#configura os dados com a chanve secreta com o algoritimo de encrypt
# tranasforma em um token por meio da biblioteca
# depois verifica se o toke retorna os dados do user

def criar_token_acesso(dados: dict):
    dados_codificados = dados.copy()
    expiracao = datetime.utcnow() + timedelta(
        minutes=int(configuracoes.TEMPO_DE_EXPIRACAO_TOKEN_DE_ACESSO)
    )
    dados_codificados.update({"exp": expiracao})
    return jwt.encode(
        dados_codificados,
        configuracoes.CHAVE_SECRETA,
        algorithm=configuracoes.ALGORITMO,
    )


def verificar_token(token: str):
    try:
        return jwt.decode(
            token, configuracoes.CHAVE_SECRETA, algorithms=[configuracoes.ALGORITMO]
        )
    except JWTError:
        return None

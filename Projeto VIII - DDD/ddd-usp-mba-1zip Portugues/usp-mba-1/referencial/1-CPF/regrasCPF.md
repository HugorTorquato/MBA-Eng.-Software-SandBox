# Regras para um CPF Válido

## Estrutura do CPF

O CPF é um número formado por 11 dígitos decimais com a seguinte configuração: ABC.DEF.GHI-JK

**Exemplo de CPF**: `123.456.789-09`.

Os oito primeiros dígitos são formados por um número base definido pela Receita Federal.
O 9º número, ocupado pela letra I, informa o estado em que o CPF foi emitido, conforme mostra a tabela abaixo:

| Região Fiscal | Estados                                  | Nono Dígito |
|----------------|------------------------------------------|-------------|
| 1.ª            | DF, GO, MT, MS, TO                      | 1           |
| 2.ª            | AC, AP, AM, PA, RO, RR                  | 2           |
| 3.ª            | CE, MA, PI                              | 3           |
| 4.ª            | AL, PB, PE, RN                          | 4           |
| 5.ª            | BA, SE                                   | 5           |
| 6.ª            | MG                                       | 6           |
| 7.ª            | ES, RJ                                   | 7           |
| 8.ª            | SP                                       | 8           |
| 9.ª            | PR, SC                                   | 9           |
| 10.ª           | RS                                       | 0           |


## Validação de CPF

O CPF é válido se os **dois últimos dígitos** (dígitos verificadores) forem calculados corretamente a partir dos 9 primeiros dígitos.

## Condições para um CPF ser Inválido

O CPF será considerado **inválido** nas seguintes situações:
- O CPF não pode ter números repetidos em sequência, como: `111.111.111-11`.
- Os **dígitos verificadores** precisam ser calculados corretamente. Caso contrário, o CPF será inválido.

## Cálculo dos Dígitos Verificadores

### Cálculo do 1º Dígito Verificador

1. Multiplicar os 9 primeiros números do CPF pelos seguintes pesos: `[10, 9, 8, 7, 6, 5, 4, 3, 2]`.
2. Somar os resultados dessas multiplicações.
3. Calcular o resto da soma dividida por 11.
4. Se o resto for menor que 2, o 1º dígito é **0**. Caso contrário, o 1º dígito é `11 - resto`.

### Cálculo do 2º Dígito Verificador

1. Multiplicar os 9 primeiros números do CPF mais o 1º dígito verificador pelos seguintes pesos: `[11, 10, 9, 8, 7, 6, 5, 4, 3, 2]`.
2. Somar os resultados dessas multiplicações.
3. Calcular o resto da soma dividida por 11.
4. Se o resto for menor que 2, o 2º dígito é **0**. Caso contrário, o 2º dígito é `11 - resto`.

## Exemplo de Cálculo

**CPF**: `123.456.789-09`

### 1º Dígito Verificador:
- **Multiplicação**:  
  `1*10 + 2*9 + 3*8 + 4*7 + 5*6 + 6*5 + 7*4 + 8*3 + 9*2 = 330`
- **Resto** da divisão de `330` por `11`:  
  `330 % 11 = 0`
- O **1º dígito verificador** é **0**.

### 2º Dígito Verificador:
- **Multiplicação**:  
  `1*11 + 2*10 + 3*9 + 4*8 + 5*7 + 6*6 + 7*5 + 8*4 + 9*3 + 0*2 = 330`
- **Resto** da divisão de `330` por `11`:  
  `330 % 11 = 0`
- O **2º dígito verificador** é **9**.

Portanto, o CPF **`123.456.789-09`** é **válido**.

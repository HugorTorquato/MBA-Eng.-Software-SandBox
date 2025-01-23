// Função chamada ao clicar no botão
function validateCPF() {
    const cpfInput = document.getElementById('cpf-input');
    const cpf = cpfInput.value.trim();
    const resultDiv = document.getElementById('result');

    // Verifica se o CPF é válido (não vazio, contém 11 números e não tem caracteres inválidos)
    if (!cpf || cpf.length !== 11 || isNaN(cpf)) {
        resultDiv.textContent = 'Por favor, insira um CPF válido (11 números).';
        resultDiv.className = 'invalid';
        return;
    }

    // Chama a função de validação
    if (isValidCPF(cpf)) {
        resultDiv.textContent = 'CPF válido!';
        resultDiv.className = 'valid';
    } else {
        resultDiv.textContent = 'CPF inválido!';
        resultDiv.className = 'invalid';
    }
}

// Função para verificar se o CPF é válido
function isValidCPF(cpf) {
    // Verifica se todos os dígitos são iguais (ex.: 111.111.111-11)
    if (/^(\d)\1+$/.test(cpf)) return false;

    let sum = 0;
    let remainder;

    // Calcula o primeiro dígito verificador
    for (let i = 1; i <= 9; i++) {
        sum += parseInt(cpf[i - 1]) * (11 - i);
    }
    remainder = (sum * 10) % 11;
    if (remainder === 10 || remainder === 11) remainder = 0;
    if (remainder !== parseInt(cpf[9])) return false;

    // Calcula o segundo dígito verificador
    sum = 0;
    for (let i = 1; i <= 10; i++) {
        sum += parseInt(cpf[i - 1]) * (12 - i);
    }
    remainder = (sum * 10) % 11;
    if (remainder === 10 || remainder === 11) remainder = 0;
    if (remainder !== parseInt(cpf[10])) return false;

    return true;
}
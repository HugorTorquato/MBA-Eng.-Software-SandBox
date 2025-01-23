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

    resultDiv.textContent = 'CPF válido!';
    resultDiv.className = 'valid';
}
// Inicializa o carrinho
let cart = JSON.parse(localStorage.getItem('cart')) || [];

// Atualiza o número de itens no carrinho
function updateCartCount() {
    const cartCount = document.getElementById('cart-count');
    cartCount.textContent = cart.length;
}

// Adiciona um item ao carrinho
function addToCart(event) {
    const button = event.target;
    const productName = button.getAttribute('data-name');
    const productPrice = parseFloat(button.getAttribute('data-price'));
    const productImage = button.parentElement.querySelector('img').getAttribute('src');

    cart.push({ name: productName, price: productPrice, image: productImage });

    localStorage.setItem('cart', JSON.stringify(cart));

    updateCartCount(); // Atualiza apenas a contagem
}

// Chama updateCartCount ao carregar a página
updateCartCount();

// Adiciona os ouvintes de evento nos botões
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', addToCart);
});
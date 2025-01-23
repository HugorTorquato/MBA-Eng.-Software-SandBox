let cart = JSON.parse(localStorage.getItem('cart')) || [];

function updateCartCount() {
    const cartCount = document.getElementById('cart-count'); // Provavelmente não existe no checkout.html
    if (cartCount) { // Verifica se o elemento existe antes de tentar acessá-lo.
        cartCount.textContent = cart.length;
    }
}

function updateCartDetails() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    cartItems.innerHTML = '';

    if (cart.length === 0) {
        cartItems.innerHTML = '<li>Sua sacola está vazia.</li>';
        cartTotal.textContent = 'R$ 0,00';
    } else {
        let total = 0;
        cart.forEach((item, index) => {
            const li = document.createElement('li');
            li.innerHTML = `
                <img src="${item.image}" alt="${item.name}" class="img-checkout">
                <span>${item.name} - R$ ${item.price.toFixed(2)}</span>
                <button class="remove-item" data-index="${index}">X</button> 
            `;
            cartItems.appendChild(li);
            total += item.price;

            // Adiciona o evento de clique para remover o item
            const removeButton = li.querySelector('.remove-item');
            removeButton.addEventListener('click', removeItemFromCart);
        });
        cartTotal.textContent = `R$ ${total.toFixed(2)}`;
    }
}

function removeItemFromCart(event) {
    const index = parseInt(event.target.getAttribute('data-index'));
    cart.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartDetails(); // Atualiza a exibição do carrinho
    updateCartCount();  // Se você tiver a função updateCartCount no checkout.js
}


document.querySelector('#cart-icon.back').addEventListener('click', function () {
    window.location.href = 'index.html';
});


updateCartDetails();
// ===== Dados das sobremesas =====
const sobremesas = [
    {
        nome: "Brigadeiro",
        preco: "R$ 2,50",
    },
    {
        nome: "Bolo de Pote",
        preco: "R$ 9,00",
       
    },
    {
        nome: "Pudim",
        preco: "R$ 7,50",
       
    },
    {
        nome: "Brownie com Cobertura",
        preco: "R$ 8,00",
       
    }
];

// ===== Container do popup =====
const container = document.getElementById('popupContainer');

// ===== Função para abrir popup =====
function abrirPopup(sobremesaIndex) {
    const item = sobremesas[sobremesaIndex];
    const listaIngredientes = item.ingredientes.map(ing => `<li>${ing}</li>`).join('');

    container.innerHTML = `
        <div class="popup active" onclick="if(event.target.classList.contains('popup')) fecharPopup()">
            <div class="popup-content">
                <button class="close-btn" onclick="fecharPopup()">×</button>
                <h2>${item.nome}</h2>
                <p><strong>Preço:</strong> ${item.preco}</p>
                <p><strong>Ingredientes:</strong></p>
                <ul>${listaIngredientes}</ul>
            </div>
        </div>
    `;
}

// ===== Função para fechar popup =====
function fecharPopup() {
    container.innerHTML = '';
}

// ===== Função para toggle da sidebar =====
function toggleMenu() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('open');
}

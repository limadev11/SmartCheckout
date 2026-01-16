// Toggle da sidebar
function toggleMenu() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('open');
}

// Dados dos pratos
const dados = {
    3: { titulo: "Strogonoff de Frango / Carne", porcoes: "10 porções", imagem: "/assets/img/strogonoff.jpg", ingredientes: ["Peito de frango / Patinho", "Sal a gosto", "Cebola picada", "Colher de manteiga", "Mostarda", "Dente de alho", "Pimenta do reino", "Maionese a gosto", "Ketchup", "Cogumelos", "Creme de leite", "Batata palha a gosto"] },
    4: { titulo: "Carne de Panela", porcoes: "10 porções", imagem: "/assets/img/carnedepanela.jpg", ingredientes: ["Carne (acem, patinho ou lombo de porco)", "Cubos de caldo de carne", "Cebolas grandes", "Temperos a gosto"] },
    5: { titulo: "Lasanha de Berinjela", porcoes: "6 porções", imagem: "/assets/img/lasanhaberinjela.jpg", ingredientes: ["Berinjelas grandes", "Dentes de alho", "Presunto", "Pimenta a gosto", "Sal a gosto", "Cebola grande", "Molho de tomate", "Mussarela"] },
    6: { titulo: "Moqueca de Peixe", porcoes: "4 porções", imagem: "/assets/img/moqueca.jpg", ingredientes: ["Peixe a gosto", "Pimentões coloridos", "Tomate", "Azeite ou óleo", "Vinagre ou limão", "Cebola", "Sal e pimenta", "Coentro e cebolinha", "Leite de coco"] },
    7: { titulo: "Arroz, Feijão e Bife Acebolado", porcoes: "Refeição completa", imagem: "/assets/img/bife.png", ingredientes: ["Arroz", "Feijão carioca", "Bife de alcatra", "Cebola", "Alho", "Tomate", "Alface", "Azeite", "Vinagre", "Sal e pimenta-do-reino"] },
    8: { titulo: "Peixe Frito com Arroz", porcoes: "Refeição completa", imagem: "/assets/img/peixe.jpg", ingredientes: ["Filé de peixe", "Limão", "Farinha de trigo", "Arroz", "Tomate", "Cebola", "Pimentão", "Vinagre", "Azeite", "Sal"] },
    9: { titulo: "Frango Grelhado com Purê", porcoes: "Refeição saudável", imagem: "/assets/img/frango.jpg", ingredientes: ["Peito de frango", "Batata inglesa", "Leite", "Manteiga", "Brócolis", "Sal, pimenta e noz-moscada"] },
    10: { titulo: "Escondidinho de Carne Moída", porcoes: "Refeição caseira", imagem: "/assets/img/escondidinho.jpg", ingredientes: ["Carne moída", "Batata inglesa", "Leite", "Manteiga", "Queijo mussarela", "Cebola", "Alho", "Sal e pimenta"] },
    11: { titulo: "Macarrão com Calabresa", porcoes: "Refeição prática", imagem: "/assets/img/macarraocalabresa.jpg", ingredientes: ["Macarrão (espaguete ou penne)", "Linguiça calabresa", "Cebola", "Alho", "Molho de tomate", "Queijo ralado", "Orégano", "Sal e azeite"] }
};

const container = document.getElementById('cardsContainer');

// Gera os cards
function gerarCards() {
    for (let id in dados) {
        const prato = dados[id];
        const card = document.createElement('div');
        card.classList.add('col-md-4');
        card.innerHTML = `
          <div class="card text-center">
            <img src="${prato.imagem}" alt="${prato.titulo}">
            <div class="card-content">
              <h2>${prato.titulo}</h2>
              <p>${prato.porcoes}</p>
              <button class="btn btn-card" onclick="abrirPopup(${id})">Ver mais</button>
            </div>
          </div>
        `;
        container.appendChild(card);
    }
}

// Abre popup
function abrirPopup(id) {
    const prato = dados[id];
    const lista = prato.ingredientes.map(item => `<li>${item}</li>`).join('');
    const popup = document.createElement('div');
    popup.classList.add('popup', 'active');
    popup.innerHTML = `
        <div class="popup-content">
          <button class="close-btn" onclick="fecharPopup(this)">×</button>
          <h2>${prato.titulo}</h2>
          <p><strong>Ingredientes:</strong></p>
          <ul>${lista}</ul>
        </div>
      `;
    popup.addEventListener('click', (e) => { if (e.target === popup) popup.remove(); });
    document.body.appendChild(popup);
}

function fecharPopup(btn) {
    const popup = btn.closest('.popup');
    popup.remove();
}

document.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        const popup = document.querySelector('.popup.active');
        if (popup) popup.remove();
    }
});

window.addEventListener('DOMContentLoaded', gerarCards);

document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. Bloco do Menu Mobile ---
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');

    // Verifica se os elementos do menu existem antes de adicionar o listener
    if (menuToggle && mobileMenu) {
        const menuIcon = menuToggle.querySelector('i');

        menuToggle.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');

            // Troca o ícone de 'bars' para 'times' (X)
            if (mobileMenu.classList.contains('hidden')) {
                menuIcon.classList.remove('fa-times');
                menuIcon.classList.add('fa-bars');
                menuToggle.setAttribute('aria-label', 'Abrir menu');
            } else {
                menuIcon.classList.remove('fa-bars');
                menuIcon.classList.add('fa-times');
                menuToggle.setAttribute('aria-label', 'Fechar menu');
            }
        });
    }

    // --- 2. Bloco de Animação de Título (Digitação) ---
    const frases = [
        "SISTEMA DE RECOMPENSAS.",
        "FAÇA SEU CHAVEIRO AGORA."
    ];
    let i = 0;
    let j = 0;
    let apagando = false;
    const textoSpan = document.querySelector('.titulo-principal .texto');

    function typeLoop() {
         // Só executa se o elemento de texto existir nesta página
        if (textoSpan) {
            let textoAtual = frases[i];
            if (!apagando) {
                textoSpan.innerText = textoAtual.slice(0, j++);
                if (j > textoAtual.length) {
                    apagando = true;
                    setTimeout(typeLoop, 2000); // Pausa antes de apagar
                    return;
                }
            } else {
                textoSpan.innerText = textoAtual.slice(0, j--);
                if (j < 0) {
                    apagando = false;
                    i = (i + 1) % frases.length; // Vai para a próxima frase
                    j = 0;
                }
            }
            setTimeout(typeLoop, apagando ? 50 : 100); // Velocidade de apagar/digitar
        }
    }
    
    typeLoop(); // Inicia a animação de digitação

    // --- 3. Bloco do Carrossel "Galeria de Projetos" ---
    new Swiper(".gallery-swiper", {
        slidesPerView: 1,
        spaceBetween: 20,
        loop: true,
        autoplay: { 
            delay: 3000,
            disableOnInteraction: false // Continua mesmo se o usuário interagir
        },
        pagination: { 
            el: ".gallery-swiper .swiper-pagination", // Seletor específico
            clickable: true 
        },
        breakpoints: {
            // telas a partir de 640px
            640: { 
                slidesPerView: 2 
            },
            // telas a partir de 1024px
            1024: { 
                slidesPerView: 3 
            },
        },
    });

    // --- 4. Bloco do Carrossel "Avaliações" ---
    new Swiper('.review-swiper', {
        loop: true,
        centeredSlides: true, // Slide ativo fica no centro
        slidesPerView: 1,     // Mostra 1 slide em telas pequenas
        spaceBetween: 20,
        autoplay: {
            delay: 3500, // Um pouco mais lento para dar tempo de ler
            disableOnInteraction: false,
        },
        breakpoints: {
            // telas a partir de 768px (md)
            768: { 
                slidesPerView: 3, // Mostra 3 slides
                spaceBetween: 30
            }
        },
        pagination: {
            el: '.review-swiper .swiper-pagination', // Seletor específico
            clickable: true,
        },
    });

    // --- 5. Bloco do "product-swiper" (do seu JS original) ---
    // (Se você não tem um ".product-swiper" nesta página, pode remover este bloco)
    new Swiper('.product-swiper', {
        loop: true,
        slidesPerView: 1,
        spaceBetween: 20,
        breakpoints: {
            768: {
                slidesPerView: 3,
                spaceBetween: 30
            }
        },
        pagination: {
            el: '.product-swiper .swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.product-swiper .swiper-button-next',
            prevEl: '.product-swiper .swiper-button-prev',
        },
    });

});
document.addEventListener('DOMContentLoaded', () => {
    // Bloco do menu - Está correto
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIcon = menuToggle.querySelector('i');

    menuToggle.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');

        if (mobileMenu.classList.contains('hidden')) {
            menuIcon.classList.remove('fa-times');
            menuIcon.classList.add('fa-bars');
            menuToggle.setAttribute('aria-label', 'Abrir menu');
            menuToggle.setAttribute('aria-expanded', 'false');
        } else {
            menuIcon.classList.remove('fa-bars');
            menuIcon.classList.add('fa-times');
            menuToggle.setAttribute('aria-label', 'Fechar menu');
            menuToggle.setAttribute('aria-expanded', 'true');
        }
    });

    // Bloco de Animação de Título - Está correto
    const typingTitle = document.querySelector('.animate-typing-title');
    if (typingTitle) {
        const textLength = typingTitle.textContent.trim().length;
        typingTitle.style.setProperty('--steps', textLength);
    }

    const typingSubtitle = document.querySelector('.animate-typing-subtitle');
    if (typingSubtitle) {
        const textLength = typingSubtitle.textContent.trim().length;
        typingSubtitle.style.setProperty('--steps', textLength);
    }

    // Bloco do productSwiper - Está correto
    const productSwiper = new Swiper('.product-swiper', {
        loop: true,
        slidesPerView: 1,
        spaceBetween: 20,
        breakpoints: {
            768: { // Em telas 'md' ou maiores
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

    // ######### MUDANÇA AQUI #########
    // O bloco do reviewSwiper foi atualizado com 'autoplay'
    const reviewSwiper = new Swiper('.review-swiper', {
        loop: true,
        centeredSlides: true, 
        slidesPerView: 1,
        spaceBetween: 20,
        
        // MUDANÇA: Adicionado Autoplay
        autoplay: {
            delay: 3000, // Move a cada 3 segundos
            disableOnInteraction: false, // Não para quando o usuário mexe
        },

        breakpoints: {
            768: {
                slidesPerView: 3,
                spaceBetween: 30
            }
        },
        pagination: {
            el: '.review-swiper .swiper-pagination', 
            clickable: true,
        },
    });
    // ######### FIM DA MUDANÇA #########

});
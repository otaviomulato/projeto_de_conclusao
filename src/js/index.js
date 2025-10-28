document.addEventListener('DOMContentLoaded', () => {
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

    const reviewSwiper = new Swiper('.review-swiper', {
loop: true,
slidesPerView: 1,
spaceBetween: 20,
autoHeight: true,
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

});
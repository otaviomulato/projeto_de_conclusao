document.addEventListener('DOMContentLoaded', () => {
    
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    //esses dois abaixo tambem são necessarios para funcionar o credito
    const credito_place = document.getElementById('credito');
    const userid = credito_place.innerHTML;

    if (menuToggle && mobileMenu) {
        const menuIcon = menuToggle.querySelector('i');

        menuToggle.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');

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
    //daqui
    function troca_credito(id) {
        fetch(`http://127.0.0.1:8000/api/usuarios/${id}/`)
            .then(res => res.json())
            .then(data => {
                credito_place.innerHTML = `$ ${data.credito}`;
            })
            .catch(err => console.error("erro ao buscar", err))
    }
    troca_credito(userid)
    //até aqui é o que faz fumegar o credito ser trocado

    const frases = [
        "SISTEMA DE RECOMPENSAS.",
        "FAÇA SEU CHAVEIRO AGORA."
    ];
    let i = 0;
    let j = 0;
    let apagando = false;
    const textoSpan = document.querySelector('.titulo-principal .texto');

    function typeLoop() {
        if (textoSpan) {
            let textoAtual = frases[i];
            if (!apagando) {
                textoSpan.innerText = textoAtual.slice(0, j++);
                if (j > textoAtual.length) {
                    apagando = true;
                    setTimeout(typeLoop, 2000); 
                    return;
                }
            } else {
                textoSpan.innerText = textoAtual.slice(0, j--);
                if (j < 0) {
                    apagando = false;
                    i = (i + 1) % frases.length;
                    j = 0;
                }
            }
            setTimeout(typeLoop, apagando ? 50 : 100);
        }
    }
    
    typeLoop();

    new Swiper(".gallery-swiper", {
        slidesPerView: 1,
        spaceBetween: 20,
        loop: true,
        autoplay: { 
            delay: 3000,
            disableOnInteraction: false 
        },
        pagination: { 
            el: ".gallery-swiper .swiper-pagination", 
            clickable: true 
        },
        breakpoints: {
            640: { 
                slidesPerView: 2 
            },
            1024: { 
                slidesPerView: 3 
            },
        },
    });

    new Swiper('.review-swiper', {
        loop: true,
        centeredSlides: true,
        slidesPerView: 1.2, 
        spaceBetween: 15,
        autoplay: {
            delay: 4000, 
            disableOnInteraction: false,
            pauseOnMouseEnter: true, 
        },
        breakpoints: {
            640: {
                slidesPerView: 2,
                spaceBetween: 20
            },
            1024: { 
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
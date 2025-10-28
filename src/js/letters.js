const frases = [
  "WAIT FOR ME,\nI'M COMING.",
  "VOU ATÉ O FIM,\nME ESPERA."
];

let i = 0;
let j = 0;
let apagando = false;

const textoSpan = document.querySelector('.titulo-principal .texto');

function typeLoop() {
  let textoAtual = frases[i];
  
  if (!apagando) {
    textoSpan.textContent = textoAtual.slice(0, j++);
    if (j > textoAtual.length) {
      apagando = true;
      setTimeout(typeLoop, 1500);
      return;
    }
  } else {
    textoSpan.textContent = textoAtual.slice(0, j--);
    if (j < 0) {
      apagando = false;
      i = (i + 1) % frases.length;
      j = 0;
    }
  }
  
  setTimeout(typeLoop, apagando ? 50 : 100);
}

typeLoop();
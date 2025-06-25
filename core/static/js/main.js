const phrases = ["Welcome to Our Cafeteria !!!", "Enjoy Every Sip !!!", "Freshly Brewed Happiness !!!"];
let i = 0;
let j = 0;
let currentPhrase = [];
let isDeleting = false;

function loop() {
  const typewriter = document.getElementById('typewriter');
  if (!typewriter) return;

  typewriter.innerHTML = currentPhrase.join('');

  if (i < phrases.length) {
    if (!isDeleting && j <= phrases[i].length) {
      currentPhrase.push(phrases[i][j]);
      j++;
    }

    if (isDeleting && j > 0) {
      currentPhrase.pop();
      j--;
    }

    if (j === phrases[i].length) {
      isDeleting = true;
      setTimeout(loop, 1500);
      return;
    }

    if (isDeleting && j === 0) {
      isDeleting = false;
      i = (i + 1) % phrases.length;
    }
  }

  setTimeout(loop, isDeleting ? 50 : 100);
}

loop();

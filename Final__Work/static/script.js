document.querySelector(".form__auth-btn").onclick = function () {
  const userPassFirst = document.querySelector("#password1").value;
  const userPassSecond = document.querySelector("#password2").value;


  if (userPassFirst == "") {
    document.getElementById("password1").style = "border: 1px solid red";
    document.getElementById("password2").style = "border: 1px solid red";
  } else if (userPassFirst != userPassSecond) {
    document.getElementById("password1").style = "border: 1px solid red";
    document.getElementById("password2").style = "border: 1px solid red";
    return false;
  } else if (userPassFirst == userPassSecond) {
    document.getElementById("password1").style = "border: 1px solid green";
    document.getElementById("password2").style = "border: 1px solid green";
  }
  return true;
};

// Модальное окно
const modal = document.getElementById('loginModal');
const openBtn = document.getElementById('openLoginModal');
const closeBtn = document.querySelector('.close');

// Открыть модалку
openBtn.onclick = function() {
    modal.style.display = 'block';
}

// Закрыть по крестику
closeBtn.onclick = function() {
    modal.style.display = 'none';
}

// Закрыть при клике на фон
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Закрыть по Escape
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        modal.style.display = 'none';
    }
});

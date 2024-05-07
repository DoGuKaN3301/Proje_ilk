function togglePassword() {
  var passwordInput = document.getElementById("password");
  var eyeIcon = document.querySelector(".toggle-password i");

  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    eyeIcon.classList.remove("fa-eye");
    eyeIcon.classList.add("fa-eye-slash");
  } else {
    passwordInput.type = "password";
    eyeIcon.classList.remove("fa-eye-slash");
    eyeIcon.classList.add("fa-eye");
  }
}

// Rastgele renk üreten bir fonksiyon
function rastgeleRenk() {
  var renk = '#' + Math.floor(Math.random()*16777215).toString(16); // Rastgele HEX renk kodu oluştur
  return renk;
}

// Belirli aralıklarla sınır rengini değiştir
setInterval(function() {
  var loginContainer = document.getElementById("login-container");
  var yeniRenk = rastgeleRenk(); // Rastgele renk al
  loginContainer.style.borderColor = yeniRenk; // Sınır rengini ayarla
}, 2000); // Her 2 saniyede bir değiştir (milisaniye cinsinden)



// Rastgele renk üreten bir fonksiyon
function rastgeleRenk() {
  var renk = '#' + Math.floor(Math.random()*16777215).toString(16); // Rastgele HEX renk kodu oluştur
  return renk;
}

// Belirli aralıklarla sınır rengini değiştir
setInterval(function() {
  var resimler = document.querySelectorAll(".resimler"); // Tüm resimlerin bulunduğu sınıfı seç
  resimler.forEach(function(resim) { // Her bir resim için işlem yap
    var yeniRenk = rastgeleRenk(); // Rastgele renk al
    resim.style.borderColor = yeniRenk; // Sınır rengini ayarla
  });
}, 2000); // Her 2 saniyede bir değiştir (milisaniye cinsinden)




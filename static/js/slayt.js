var index = 0;
var slaytFotolar = document.getElementsByClassName("slayt-foto");

function slaytGoster() {
  // Tüm resimleri gizle
  for (var i = 0; i < slaytFotolar.length; i++) {
    slaytFotolar[i].style.display = "none";  
  }
  
  // Index değerini arttır ve son resme ulaşıldıysa sıfıra döndür
  index++;
  if (index >= slaytFotolar.length) {
    index = 0;
  }
  
  // Şu anki resmi göster
  slaytFotolar[index].style.display = "block";  
  
  // Bir sonraki resme geçmek için 10 saniye bekleyin
  setTimeout(slaytGoster, 10000); // 10 saniye aralıklarla değiştir
}

// İlk çağrıyı yap
slaytGoster();



// değişen yazı için yazılmıi olan javasrc kodları


var degisenYazilar = [
  "Steve Jobs'un dediği gibi, 'Bir şirketin sadece parasını kazanma amacı varsa, o şirket asla büyük olamaz.' DAPHNE Yazılım Şirketi olarak, kar amacının ötesine geçerek, teknolojiyi insanların hayatlarını iyileştirmek için bir araç olarak kullanıyoruz.'",
  "'Kodlayanlar geleceği yazıyor.'derler. Biz de bu sözü kendimize misyon edindik ve her gün bir adım daha ileri gitmek için çalışıyoruz. Çünkü bizim için yazılım sadece bir meslek değil, bir tutkudur.",
  "Dijital dönüşüm çağında, DAPHNE Yazılım Şirketi sizin yanınızda. İnovasyon, kalite ve müşteri memnuniyeti konusundaki kararlılığımızla, geleceği birlikte şekillendiriyoruz.",
  "Dijital çağın öncüsü olmak, yazılım dünyasında yıldızlaşmak, geleceği bugünden şekillendirmek... İşte tüm bu hedeflerin gerçeğe dönüştüğü yer:   DAPHNE Yazılım Şirketi.",
  "DAPHNE Yazılım Şirketi, bugünün sorunlarına yarının çözümlerini sunuyor. Müşterilerimizin işletme ihtiyaçlarına uygun özelleştirilmiş çözümler üretirken, aynı zamanda topluma ve dünyaya katkıda bulunmanın gururunu yaşıyoruz."
];

var indexYazi = 0;
var yaziElementi = document.getElementById("degisenYazi");

function yaziGoster() {
  yaziElementi.textContent = degisenYazilar[indexYazi];
  indexYazi++;
  if (indexYazi >= degisenYazilar.length) {
    indexYazi = 0;
  }
}

// İlk çağrıyı yap
yaziGoster();

// Her 5 saniyede bir yazıyı güncelle
setInterval(yaziGoster, 10000);


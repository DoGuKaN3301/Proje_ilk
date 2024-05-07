function saatGuncelle() {
    var simdi = new Date();
    var saat = simdi.getHours();
    var dakika = simdi.getMinutes();
    var saniye = simdi.getSeconds();
    saat = (saat < 10 ? "0" : "") + saat;
    dakika = (dakika < 10 ? "0" : "") + dakika;
    saniye = (saniye < 10 ? "0" : "") + saniye;
    var zaman = saat + ":" + dakika + ":" + saniye;
    document.getElementById('saat').innerHTML = zaman;
}
setInterval(saatGuncelle, 1000);



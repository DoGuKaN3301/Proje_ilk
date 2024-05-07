from flask import Flask ,render_template ,redirect,session ,request , url_for
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import io
import sys
import html
from sorgular import select , insert , delete , update


#site yönlendirmesi
app =Flask(__name__)
app.secret_key="1234"



# anasayfaya yönlendirmesi için kullanılır
@app.route("/")            
def anasayfa(): 
        
    if "ad" in session and session ["ad"] != None:
        kullaniciadi = session.get('ad')
        return render_template("index.html",kullaniciadi=kullaniciadi)
    else:
            return render_template("giris.html")


# kullancıları yönlendirmesi için 
@app.route("/kullanici_ayarlari")            
def hesap_guncelle(): 
    if "ad" in session and session ["ad"] != None:
        return render_template("hesap_guncelle.html")
    else: 
        return redirect("/giris")


# python'a yönlendirmesi için 
@app.route("/python")            
def python(): 
    if "ad" in session and session ["ad"] != None:
        return render_template("python.html")
    else: 
        return redirect("/giris")
    

# c# yönlendirme kodları
@app.route("/c#")            
def c_sharp(): 
    if "ad" in session and session ["ad"] != None:
        return render_template("c_sharp.html")
    else: 
        return redirect("/giris")



# bolume yönlendirmek için kullanılır 
@app.route("/bolum")
def bolum():
    if "ad" in session and session ["ad"] != None:
        kullaniciadi = session.get('ad')
        
        return render_template("kg.html")
    else: 
        return redirect("/giris")
    
 

# yazılım mühendisi sayfası için kullanılır 
@app.route("/muhyazilim")            
def muhyazilim(): 
    if "ad" in session and session ["ad"] != None:
        return render_template("yazilimmuhendisi.html")
    else: 
        return redirect("/giris")
    




# girişte admin yada kullanıcı olup olmadığını kontrol etmesi için
@app.route("/giris")            
def giris():
    if "ad" in session and session ["ad"] != None:    
        kullaniciadi = session.get('ad')
        if "user_type" in session  and session["user_type"] == "admin":
            return render_template("admin.html",kullaniciadi=kullaniciadi)
        else: 
            return render_template("index.html",kullaniciadi=kullaniciadi)
        
    else:
        return render_template("giris.html")



# user tipi admin ise admin.html ye yönlendrimesi için
@app.route("/admin_panel")
def admin_panel():
    if "user_type" in session  and session["user_type"] == "admin":
        return render_template("admin.html")
    else:
        return render_template("hesap_guncelle.html")


  
    
# php sayfasına yönlendirmesi için kullanılır 
@app.route("/php")
def php():
    if "ad" in session and session ["ad"] != None:
        return render_template("php.html")
    else:
      return redirect("/giris")
    


# c++ sayfasına yönlendirmesi için
@app.route("/C++")
def c_plus():
    if "ad" in session and session ["ad"] != None:
        return render_template("c++.html")
    else:
      return redirect("/giris")
    

# muh bilgisayar.html ye yönlendirir
@app.route("/muhbilgisayar")
def muhbilgisayar():
    if "ad" in session and session ["ad"] != None:
        kullaniciadi = session.get('ad')
        return render_template("muhbilgisayar.html" ,kullaniciadi=kullaniciadi)
    else:
      return redirect("/giris")



# ziraata yönlendirmek için
@app.route("/ziraat")
def ziraat():
    if "ad" in session and session ["ad"] != None:
        sorgu = "SELECT * FROM ziraat "
        kayitlar = select(sorgu)          
        return render_template("ziraat.html", ziraat = kayitlar)
    else:
      return redirect("/giris")



# gıda.html sayfasına yönlendirmek için kullanılır
@app.route("/gida")            
def gida(): 
    if "ad" in session and session ["ad"] != None:
        sorgu = "SELECT * FROM gida "
        kayitlar = select(sorgu)          
        return render_template("gida.html", gida = kayitlar)
    else:
          return redirect("/giris")




# erisim.html sayfasına yönlendirmek için kullanılır
@app.route("/erisim")            
def erisim(): 
    if "ad" in session and session ["ad"] != None:       
        return render_template("erisim.html")
    else:
          return redirect("/giris")




# giriş yapman admin ise admin.html ye user ise index.html ye hiçbiri değilse kullanıcı bilgileri hatalı olan kod
@app.route("/loginbilgilerikontrol", methods=["POST"])
def login_kontrol():    
    if request.method == "POST":
        kullaniciadi = html.escape(request.form.get("kullaniciadi"))  #  <, >, &, ", ' gibi) HTML kodlarına dönüştürür.
        sifre = html.escape(request.form.get("sifre"))
        sorgu = f"SELECT * FROM personel WHERE ad = '{kullaniciadi}' AND sifre = '{sifre}'"
        kayitlar = select(sorgu)
        
        if kayitlar and len(kayitlar) != 0:
            session["ad"] = kullaniciadi
            
            if kayitlar[0][-1] == 'Admin':
                session["user_type"] = "admin"
                return render_template("admin.html", kullaniciadi=kullaniciadi)
            else:
                session["user_type"] = "user"
                return render_template("index.html", kullaniciadi=kullaniciadi)
        else:
            return render_template("giris.html", hata="Kullanıcı bilgileri hatalı!")

        


#admin panelde kullanıcıları listelemek için yazıldı
@app.route("/admin_panel/kullanici_bilgileri", methods=["GET", "POST"])
def kullanici_bilgileri():
    if "ad" in session and session ["ad"] != None:
          sorgu = "SELECT * FROM personel"
          kayitlar = select(sorgu)          
          return render_template("kullanicilar.html", personel = kayitlar)
    else:
          return redirect("/giris")
    






# bölümlere giriş yapılan yer
@app.route("/bolumkontrol", methods=["POST"])
def bolumkontrol():  
 if "ad" in session and session ["ad"] != None:
    if request.method == "POST":
        
        kullaniciadi = html.escape(request.form.get("kullaniciadi"))
        sifre = html.escape(request.form.get("sifre"))
        
        sorgu = f"SELECT bolum FROM personel WHERE ad = '{kullaniciadi}' AND sifre = '{sifre}'"
        kayitlar = select(sorgu)
        
        if kayitlar and len(kayitlar) != 0:
            session["ad"] = kullaniciadi
            kullaniciadi = session.get('ad')
            # Kullanıcının bölüm bilgisini al
            user_bolum = kayitlar[0][-1]  # İlk satırın ilk sütunu
            
            # Kullanıcıyı bölümüne göre yönlendir
            if user_bolum == 'Gıda':
                return redirect("/gida")
            elif user_bolum == 'Admin':
                return redirect("/erisim")
            elif user_bolum == 'Ziraat':
                return redirect("/ziraat")
            elif user_bolum == 'Yazılım':
                return render_template("yazilimmuhendisi.html" , kullaniciadi = kullaniciadi)
            elif user_bolum == 'Bilgisayar':
                return redirect("/muhbilgisayar", kullaniciadi=kullaniciadi)
            else:
                return render_template("kg.html", hata="Bilinmeyen bölüm!")
        
        else:
            return render_template("kg.html", hata="Kullanıcı adı veya şifre hatalı!")
    
    else:
        return render_template("kg.html", hata="Bilinmeyen bölüm!")
 else:
        return redirect("/giris")





# gida bilgilerini günceller
@app.route("/gida/guncelle",methods=["post"])
def gida_guncelle():
    if "ad" in session and session ["ad"] != None:
        id = request.form["id"]
        ad = request.form["ad"]
        kalori = request.form["kalori"]
        durum = request.form["durum"]
        katogori = request.form["katogori"]
        sorgu = f"UPDATE gida SET ad= '{ad}',  kalori= '{kalori}', durum= '{durum}' , katogori = '{katogori}' WHERE id={int(id)}"
        update(sorgu)
        return redirect("/gida")
        
    else:
      return redirect("/giris")



# güncellemme yaparken id kullanarak güncelleme yapıldığı için id yi alır 
@app.route("/gida/guncelle/<id>")                                   
def gida_gn(id):  
    if "ad" in session and session ["ad"] != None:
        sorgu = f"SELECT * FROM gida WHERE id={int(id)}"
        kayit = select(sorgu)                      
        return render_template ("gidagn.html", gida = kayit[0])
    else:
        return redirect("/giris")




# gıda da sorgu için kullanılır 
@app.route("/gida/sorgu", methods=["POST"])                                   
def gida_sorgu():  
    if "ad" in session and session["ad"] is not None:
        durum = request.form["durum"]
        katogori = request.form["katogori"]

        sorgu = f"SELECT * FROM gida WHERE durum = '{durum}' AND katogori = '{katogori}' "
        kayit = select(sorgu)

        if kayit:  # Eğer kayıt boş değilse
            first_char_upper = kayit[0][4].title()  # İlk harfi büyük yap
        else:
            first_char_upper = ""  # Kayıt boş ise başlangıç değeri boş dize olsun

        return render_template("gida.html", gida=kayit, first_char_upper=first_char_upper)
    else:
        return redirect("/giris")




# gıda silmek için kullanılır.
@app.route("/gida/sil/<id>")                                   
def gida_sil(id): 
     if "ad" in session and session ["ad"] != None:
            sorgu = f"DELETE FROM gida WHERE id={int(id)}"
            delete(sorgu)
            return redirect("/gida")
     else:
          return redirect("/giris")
     


# gıda eklemek için eklenmiştir
@app.route("/gida/ekle", methods=['GET','POST'])                                   
def gida_ekle():
    if "ad" in session and session ["ad"] != None:
            if request.method == "POST":
                ad = request.form["ad"]
                kalori = request.form["kalori"]
                durum = request.form["durum"]
                katogori = request.form["katogori"]
                sorgu = f"INSERT INTO gida (ad,kalori,durum , katogori) VALUES ('{ad}','{kalori}' ,'{durum}','{katogori}')"
                insert(sorgu)
                return redirect("/gida")
            else:
                return render_template("gida_ekle.html")
    else:
        return redirect("/giris")




# ziraat eklemek için kullanılır 
@app.route("/ziraat/ekle", methods=['GET','POST'])                                   
def ziraat_ekle():
    if "ad" in session and session ["ad"] != None:
            if request.method == "POST":
                ad = request.form["ad"]
                ekim_zamanı = request.form["ekim_zamanı"]
                gubre = request.form["gubre"]
                alınan_mahsul = request.form["alınan_mahsul"]
                il = request.form["il"]
                sorgu = f"INSERT INTO ziraat (ad, ekim_z , gubre ,alınan_m ,il) VALUES ('{ad}','{ekim_zamanı}' ,'{gubre}','{alınan_mahsul}','{il}')"
                insert(sorgu)
                return redirect("/ziraat")
            else:
                return render_template("ziraat_ekle.html")
    else:
        return redirect("/giris")



# ziraat için güncelleme
@app.route("/ziraat/guncelle",methods=["post"])
def ziraat_guncelle():
    if "ad" in session and session ["ad"] != None:
        id = request.form["id"]
        ad = request.form["ad"]
        ekim_zamanı = request.form["ekim_zamanı"]
        gubre = request.form["gubre"]
        alınan_mahsul = request.form["alınan_mahsul"]
        il = request.form["il"]
        sorgu = f"UPDATE ziraat SET ad= '{ad}',  ekim_z= '{ekim_zamanı}', gubre= '{gubre}' , alınan_m = '{alınan_mahsul}' , il = '{il}' WHERE id={int(id)}"
        update(sorgu)
        return redirect("/ziraat")
        
    else:
      return redirect("/giris")



# ziraat de sorgu için kullanılır 
@app.route("/ziraat/sorgu", methods=["POST"])                                   
def ziraat_sorgu():  
    if "ad" in session and session["ad"] is not None:
        ekim_z = request.form["ekim_z"]
        il = request.form["il"]
        sorgu = f"SELECT * FROM ziraat WHERE ekim_z = '{ekim_z}' or il = '{il}' "
        kayit = select(sorgu)
    
        if kayit:  # Eğer kayıt boş değilse
            first_char_upper = kayit[0][4].title()  # İlk harfi büyük yap
        else:
            first_char_upper = ""  # Kayıt boş ise başlangıç değeri boş dize olsun

        return render_template("ziraat.html", ziraat=kayit, first_char_upper=first_char_upper)
    else:
        return redirect("/giris")




# güncellemme yaparken id kullanarak güncelleme yapıldığı için id yi alır 
@app.route("/ziraat/guncelle/<id>")                                   
def ziraat_gn(id):  
    if "ad" in session and session ["ad"] != None:
        sorgu = f"SELECT * FROM ziraat WHERE id={int(id)}"
        kayit = select(sorgu)                      
        return render_template ("ziraatgn.html", ziraat = kayit[0])
    else:
        return redirect("/giris")




# ziraat silmek için kullanılır.
@app.route("/ziraat/sil/<id>")                                   
def ziraat_sil(id): 
     if "ad" in session and session ["ad"] != None:
            sorgu = f"DELETE FROM ziraat WHERE id={int(id)}"
            delete(sorgu)
            return redirect("/ziraat")
     else:
          return redirect("/giris")
      


# kullanıcı silmek için yazılmıştır
@app.route("/admin_panel/kullanici_bilgileri/sil/<id>")                                  
def kullanici_sil(id): 
     if "ad" in session and session ["ad"] != None:
            sorgu = f"DELETE FROM personel WHERE id={int(id)}"
            delete(sorgu)
            sorgu = "SELECT * FROM personel"
            kayitlar = select(sorgu)          
            return render_template("kullanicilar.html", personel = kayitlar)
     else:
          return redirect("/giris")
     
     
# kullanıcı bilgilerini güncellemek için yazılmıştır ama id alır

@app.route("/admin_panel/kullanici_bilgileri/guncelle/<id>")                                   
def kullanici_gn(id):  
    if "ad" in session and session ["ad"] != None:
        sorgu = f"SELECT * FROM personel WHERE id={int(id)}"
        kayit = select(sorgu)                      
        return render_template ("kullanicign.html", personel = kayit[0])
    else:
        return redirect("/giris")




# kullanıcı bilgilerini güncellemek için kullanılır.
@app.route("/admin_panel/kullanici_bilgileri/guncelle" ,methods=["post"])                                   
def kullanici_gnn():  
    if "ad" in session and session ["ad"] != None:
        id = request.form["id"]
        ad = request.form["ad"]
        email = request.form["email"]
        sifre = request.form["sifre"]
        tur = request.form["tur"]
        bolum = request.form["bolum"] 

        sorgu = f"UPDATE personel SET ad= '{ad}',  email= '{email}', sifre= '{sifre}', tur= '{tur}', bolum='{bolum}' WHERE id={int(id)}"
        update(sorgu)
        return redirect("/admin_panel/kullanici_bilgileri")
    else:
        return redirect("/giris")




# kullanıcı eklemek için yazılmıştır
@app.route("/admin_panel/kullanici_ekle",methods=['GET','POST'])                                 
def kullanici_ekle():  
    if "user_type" in session  and session["user_type"] == "admin":    
        if "ad" in session and session ["ad"] != None:
            if request.method == "POST":
                ad = request.form["ad"]
                email = request.form["email"]
                sifre = request.form["sifre"]
                tur = request.form["tur"]
                bolum = request.form["bolum"]   
                
                sorgu = f"INSERT INTO personel (ad,email,sifre,tur,bolum) VALUES ('{ad}','{email}' ,'{sifre}','{tur}','{bolum}')"
                insert(sorgu)
                
                return redirect("/admin_panel/kullanici_bilgileri")
            else:
                return render_template("kullaniciekle.html")
        else:
            return redirect("/giris")





# çıkışa bastığımızda sessionda bilgileri siler
@app.route("/cikis")                                
def cikis():
    if "user_type" in session  and session["user_type"] == "admin" :
        if "ad" in session:
            del session["ad"]
        return render_template("giris.html")
        
    else:
        if "ad" in session:
            del session["ad"]
        return render_template("giris.html")

app.run(debug=True)
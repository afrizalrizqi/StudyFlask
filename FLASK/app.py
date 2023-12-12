from flask import Flask, render_template

app = Flask(__name__)   #__name__ ini untuk nama aplikasinya

#define route
'''
Cara mendefine route yaitu dengan
@[nama flasknya].route
lalu bikin function index
'''
@app.route("/")
@app.route("/index")    #jadi kalau kaya gini nanti kedua pagenya akan menampilkan isi yang sama, jadi ketika di page utama akan menampilkan hello world, sedangkan ketika ubah ke page /index maka nanti juga akan muncul hello world
#sehingga ketika kita mempunya isi page yang sama kita bisa bikin routenya jadi dua dan dalam 1 function saja
def index():
    return render_template("index.html")

#misal bikin kita routing baru
'''
jadi ketika page nya ditambah dengan /user maka nanti munculnya nama dan kota 
tapi kalau masih di page biasa yaitu di 172.0.0.1:5000 maka nanti isi pagenya yaitu hello world
'''
@app.route("/user")
def get_user():
    user = {
        "nama" : "Afrizal",
        "kota" : "Surakarta"
    }
    return render_template("user.html", data=user)

app.run(debug=True) #debug=True : ini debugnya kita aktifkan
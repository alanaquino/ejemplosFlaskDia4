from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

products = [
    (1, "Motherboard Micro-ATX", 84.60, "hardware", "img/motherboard.jpg"),
    (2, "Procesador Intel i5", 190.60, "hardware", "img/i5.jpg"),
    (3, "Memoria ddr4", 60.75, "hardware","img/memoria.jpg"),
    (4, "Tarjeta de video", 239.93, "hardware","img/video.jpg"),
    (5, "Procesador Ryzen ", 199.90, "hardware","img/ryzen.jpg"),
    (6, "Procesador Intel 9", 450.00, "hardware","img/i9.jpg"),
    (7, "Windows 10 Pro 64 bits",99,"Software","img/windows.jpg")
]


@app.route("/")
def index():
    return render_template("index.html", products=products)


@app.route("/user", methods=["GET","POST"])
def user():
    if request.method == "POST":
        print(request.form)
        return redirect("/")
    else:
        return render_template("userform.html")


@app.route("/create", methods=["GET","POST"])
def create():
    if  request.method== "POST":
        nuevo = []
        for key in request.form.keys():
            nuevo.append(request.form[key])
        products.append(tuple(nuevo))
        return redirect("/")
    else:    
        return render_template("productform.html")

if __name__ == "__main__":
    app.run(debug=True)
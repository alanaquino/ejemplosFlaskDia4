from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

products = [
    (1, "Motherboard Micro-ATX", 84.60, "motherboard", "img/motherboard.jpg","Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum laudantium voluptate aliquid hic architecto? Obcaecati deserunt repellat perspiciatis praesentium pariatur, non amet ipsum recusandae delectus, deleniti nemo, provident repudiandae possimus!"),
    (2, "Procesador Intel i5", 190.60, "cpu", "img/i5.jpg","Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum laudantium voluptate aliquid hic architecto? Obcaecati deserunt repellat perspiciatis praesentium pariatur, non amet ipsum recusandae delectus, deleniti nemo, provident repudiandae possimus!"),
    (3, "Memoria ddr4", 60.75, "Memoria","img/memoria.jpg","Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum laudantium voluptate aliquid hic architecto? Obcaecati deserunt repellat perspiciatis praesentium pariatur, non amet ipsum recusandae delectus, deleniti nemo, provident repudiandae possimus!"),
    (4, "Tarjeta de video", 239.93, "video cards","img/video.jpg","Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum laudantium voluptate aliquid hic architecto? Obcaecati deserunt repellat perspiciatis praesentium pariatur, non amet ipsum recusandae delectus, deleniti nemo, provident repudiandae possimus!"),
    (5, "Procesador Ryzen ", 199.90, "cpu","img/ryzen.jpg","Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum laudantium voluptate aliquid hic architecto? Obcaecati deserunt repellat perspiciatis praesentium pariatur, non amet ipsum recusandae delectus, deleniti nemo, provident repudiandae possimus!"),
    (6, "Procesador Intel 9", 450.00, "cpu","img/i9.jpg","Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum laudantium voluptate aliquid hic architecto? Obcaecati deserunt repellat perspiciatis praesentium pariatur, non amet ipsum recusandae delectus, deleniti nemo, provident repudiandae possimus!"),
    (7, "Windows 10 Pro 64 bits",99.99,"Software","img/windows.jpg","Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum laudantium voluptate aliquid hic architecto? Obcaecati deserunt repellat perspiciatis praesentium pariatur, non amet ipsum recusandae delectus, deleniti nemo, provident repudiandae possimus!"),
    (8, "Power supply Corsair ",75.87,"power supply","img/power.jpg","Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum laudantium voluptate aliquid hic architecto? Obcaecati deserunt repellat perspiciatis praesentium pariatur, non amet ipsum recusandae delectus, deleniti nemo, provident repudiandae possimus!"),
    (9, "Unidad de almacenamiento SSD Kingston 480GB",64.90,"storage","img/ssd.jpg","Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum laudantium voluptate aliquid hic architecto? Obcaecati deserunt repellat perspiciatis praesentium pariatur, non amet ipsum recusandae delectus, deleniti nemo, provident repudiandae possimus!"),
]

categories = ["ALL"]
for c in products:
    categories.append(c[3])
categories = list(set(categories))
categories.sort()

@app.route("/")
def index():
    
    return render_template("index.html", products=products, categories=categories)


@app.route("/filter", methods=["GET","POST"])
def filter_products():
    if request.method == "POST":
        search = request.form['categoria']
        filtered_list = []
        if search == "All":
            return redirect("/")
        else:
            for p in products:
                if p[3] == search:
                    filtered_list.append(p)
            return render_template("index.html", products=filtered_list, categories=categories)
    else:
        return redirect("/")

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
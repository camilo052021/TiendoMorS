def importe_total_carro(request):
    total=0
    carro = request.session["carro"].items() # esta linea es temporal
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total+(float(value["precio"])*value["cantidad"])
    else:
        total = "Debes Hacer Login"
    return {"importe_total_carro": total}
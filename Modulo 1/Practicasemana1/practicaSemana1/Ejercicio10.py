precio=float(input("Ingrese el precio del producto: "))
descuento=float(input("Ingrese el porcentaje de descuento: "))

valor_descuento=precio*descuento/100
importe_a_pagar= precio - valor_descuento

print ("El descuento del valor del producto va a ser de $ ", round(valor_descuento,2), "y el importe a pagar sera de $ ", round(importe_a_pagar,2))


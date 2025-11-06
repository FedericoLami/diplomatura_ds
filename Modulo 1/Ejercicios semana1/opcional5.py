saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11 
adicional = 1000
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
mes=0

while pago_extra_mes_comienzo > mes :
        mes = mes +1 
        saldo = saldo * (1 + tasa/12) - pago_mensual 
        total_pagado = total_pagado + pago_mensual 

else : 
    while mes <= pago_extra_mes_fin :
        mes = mes + 1
        saldo = saldo * (1 + tasa/12) - pago_mensual - adicional
        total_pagado = total_pagado + pago_mensual + adicional
    else :
        while saldo > 0 :
            mes = mes +1 
            saldo = saldo * (1 + tasa/12) - pago_mensual 
            total_pagado = total_pagado + pago_mensual 
        
            

print('Total pagado:', round(total_pagado, 2), "          Saldo : ", saldo ,               "              Mes:", mes)
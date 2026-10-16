lanch = float (input ("Escreva o valor do lanche: "))
quant = int (input ("Escreva a quantidade comprada: "))
pagament = float (input ("Digite a quantidade paga: "))
total = lanch * quant

troco = pagament-total

print ("Total: ",total)
print ("Troco: ",troco)
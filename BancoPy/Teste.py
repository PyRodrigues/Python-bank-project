from models.cliente import Cliente
from models.conta import Conta


diego: Cliente = Cliente('Diego Rodrigues', 'drjrhh@gmail.com', '646.464.135.-98', '14/07/2000')
amanda: Cliente = Cliente('Amanda Rodrigues', 'amsnidf@gmail.com', '112.645.548-12', '19/11/2009')

# print(diego)
# print(amanda)

contad: Conta = Conta(diego)
contaa: Conta = Conta(amanda)

# print(contad)
# print(contaa)

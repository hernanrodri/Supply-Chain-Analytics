# Análisis de una cadena de suministro (Supply Chain)
## Descripción del proyecto

<img src = "Supply Chain Image.png" width = "500">
Ejemplo de una cadena de suministro formada por 15 plantas de almacenamiento, 11 puertos de orígenes y 1 puerto de destino.

### Primera parte
- Realizar un análisis exploratorio de cada una de las tablas de la base de datos "Logistics problem". </br>

### Segunda parte
- Determinar un conjunto de plantas de almacenaje, puertos de origen y puertos de destino que minimicen el costo total de la cadena de suministro.

$$ X_{ki} = q_{ki}*C_i $$

$$ Y_{ikpjcstm} = \frac{w_{ikpjcstm}}{\sum_{i}{...\sum_{m}{w_{ikpjcstm}}}}*R_{ikpjcstm} $$

$$ Z_{ipj} = \sum_{k}{(X_{ki} + \sum_{c}{...\sum_{m}{Y_{ikpjcstm}}})} $$

Bajo las siguientes restricciones:

#### Modo de transporte
- Aire
- Tierra

#### Nivel de servicio
- CRF (Customer Referred Freight): Solo el cliente paga el transporte.
- DTD (Door To Door):
- DTP (Door To Port):

## Referencias
<a href = "https://brunel.figshare.com/articles/dataset/Supply_Chain_Logistics_Problem_Dataset/7558679?file=20162015"> Database </a>

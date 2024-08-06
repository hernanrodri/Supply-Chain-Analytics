# Análisis de una cadena de suministro (Supply Chain)
## Descripción del proyecto

Se tiene una cadena de suministro formada por 15 plantas de almacenamiento, 11 puertos de orígenes y 1 puerto de destino. </br>
<p align = "center">
  <img src = "Supply Chain Image.png" width = "500"/>
</p>

### Primera parte
- Realizar un análisis exploratorio de cada una de las tablas de la base de datos "Logistics problem".

### Segunda parte
- Determinar un conjunto de plantas de almacenaje, puertos de origen y puertos de destino que minimicen el costo total de la cadena de suministro.

Nomenclatura:
- k: ID de pedido
- i: ID de planta de almacenamiento
- p: ID de puerto de origen
- j: ID de puerto de destino
- c: ID de transportista
- s: Nivel de servicio
- t: Tiempo de envío [días]
- m: Modo de transporte (aire o tierra)
- q: Cantidad de items en cada pedido [items]

- M: Costo de fijo de transporte [USD/kg]
- X: Costo de almacenamiento [USD/item]
- Y: Costo de transporte [USD/kg]
- Z: Costo total de la cadena de suministro [USD]

Ecuaciones:

$$ X_{ki} = q_{ki}*C_i $$

$$ Si \ s = CRF: \ Y_{ikpjcstm} = 0 $$

$$ Si \ s \neq CRF, \ m = Tierra: \ Y_{ikpjcstm} = \frac{w_{ikpjcstm}}{\sum_{i}{...\sum_{m}{w_{ikpjcstm}}}}*R_{ikpjcstm} $$

$$ Si \ s \neq CRF, \ m \neq Tierra: \ Y_{ikpjcstm} = w_{ikpjcstm}*R_{ikpjcstm} $$

Función Objetivo:

$$ Z_{ipj} = min \sum_{k}{(X_{ki} + \sum_{c}{...\sum_{m}{Y_{ikpjcstm}}})} $$

Restricciones:

$$ Si \ Y_{ikpjcstm} < M_{ikpjcstm}: \ Y_{ikpjcstm} = M_{ikpjcstm} $$

$$ w_{ikpjcstm} \leq F_{ikpjcstm} $$


#### Nivel de servicio
- CRF (Customer Referred Freight): Solo el cliente paga el transporte.
- DTD (Door To Door)
- DTP (Door To Port)

## Referencias
<a href = "https://brunel.figshare.com/articles/dataset/Supply_Chain_Logistics_Problem_Dataset/7558679?file=20162015"> Database </a>

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

- C: Costo de almacenamiento [USD/item]
- M: Costo fijo de transporte [USD/kg]
- X: Costo de almacenamiento [USD]
- Y: Costo de transporte [USD/kg]
- Z: Costo total de la cadena de suministro [USD]

Ecuaciones:

$$ X_{ki} = q_{ki}*C_i $$

$$ Si \ s = CRF \ \Rightarrow \ Y_{kpjcstm} = 0 $$

$$ Si \ s \neq CRF, \ m = Tierra \ \Rightarrow \ Y_{kpjcstm} = \frac{w_{kpjcstm}}{\sum_{i}{w_{kpjcstm}}}*R_{kpjcstm} $$

$$ Si \ s \neq CRF, \ m \neq Tierra \ \Rightarrow \ Y_{kpjcstm} = w_{kpjcstm}*R_{kpjcstm} $$

Función Objetivo:

$$ Z_{ipj} = min \sum_{k}{(X_{ki} + Y_{kpj})} $$

Restricciones:

$$ Si \ Y_{kpjcstm} < M_{kpjcstm} \ \Rightarrow \ Y_{kpjcstm} = M_{kpjcstm} $$

$$ w_{kpjcstm} \leq F_{kpjcstm} $$


#### Nivel de servicio
- CRF (Customer Referred Freight): Solo el cliente paga el transporte.
- DTD (Door To Door)
- DTP (Door To Port)

## Referencias
<a href = "https://brunel.figshare.com/articles/dataset/Supply_Chain_Logistics_Problem_Dataset/7558679?file=20162015"> Database </a>

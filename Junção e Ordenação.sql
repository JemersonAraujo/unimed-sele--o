select c.NomeCliente,p.PedidoID,p.DataPedido
from Pedidos p 
left join Clientes c on c.ClienteID = p.ClienteID
order by p.DataPedido desc;
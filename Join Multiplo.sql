select c.NomeCliente, p.PedidoID, count(pro.ProdutoID) Clientes c
left join Pedidos p on p.ClienteID = c.ClienteID
left join Produtos pro on pro.PedidoID = p.PedidoID
group by c.NomeCliente, p.PedidoID;
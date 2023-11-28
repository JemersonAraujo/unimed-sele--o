select c.NomeCategoria, count(p.ProdutoID)
from Produtos p 
left join Categorias c on c.CategoriaID = p.CategoriaID
group by c.NomeCategoria ; 
select a.NomeAluno, Notas.media
from Alunos a,
(select n.AlunoID, avg (n.Nota) as media from Notas n group by n.AlunoID ) as Media 
where a.AlunoID = Notas.AlunoID;
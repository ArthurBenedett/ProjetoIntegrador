# Sistema de Análise de Desempenho Acadêmico
Projeto desenvolvido com o objetivo de ajudar a coordenação do SENAI a analisar o desempenho dos alunos de forma mais rápida, organizada e confiável.

# Sobre o Projeto
Atualmente, o processo de análise de notas é feito de forma manual, o que gera:
- Dados desorganizados
- Possíveis erros de cálculo
- Retrabalho constante
- Dificuldade na tomada de decisão

# Design Thinking

# Mapa de Empatia
Acesse o mapa completo:
https://miro.com/app/board/uXjVGwxcw1Y=/

# Visual do Mapa
![Mapa de Empatia](./prints/MapaEmpatia.jpeg)

# Metodologia Ágil
# Kanban
Acesse o quadro Kanban:
https://miro.com/app/board/uXjVGwxOsFg=/

# Visual do Kanban
![Kanban](./prints/Kanban.jpeg)

# Levantamento de Requisitos

# Requisitos Funcionais (RF)
- RF01: O sistema deve receber uma lista de alunos no formato de tuplas ("Nome", [notas]).  
- RF02: O sistema deve verificar se a lista de notas de cada aluno não está vazia ou com dados inválidos.  
- RF03: O sistema deve calcular a média das notas de cada aluno.  
- RF04: O sistema deve percorrer os dados utilizando estruturas de repetição.  
- RF05: O sistema deve identificar quais alunos estão em recuperação (média < 7.0).  
- RF06: O sistema deve identificar o aluno com a maior média.  
- RF07: O sistema deve gerar um relatório final em arquivo .txt com os resultados.  
- RF08: O sistema deve mostrar mensagens quando encontrar dados inválidos.  

# Requisitos Não Funcionais (RNF)
- RNF01: O sistema deve ser desenvolvido em Python.  
- RNF02: O código deve ser dividido em dois arquivos: main.py e processamento.py.  
- RNF03: O sistema deve tratar possíveis erros relacionados a dados inválidos.  
- RNF04: O código deve ser organizado, fácil de entender e manter.  
- RNF05: O sistema deve ter um bom desempenho ao processar os dados.  
- RNF06: O projeto deve utilizar Git (branches, commits e merges).  

# Regras de Negócio (RN)
- RN01: A média do aluno deve ser calculada somando todas as notas e dividindo pela quantidade de notas.  
- RN02: Alunos com média menor que 7.0 devem ser considerados "Em Recuperação".  
- RN03: O Top Student será o aluno com maior média.  
- RN04: Alunos com lista de notas vazia ou inválida não devem ser considerados.  
- RN05: O relatório deve apresentar as informações de forma clara e organizada.  

# Tecnologias Utilizadas
- Python
- Git & GitHub

# Estrutura do Projeto
projeto/
- main.py
- processamento.py
- resultado.txt
- README.md

# Exemplo de Saída
RELATÓRIO DE DESEMPENHO
------------------------------media dos aluno:
Arthur Benedetti: 8.17
Esther Scartozzoni: 5.00
Fabio Henrique Pacheco: 5.83
Giovanni Buscarino: 9.50

alunos em recuperação:
Esther Scartozzoni: 5.00
Fabio Henrique Pacheco: 5.83

bom aluno:
Giovanni Buscarino: 9.50
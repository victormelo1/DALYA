import plotly.graph_objects as go
from plotly.subplots import make_subplots

luiz = int(input("Quantas tarefas Luiz Daltro concluidas? "))
beatriz = int(input("Quantas tarefas Beatriz Rodrigues concluidas? "))
priscilaPaixao = int(input("Quantas tarefas Priscila Paixao concluidas? "))
grazielle = int(input("Quantas tarefas Grazielle Ramos concluidas? "))
paulo = int(input("Quantas tarefas Paulo Igor concluidas? "))
priscilaFarias = int(input("Quantas tarefas Priscila Farias concluidas? "))
luis = int(input("Quantas tarefas Luis Octavio concluidas? "))

coordenadores = ['Luiz Daltro','Beatriz Rodrigues','Priscila Paixao','Grazielle Ramos', 
                 'Paulo Igor', 'Priscila Farias', 'Luis Octavio']
concluidas = [luiz, beatriz, priscilaPaixao, grazielle, paulo, priscilaFarias, luis]

fig = go.Figure(data=[go.Pie(labels=coordenadores, values=concluidas)])
fig.update_layout(title_text="Concluídas Sou Grato")

fig.show()


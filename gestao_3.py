import plotly.graph_objects as go
from plotly.subplots import make_subplots

luiz = int(input("Quantas tarefas de Luiz Daltro estão em atraso ? "))
beatriz = int(input("Quantas tarefas de Beatriz Rodrigues estão em atraso? "))
priscilaPaixao = int(input("Quantas tarefas de Priscila Paixao estão em atraso? "))
grazielle = int(input("Quantas tarefas de Grazielle Ramos estão em atraso? "))
paulo = int(input("Quantas tarefas de Paulo Igor estão em atraso? "))
priscilaFarias = int(input("Quantas tarefas de Priscila Farias estão em atraso? "))
luis = int(input("Quantas tarefas de Luis Octavio estão em atraso? "))

coordenadores = ['Luiz Daltro','Beatriz Rodrigues','Priscila Paixao','Grazielle Ramos', 
                 'Paulo Igor', 'Priscila Farias', 'Luis Octavio']

atrasos = [luiz, beatriz, priscilaPaixao, grazielle, paulo, priscilaFarias, luis]

fig = go.Figure(data=[go.Pie(labels=coordenadores, values=atrasos)])
fig.update_layout(title_text="Atrasos Sou Grato")

fig.show()
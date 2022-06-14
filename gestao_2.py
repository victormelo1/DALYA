import plotly.graph_objects as go
from plotly.subplots import make_subplots

luiz = int(input("Quantas tarefas Luiz Daltro está por fazer? "))
beatriz = int(input("Quantas tarefas Beatriz Rodrigues está por fazer? "))
priscilaPaixao = int(input("Quantas tarefas Priscila Paixao está por fazer? "))
grazielle = int(input("Quantas tarefas Grazielle Ramos está por fazer? "))
paulo = int(input("Quantas tarefas Paulo Igor está por fazer? "))
priscilaFarias = int(input("Quantas tarefas Priscila Farias está por fazer? "))
luis = int(input("Quantas tarefas Luis Octavio está por fazer? "))

coordenadores = ['Luiz Daltro','Beatriz Rodrigues','Priscila Paixao','Grazielle Ramos', 
                 'Paulo Igor', 'Priscila Farias', 'Luis Octavio']

porfazer = [luiz, beatriz, priscilaPaixao, grazielle, paulo, priscilaFarias, luis]

fig = go.Figure(data=[go.Pie(labels=coordenadores, values=porfazer)])
fig.update_layout(title_text="Por Fazer Sou Grato")

fig.show()
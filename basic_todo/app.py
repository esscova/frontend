from fasthtml.fastapp import fast_app, serve, Titled, RedirectResponse  
from components import gerar_titulo, gerar_formulario, gerar_lista_de_tarefas

app, routes = fast_app()
lista_tarefas = [] #fakedb

@routes('/')
def homepage():
    item_lista_tarefas = gerar_lista_de_tarefas(lista_tarefas)
    formulario = gerar_formulario()
    return Titled('To-do com FastHTML', formulario, item_lista_tarefas)

@routes('/adicionar_tarefa', methods=['post'])
def adicionar_tarefa(tarefa:str):
    if tarefa:
        lista_tarefas.append(tarefa)
    return gerar_lista_de_tarefas(lista_tarefas)

@routes('/deletar/{posicao}')
def deletar_tarefa(posicao:int):
    lista_tarefas.pop(posicao)
    return gerar_lista_de_tarefas(lista_tarefas)

serve()
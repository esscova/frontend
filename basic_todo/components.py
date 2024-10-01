from fasthtml.components import Div, H1, P, Form, Input, Button, Ul, Li, A

def gerar_titulo(titulo:str, subtitulo:str):
    return Div(
        H1(titulo),
        P(subtitulo)
    )

def gerar_formulario():
    formulario = Form(
        Input(type='text', name='tarefa', placeholder='Insira a tarefa a ser adicionada'),
        Button('Enviar'),
        method='post',
        action='/adicionar_tarefa',
        hx_post='/adicionar_tarefa',
        hx_target='#lista-tarefas',
        hx_swap='outerHTML'
    )
    return formulario


def gerar_lista_de_tarefas(lista_tarefas:list):
    itens_da_lista = [
        Li(tarefa, ' - ', A('Excluir', 
                            hx_get=f'/deletar/{i}',
                            hx_target='#lista-tarefas',
                            hx_swap='outerHTML')) for i,tarefa in enumerate(lista_tarefas)
    ]
    lista = Ul(*itens_da_lista, id='lista-tarefas')
    return lista
import flet as ft 
import sqlite3 

class ToDo:
    def __init__(self, page : ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window.height = 450
        self.page.window.width = 350
        self.page.window.resizable = False
        self.page.window.always_on_top = True
        self.page.title = 'TaskFlow'
        self.main_page()

    #TODO
    def db_execute(self, query, params = []):
        pass


    def tasks_container(self):
        return ft.Container(
            height=self.page.height = 0.8,
            #TODO
            content= ft.Column(
                controls=[
                    ft.Checkbox(label='Tarefa 1', value=True)
                ]
            )
        )

    def main_page(self):
        input_task = ft.TextField(hint_text='Digite aqui uma tarefa', expand=True)

        input_bar = ft.Row(
            controls=[
                input_task,
                ft.FloatingActionButton(icon=ft.icons.ADD)
            ]
        )

        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text='Todos'),
                ft.Tab(text='Em andamento'),
                ft.Tab(text='Finalizados')
            ]
        )

        tasks = self.tasks_container()

        self.page.add(input_bar, tabs, tasks)


ft.app(target=ToDo)
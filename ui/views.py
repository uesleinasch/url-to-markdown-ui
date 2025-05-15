# -*- coding: utf-8 -*-

"""
Views para a aplicação de conversão de URL para Markdown.

Este módulo contém as classes de visualização que compõem a interface
gráfica do usuário.
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

from shared.controllers import UrlConverterController

class MultipleUrlInput(BoxLayout):
    """
    Widget para entrada de uma URL com botão para adicionar mais campos.
    
    Este componente consiste em um campo de texto para a URL e um botão
    para remover esse campo específico da lista.
    """
    
    def __init__(self, parent_view, **kwargs):
        """
        Inicializa o componente de entrada de URL.
        
        Args:
            parent_view (UrlListView): Referência à view pai que contém este componente
        """
        super(MultipleUrlInput, self).__init__(**kwargs)
        
        self.parent_view = parent_view
        self.orientation = 'horizontal'
        self.size_hint = (1, None)
        self.height = 40
        self.spacing = 5
        
        # Campo para entrada da URL
        self.url_input = TextInput(
            hint_text='Digite a URL aqui...',
            multiline=False,
            size_hint=(0.9, 1),
            font_size='16sp'
        )
        self.add_widget(self.url_input)
        
        # Botão para remover este campo
        self.remove_button = Button(
            text='-',
            size_hint=(0.1, 1),
            background_color=(1, 0.3, 0.3, 1)
        )
        self.remove_button.bind(on_press=self.on_remove_pressed)
        self.add_widget(self.remove_button)
    
    def on_remove_pressed(self, instance):
        """
        Manipula o evento de pressionar o botão de remover campo.
        
        Args:
            instance: A instância do botão pressionado
        """
        self.parent_view.remove_url_input(self)
    
    def get_url(self):
        """
        Retorna o texto inserido no campo de URL.
        
        Returns:
            str: O texto da URL inserido pelo usuário
        """
        return self.url_input.text.strip()


class UrlListView(BoxLayout):
    """
    View que gerencia a lista de campos de URL.
    
    Esta classe implementa um container para os campos de entrada de URL,
    com funcionalidades para adicionar e remover campos.
    """
    
    def __init__(self, **kwargs):
        """Inicializa a view de lista de URLs."""
        super(UrlListView, self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.spacing = 5
        self.size_hint = (1, None)
        self.bind(minimum_height=self.setter('height'))
        
        # Lista para armazenar as referências aos componentes de entrada de URL
        self.url_inputs = []
        
        # Adiciona o primeiro campo de entrada de URL
        self.add_url_input()
    
    def add_url_input(self, *args):
        """
        Adiciona um novo campo de entrada de URL à lista.
        
        Args:
            *args: Argumentos opcionais para compatibilidade com eventos
        """
        url_input = MultipleUrlInput(self)
        self.url_inputs.append(url_input)
        self.add_widget(url_input)
    
    def remove_url_input(self, url_input):
        """
        Remove um campo de entrada de URL da lista.
        
        Args:
            url_input (MultipleUrlInput): O componente de entrada a ser removido
        """
        # Não permite remover se houver apenas um campo
        if len(self.url_inputs) <= 1:
            return
            
        self.url_inputs.remove(url_input)
        self.remove_widget(url_input)
    
    def get_all_urls(self):
        """
        Retorna todas as URLs inseridas nos campos.
        
        Returns:
            list: Lista com todas as URLs inseridas
        """
        return [url_input.get_url() for url_input in self.url_inputs]
    
    def clear_all_fields(self):
        """Limpa todos os campos de entrada de URL."""
        # Remove todos os campos exceto o primeiro
        while len(self.url_inputs) > 1:
            url_input = self.url_inputs[-1]
            self.remove_url_input(url_input)
        
        # Limpa o primeiro campo
        if self.url_inputs:
            self.url_inputs[0].url_input.text = ''


class MainView(BoxLayout):
    """
    View principal da aplicação.
    
    Esta classe implementa a interface principal do usuário, contendo
    campos para entrada de múltiplas URLs e botões para controle.
    """
    
    def __init__(self, **kwargs):
        """Inicializa a view principal."""
        super(MainView, self).__init__(**kwargs)
        
        # Configura o layout principal
        self.orientation = 'vertical'
        self.padding = [20, 20, 20, 20]
        self.spacing = 10
        
        # Define tamanho mínimo da janela
        Window.size = (600, 500)
        Window.minimum_width, Window.minimum_height = 500, 400
        
        # Inicializa o controlador
        self.controller = UrlConverterController()
        
        # Adiciona o título
        self.add_widget(Label(
            text='URL para Markdown',
            font_size='24sp',
            size_hint=(1, 0.1)
        ))
        
        # Adiciona uma mensagem de boas-vindas
        self.add_widget(Label(
            text='Adicione URLs para abrir no navegador com o conversor de Markdown',
            font_size='16sp',
            size_hint=(1, 0.1)
        ))
        
        # Área de rolagem para campos de URL
        scroll_view = ScrollView(
            size_hint=(1, 0.5),
            do_scroll_x=False,
            do_scroll_y=True
        )
        
        # Adiciona a view de lista de URLs
        self.url_list_view = UrlListView()
        scroll_view.add_widget(self.url_list_view)
        self.add_widget(scroll_view)
        
        # Layout para botões de controle
        control_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.1),
            spacing=10
        )
        
        # Botão para adicionar mais campos de URL
        add_button = Button(
            text='Adicionar URL',
            size_hint=(0.3, 1),
            background_color=(0.3, 0.8, 0.3, 1)
        )
        add_button.bind(on_press=self.url_list_view.add_url_input)
        control_layout.add_widget(add_button)
        
        # Botão para executar
        self.execute_button = Button(
            text='Executar',
            size_hint=(0.4, 1),
            background_color=(0.3, 0.6, 1, 1)
        )
        self.execute_button.bind(on_press=self.on_execute_pressed)
        control_layout.add_widget(self.execute_button)
        
        # Botão para limpar
        clear_button = Button(
            text='Limpar',
            size_hint=(0.3, 1),
            background_color=(0.8, 0.8, 0.8, 1)
        )
        clear_button.bind(on_press=self.on_clear_pressed)
        control_layout.add_widget(clear_button)
        
        self.add_widget(control_layout)
        
        # Área para exibir o resultado/status
        self.status_area = TextInput(
            text='Os resultados serão exibidos aqui.',
            readonly=True,
            multiline=True,
            size_hint=(1, 0.2)
        )
        self.add_widget(self.status_area)
    
    def on_execute_pressed(self, instance):
        """
        Manipula o evento de pressionar o botão de executar.
        
        Args:
            instance: A instância do botão pressionado
        """
        try:
            # Obtém todas as URLs inseridas
            urls = self.url_list_view.get_all_urls()
            urls = [url for url in urls if url]  # Remove URLs vazias
            
            if not urls:
                self.status_area.text = 'Por favor, insira pelo menos uma URL.'
                return
                
            # Processa as URLs usando o controlador
            results = self.controller.process_multiple_urls(urls)
            
            # Atualiza a área de status
            success_count = sum(1 for r in results if r)
            self.status_area.text = f"Foram abertas {success_count} de {len(urls)} URLs no navegador."
            
        except Exception as e:
            self.status_area.text = f'Erro: {str(e)}'
    
    def on_clear_pressed(self, instance):
        """
        Manipula o evento de pressionar o botão de limpar.
        
        Args:
            instance: A instância do botão pressionado
        """
        self.url_list_view.clear_all_fields()
        self.status_area.text = 'Os campos foram limpos.'

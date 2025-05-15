# -*- coding: utf-8 -*-

"""
Aplicação principal Kivy.

Este módulo contém a classe principal da aplicação Kivy que inicializa
a interface do usuário.
"""

from kivy.app import App
from ui.views import MainView

class UrlToMarkdownApp(App):
    """
    Classe principal da aplicação Kivy para o conversor de URL para Markdown.
    
    Esta classe inicializa e gerencia a aplicação Kivy, configurando os elementos
    da interface do usuário.
    """
    
    def __init__(self, **kwargs):
        """Inicializa a aplicação."""
        super(UrlToMarkdownApp, self).__init__(**kwargs)
        self.title = 'URL para Markdown'
    
    def build(self):
        """
        Constrói e retorna a interface principal da aplicação.
        
        Returns:
            MainView: A view principal da aplicação
        """
        return MainView()

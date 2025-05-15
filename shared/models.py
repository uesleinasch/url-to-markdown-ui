# -*- coding: utf-8 -*-

"""
Modelo para o conversor de URL para Markdown.

Este módulo contém as classes relacionadas a dados e regras de negócio
para a conversão de conteúdo de URLs para o formato Markdown.
"""

import webbrowser

class UrlConverter:
    """
    Classe responsável pela conversão de conteúdo de URL para Markdown.
    
    Esta classe implementa a lógica principal de negócio para converter
    o conteúdo obtido de uma URL para o formato Markdown.
    """
    
    def __init__(self):
        """Inicializa o conversor de URL."""
        pass
    
    def convert_url_to_markdown(self, url):
        """
        Converte o conteúdo de uma URL para o formato Markdown.
        
        Args:
            url (str): A URL a ser convertida
            
        Returns:
            str: O conteúdo formatado em Markdown
            
        Raises:
            ValueError: Se a URL for inválida
        """
        # Este é apenas um placeholder. A implementação real seria feita aqui.
        try:
            # Aqui viria o código para buscar a URL e converter para Markdown
            return f"# Conteúdo da URL: {url}\n\nConteúdo convertido estaria aqui."
        except Exception as e:
            raise ValueError(f"Erro ao converter a URL: {str(e)}")
        
    def open_url_in_browser(self, url):
        """
        Abre uma URL no navegador padrão do sistema.
        
        Args:
            url (str): A URL a ser aberta
            
        Returns:
            bool: True se a URL foi aberta com sucesso, False caso contrário
            
        Raises:
            ValueError: Se a URL for inválida
        """
        try:
            # Verifica se a URL está em um formato válido
            if not url or len(url.strip()) == 0:
                raise ValueError("A URL não pode estar vazia")
                
            # Abre a URL no navegador padrão
            return webbrowser.open(url, new=2)  # new=2 abre em uma nova aba
        except Exception as e:
            raise ValueError(f"Erro ao abrir a URL no navegador: {str(e)}")

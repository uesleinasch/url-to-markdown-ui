# -*- coding: utf-8 -*-

"""
Controladores para o conversor de URL para Markdown.

Este módulo contém as classes de controlador que coordenam a interação
entre as views e os modelos.
"""

from shared.models import UrlConverter

class UrlConverterController:
    """
    Controlador para intermediar a interação entre a UI e o modelo de conversão.
    
    Esta classe implementa as operações de controle necessárias para coordenar
    os inputs da interface do usuário com as operações de conversão.
    """
    
    def __init__(self):
        """Inicializa o controlador com um conversor."""
        self.converter = UrlConverter()
        self.markdown_prefix = "https://markdown.nimk.ir/"
    
    def process_url(self, url):
        """
        Processa uma URL e retorna o conteúdo em Markdown.
        
        Args:
            url (str): A URL a ser processada
            
        Returns:
            str: O conteúdo em Markdown
            
        Raises:
            ValueError: Se ocorrer algum erro no processamento
        """
        try:
            if not url or len(url.strip()) == 0:
                raise ValueError("A URL não pode estar vazia")
                
            # Valida se a URL está em um formato válido
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
                
            # Converte a URL para Markdown usando o modelo
            return self.converter.convert_url_to_markdown(url)
            
        except Exception as e:
            raise ValueError(f"Erro ao processar a URL: {str(e)}")
            
    def process_multiple_urls(self, urls):
        """
        Processa múltiplas URLs e abre cada uma no navegador com o prefixo.
        
        Args:
            urls (list): Lista de URLs a serem processadas
            
        Returns:
            list: Lista de resultados (True/False) indicando quais URLs foram abertas com sucesso
            
        Raises:
            ValueError: Se ocorrer algum erro no processamento
        """
        if not urls or len(urls) == 0:
            raise ValueError("A lista de URLs não pode estar vazia")
            
        results = []
        errors = []
        
        for url in urls:
            try:
                if url and len(url.strip()) > 0:
                    # Valida se a URL está em um formato válido
                    if not url.startswith(('http://', 'https://')):
                        url = 'https://' + url
                    
                    # Adiciona o prefixo de markdown
                    markdown_url = f"{self.markdown_prefix}{url}"
                    
                    # Abre a URL no navegador
                    success = self.converter.open_url_in_browser(markdown_url)
                    results.append(success)
                    
                    if not success:
                        errors.append(f"Falha ao abrir URL: {url}")
            except Exception as e:
                results.append(False)
                errors.append(f"Erro ao processar URL '{url}': {str(e)}")
        
        if errors:
            raise ValueError("; ".join(errors))
            
        return results

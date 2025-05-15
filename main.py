#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aplicação principal que inicializa o app Kivy.

Este módulo contém a função principal que inicializa a aplicação Kivy.
"""

from ui.app import UrlToMarkdownApp

if __name__ == "__main__":
    # Inicializa a aplicação
    app = UrlToMarkdownApp()
    app.run()

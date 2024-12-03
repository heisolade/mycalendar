#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour lancer le myCalendar.
Auteur : Olade LAOUROU
Date : 03/12/2024
"""

import os

class EnvManager:
    """Gestionnaire du fichier .env."""
    
    @staticmethod
    def find_in_env(key):
        """Recherche une clé dans le fichier .env."""
        try:
            with open(".env", "r") as fichier:
                for ligne in fichier:
                    if "=" in ligne:
                        cle, valeur = ligne.strip().split("=", 1)
                        if cle == key:
                            return valeur
        except FileNotFoundError:
            return 'NONE'
        return 'NONE'

    @staticmethod
    def write_in_env(key, value):
        """Ajoute une clé-valeur dans le fichier .env si elle n'existe pas."""
        if EnvManager.find_in_env(key) == 'NONE':
            with open(".env", "a") as fichier:
                fichier.write(f"{key}={value}\n")
            print(f"✔ {key} enregistrée avec succès dans .env.")
        else:
            print(f"⚠ {key} existe déjà dans .env.")

class ConnectService:
    def __init__(self):
        name_in_env = EnvManager.find_in_env('NAME')
        self.username = name_in_env if name_in_env != 'NONE' else input('[username] Hello !! Type your name : ')
        if name_in_env == 'NONE':
            EnvManager.write_in_env('NAME', self.username)
        print(f"👋 [{self.username}] Bienvenue, {self.username} !")

    def openai_config(self):
        api_key_in_env = EnvManager.find_in_env('OPENAI_API_KEY')
        self.openAIKey = api_key_in_env if api_key_in_env != 'NONE' else input('[OpenAI] Type your OpenAI API key : ')
        if api_key_in_env == 'NONE':
            EnvManager.write_in_env('OPENAI_API_KEY', self.openAIKey)
        print("✔ Clé OpenAI configurée avec succès !")

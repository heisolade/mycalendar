#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour lancer le myCalendar.
Auteur : Olade LAOUROU
Date : 03/12/2024
"""

import os
import json
import getpass
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

SCOPES = ['https://www.googleapis.com/auth/calendar']

class EnvManager:
    """Gestionnaire pour créer et écrire dans un fichier JSON ou gérer les variables d'environnement."""

    BASE_DIR = os.path.expanduser("~/.mycalendar")

    @staticmethod
    def ensure_hidden_directory():
        """Crée le répertoire caché s'il n'existe pas."""
        if not os.path.exists(EnvManager.BASE_DIR):
            os.makedirs(EnvManager.BASE_DIR)

    @staticmethod
    def save_to_json(file_name, data):
        """Enregistre des données dans un fichier JSON."""
        EnvManager.ensure_hidden_directory()
        file_path = os.path.join(EnvManager.BASE_DIR, file_name)
        try:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f"✔ Données enregistrées avec succès dans {file_path}.")
        except Exception as e:
            print(f"❌ Une erreur s'est produite lors de l'enregistrement : {e}")

    @staticmethod
    def find_in_env(key):
        """Recherche une clé dans le fichier .env."""
        EnvManager.ensure_hidden_directory()
        env_path = os.path.join(EnvManager.BASE_DIR, ".env")
        try:
            with open(env_path, "r") as fichier:
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
        EnvManager.ensure_hidden_directory()
        env_path = os.path.join(EnvManager.BASE_DIR, ".env")
        if EnvManager.find_in_env(key) == 'NONE':
            with open(env_path, "a") as fichier:
                fichier.write(f"{key}={value}\n")
            print(f"✔ {key} enregistrée avec succès dans {env_path}.")
        else:
            print(f"⚠ {key} existe déjà dans {env_path}.")

class ConnectService:
    def __init__(self):
        name_in_env = EnvManager.find_in_env('NAME')
        self.username = name_in_env if name_in_env != 'NONE' else "default_user"
        if name_in_env == 'NONE':
            EnvManager.write_in_env('NAME', self.username)
        print(f"👋 [{self.username}] Bienvenue, {self.username} !")

    def get_user_credentials(self, email=None, password=None):
        """Demande ou utilise les credentials fournis pour email et mot de passe."""
        if email is None or password is None:
            email = input('Entrez votre email : ')
            password = getpass.getpass('Entrez votre mot de passe : ')

        user_data = {
            'email': email,
            'password': password
        }

        # Enregistrer les données dans un fichier JSON
        EnvManager.save_to_json('user_credentials.json', user_data)
        print("✔ Credentials configurés avec succès !")

    def google_config(self):
        creds = None
        token_path = os.path.join(EnvManager.BASE_DIR, 'token.pickle')
        credentials_path = os.path.join(EnvManager.BASE_DIR, 'credentials.json')

        if not os.path.exists(credentials_path):
            print(f"❌ Le fichier {credentials_path} est introuvable.")
            print("Veuillez placer votre fichier 'credentials.json' dans le répertoire suivant :")
            print(f"  {EnvManager.BASE_DIR}")
            return

        if os.path.exists(token_path):
            with open(token_path, 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES
            )
            try:
                creds = flow.run_local_server(port=8080)
            except Exception:
                flow.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
                auth_url, _ = flow.authorization_url(prompt='consent')
                print("Veuillez ouvrir ce lien dans votre navigateur pour autoriser l'accès :")
                print(auth_url)

                code = input("Entrez le code d'autorisation ici : ")
                flow.fetch_token(code=code)
                creds = flow.credentials
            with open(token_path, 'wb') as token:
                pickle.dump(creds, token)

        print("✔ Google Calendar configuré avec succès !")
        return creds
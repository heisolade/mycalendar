#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour lancer le myCalendar.
Auteur : Olade LAOUROU
Date : 03/12/2024
"""

from connectService import *
from prompt import *

def main():
    printCalendar()
    service = ConnectService()
    service.get_user_credentials()
    creds = service.google_config()
    service = build('calendar', 'v3', credentials=creds)
    # event = {
    #     'summary': 'Test Réunion',
    #     'start': {
    #         'dateTime': '2024-12-07T10:00:00+01:00',  # Format ISO 8601
    #         'timeZone': 'Europe/Paris',
    #     },
    #     'end': {
    #         'dateTime': '2024-12-07T11:00:00+01:00',  # Format ISO 8601
    #         'timeZone': 'Europe/Paris',
    #     },
    # }
    # print("Données de l'événement envoyé à l'API :")
    # print(event)

    # try:
    #     event = service.events().insert(calendarId='primary', body=event).execute()
    #     print('Événement créé avec succès : %s' % event.get('htmlLink'))
    # except Exception as e:
    #     print("Erreur lors de la création de l'événement :")
    #     print(e)

if __name__ == "__main__":
    main()

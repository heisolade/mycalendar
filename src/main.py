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
    service.openai_config()

if __name__ == "__main__":
    main()

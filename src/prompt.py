#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour lancer le myCalendar.
Auteur : Olade LAOUROU
Date : 03/12/2024
"""

import pyfiglet
from colorama import Fore, Back, Style, init
import time
import sys

init(autoreset=True)

def printWithanimation(texte, color=Fore.WHITE, delay=0.05):
    """Affiche un texte caractère par caractère avec animation."""
    for char in texte:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def printCalendar():
    title = pyfiglet.figlet_format("MYCALENDAR", font="slant")
    sous_title = "by Olade"

    color_title = Fore.MAGENTA + Back.BLACK + Style.BRIGHT
    color_sous_title = Fore.YELLOW + Style.BRIGHT
    ligne_separation = Fore.CYAN + f"{'-'*40}"

    print(color_title)
    for line in title.splitlines():
        printWithanimation(line, color=Fore.MAGENTA, delay=0.02)

    printWithanimation(ligne_separation, color=Fore.CYAN, delay=0.01)
    printWithanimation(sous_title.center(40), color=color_sous_title, delay=0.03)
    printWithanimation(ligne_separation, color=Fore.CYAN, delay=0.01)


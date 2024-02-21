#!/usr/bin/env python3
"""Hello World Multilingual

Depending on the language configured in the environment, the program displays
the corresponding message.

Usage:

Have a properly configured LANG variable. Example:

    export LANG=pt_BR

Execution:

    python3 hello.py
    or
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Bruno Sousa"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
message = "Hello, World!"

if current_language == "pt_BR":
    message = "Olá, Mundo!"
elif current_language == "it_IT": 
    message = "Ciao, Mondo!"
    
print(message)

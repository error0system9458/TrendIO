#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":





    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TrendIO.settings")
    try:
        from django.core.management import execute_from_command_line



        print("""
    ___________________________________________________________________________________________________________________
    _______                 _ _____ ____    __  __       _          _____
    |__   __|               | |_   _/ __ \  |  \/  |     (_)        / ____|
        | |_ __ ___ _ __   __| | | || |  | | | \  / | __ _ _ _ __   | (___   ___ _ ____   _____ _ __
        | | '__/ _ \ '_ \ / _` | | || |  | | | |\/| |/ _` | | '_ \   \___ \ / _ \ '__\ \ / / _ \ '__|
        | | | |  __/ | | | (_| |_| || |__| | | |  | | (_| | | | | |  ____) |  __/ |   \ V /  __/ |
        |_|_|  \___|_| |_|\__,_|_____\____/  |_|  |_|\__,_|_|_| |_| |_____/ \___|_|    \_/ \___|_|
    ___________________________________________________________________________________________________________________

    Written By: Piyush Sharma
    \x1B[01;91m

            """)


    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

#! /usr/bin/env python3
# simbot_launcher.py
# Refactored using Clean Architecture & Pragmatic Programmer principles

from Voice.imports import say, listen_for_input
from Logic.conversation import SimBotSimulation
from Modules.dialog import SIMBOT_PERSONA, BRITTANY_PERSONA

def select_persona():
    say("Please choose a persona: Number One  or Number Two.")
    while True:
        user_input = listen_for_input().lower()
        if "number one" in user_input:
            return SIMBOT_PERSONA
        elif "number two" in user_input:
            return BRITTANY_PERSONA
        else:
            say("Invalid choice. Please say 'Number One' or 'Number Two'.")

def main():
    persona = select_persona()
    simulation = SimBotSimulation(persona, say, listen_for_input)
    simulation.run()

if __name__ == "__main__":
    main()

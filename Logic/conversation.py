import time
from Modules.dialog import keyword_match

# This code creates a class of the SimBot Personas and runs the simulation based on the dialog flows defined in Modules/dialog.py.
# The logic of the simulation is to go through each stage of the dialog flow, listen for user input, and respond based on whether the input matches the advance keywords for that stage. If the user input matches, it advances to the next stage. If not, it provides prompts and hints to guide the user towards the correct response. The simulation can be exited at any time by saying "quit", "exit", or "stop".
# Creating a class for the SimBot Simulation allows more personalities to be added in the future.


class SimBotSimulation:
    def __init__(self, persona, say_func, listen_func):
        self.persona = persona
        self.dialogue_flow = persona.get_dialogue_flow()
        self.say = say_func
        self.listen = listen_func
        self.current_stage = 0

    def run(self):
        print(f"Starting simulation for persona: {self.persona.get_name()}")
        while self.current_stage < len(self.dialogue_flow):
            stage = self.dialogue_flow[self.current_stage]
            print(f"Starting stage: {stage['stage']}")
            stage_complete = False
            hint_given = False
            failed_attempts = 0

            while not stage_complete:
                user_input = self.listen()

                if user_input in ["quit", "exit", "stop"]:
                    self.say("Thank you for your time. Goodbye!")
                    return

                if not user_input:
                    continue

                matched = keyword_match(user_input, stage["advance_keywords"])

                if matched:
                    self.say(stage.get("prompt_if_asked", "Okay."))
                    stage_complete = True
                else:
                    failed_attempts += 1
                    if failed_attempts == 1:
                        self.say(stage.get("prompt_if_missed", "Can you explain that differently?"))
                    elif failed_attempts == 2 and not hint_given and "hint" in stage:
                        self.say(stage["hint"])
                        hint_given = True
                    elif failed_attempts >= 3:
                        self.say(stage.get("fallback", "Let’s move forward for now."))
                        stage_complete = True

            self.current_stage += 1

        print("\nSimulation complete.")
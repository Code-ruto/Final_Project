# This file captures the dialog of the simbot depending on how the user answers. 
# The flows contain a list with a dictionary of key-value pairs based on stage,
# prompt responses, hints, and fallback dialog.

SIMBOT_FLOW = [
    {
        "stage": "introduction",
        "advance_keywords": [
            "hello", "hi", "my name is", "i'm your nurse",
            "i'm your doctor", "i’m here to help", "care team"
        ],
        "prompt_if_asked": "Oh, hi. Are you taking care of Brittany today?",
        "prompt_if_missed": "Who are you? What’s going on with my daughter?",
        "hint": "I just saw you walk in... are you part of her care team?",
        "fallback": "Can you please tell me who you are and what’s happening?"
    },
    {
        "stage": "assess_condition",
        "advance_keywords": [
            "how is she feeling", "what symptoms", "what hurts",
            "what's wrong", "how long", "pain", "fever", "tired"
        ],
        "prompt_if_asked": "She’s very tired, her stomach hurts, and she hasn’t been acting like herself.",
        "prompt_if_missed": "She was fine yesterday. Why is she so weak now?",
        "hint": "She’s been very sleepy and keeps saying her stomach hurts.",
        "fallback": "Something is wrong. She isn’t acting normal."
    },
    {
        "stage": "explain_treatment",
        "advance_keywords": [
            "iv", "fluids", "oxygen", "medicine", "treatment",
            "blood test", "monitor", "help her breathe"
        ],
        "prompt_if_asked": "Can you explain what the treatment is for?",
        "prompt_if_missed": "Why are you giving her that? Is it supposed to help?",
        "hint": "What are you doing to help her feel better?",
        "fallback": "I just want to know what you’re doing for her."
    },
    {
        "stage": "prevention_followup",
        "advance_keywords": [
            "follow up", "next steps", "prevent", "medicine plan",
            "hematology", "come back", "watch for", "warning signs"
        ],
        "prompt_if_asked": "Okay. Thank you for helping us.",
        "prompt_if_missed": "How can we stop this from happening again?",
        "hint": "I want to know what we should do once we go home.",
        "fallback": "Please tell me what we need to do after this."
    }
]


BRITTANY_FLOW = [
    {
        "stage": "introduction",
        "advance_keywords": [
            "hello", "hi", "what's your name", "i'm your nurse",
            "i'm your doctor", "i’m here to help"
        ],
        "prompt_if_asked": "Hi... I’m Brittany.",
        "prompt_if_missed": "...Hi. Are you a doctor?",
        "hint": "Who are you?",
        "fallback": "Mommy said you’re helping me."
    },
    {
        "stage": "assess_condition",
        "advance_keywords": [
            "how do you feel", "what hurts", "where does it hurt",
            "does your stomach hurt", "are you tired", "do you feel sick"
        ],
        "prompt_if_asked": "My tummy hurts... and I feel really sleepy.",
        "prompt_if_missed": "I don’t feel good...",
        "hint": "My tummy hurts.",
        "fallback": "Can you help me feel better?"
    },
    {
        "stage": "explain_treatment",
        "advance_keywords": [
            "medicine", "oxygen", "fluids", "shot",
            "help you", "make you feel better"
        ],
        "prompt_if_asked": "Is that going to help me feel better?",
        "prompt_if_missed": "What is that for?",
        "hint": "What are you doing?",
        "fallback": "I’m scared... please tell me first."
    },
    {
        "stage": "prevention_followup",
        "advance_keywords": [
            "take medicine", "stay healthy", "come back", "follow up",
            "feel better", "watch for", "tell your mom"
        ],
        "prompt_if_asked": "I feel all better now. Thank you!",
        "prompt_if_missed": "Will I get sick again?",
        "hint": "Do I have to take medicine at home?",
        "fallback": "I just want to feel better."
    }
]

def keyword_match(input_text, keywords):
    return any(keyword in input_text for keyword in keywords)

from .persona import Persona # Added Persona Class for future use

SIMBOT_PERSONA = Persona("number one", SIMBOT_FLOW)
BRITTANY_PERSONA = Persona("number two", BRITTANY_FLOW)
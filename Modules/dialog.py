# This file captures the dialog of the simbot depending on how the user answers. 
# The flows contain a list with a dictionary of key-value pairs based on stage,
# prompt responses, hints, and fallback dialog.

SIMBOT_FLOW = [
    {
        "stage": "introduction",
        "advance_keywords": ["hello", "hi", "my name is", "i'm your nurse", "i’m here"],
        "prompt_if_asked": "Oh, hi. Is something wrong with Brittany?",
        "prompt_if_missed": "Who are you? What’s going on with my daughter?",
        "hint": "I just saw you walk in... are you part of her care team?",
        "fallback": "I’m just trying to understand… can you please tell me what’s going on?"
    },
    {
        "stage": "ask_condition",
        "advance_keywords": ["how is she", "what's wrong", "change", "different", "symptoms"],
        "prompt_if_asked": "She’s so tired and exhausted. I’ve never seen her like this.",
        "prompt_if_missed": "Why do they keep checking her spleen and drawing blood?",
        "hint": "She was running around just yesterday… this isn’t like her.",
        "fallback": "Something’s wrong. I know it. I just need someone to say it."
    },
    {
        "stage": "call_provider",
        "advance_keywords": ["call", "help", "doctor", "get provider", "emergency"],
        "prompt_if_asked": "Please get someone—she needs help right now!",
        "prompt_if_missed": "What’s happening to my baby? Do something! Get the doctor!",
        "hint": "She doesn’t look right—please, can someone come see her now?",
        "fallback": "Please… even if you don’t know yet, just get someone to help her."
    },
    {
        "stage": "explain_treatment",
        "advance_keywords": ["fluid", "bolus", "iv", "treatment", "oxygen"],
        "prompt_if_asked": "Tell me why you’re doing that. Is that going to help her?",
        "prompt_if_missed": "What is that for? Is she going to be okay?",
        "hint": "Is that going to make her feel better soon?",
        "fallback": "Even if you can’t explain, please make sure it helps her."
    },
    {
        "stage": "reassurance",
        "advance_keywords": ["she's stable", "monitoring", "okay", "safe", "watching her", "reassure"],
        "prompt_if_asked": "Okay. I just want to understand what’s happening.",
        "prompt_if_missed": "I’m trying to stay calm, but I don’t know what’s going on.",
        "hint": "Please just tell me she’s going to be okay.",
        "fallback": "I just need to hear that she’ll be okay. That’s all."
    },
    {
        "stage": "prevention",
        "advance_keywords": ["follow up", "prevention", "happen again", "hematology", "plan"],
        "prompt_if_asked": "Thank you… I’ll make sure we follow up.",
        "prompt_if_missed": "We can’t go through this again. There has to be a way to keep her safe.",
        "hint": "I don’t want to end up back in the ER like this again.",
        "fallback": "I’ll follow whatever plan you give me. I just don’t want this again."
    },
    {
        "stage": "closure",
        "advance_keywords": ["goodbye", "let me know", "call me", "finished", "take care"],
        "prompt_if_asked": "Thank you for helping her. I just want her to be okay.",
        "prompt_if_missed": "Please don’t forget to update me if anything changes.",
        "hint": "I’ll be right here if anything changes.",
        "fallback": "Thanks for being here. I’m going to stay close by, just in case."
    }
]


BRITTANY_FLOW = [
    {
        "stage": "introduction",
        "advance_keywords": ["hello", "hi", "what's your name", "how are you"],
        "prompt_if_asked": "Hi... I’m Brittany.",
        "prompt_if_missed": "...Hi. Are you a doctor?",
        "hint": "Who are you?",
        "fallback": "Mommy said you’re helping me. Are you nice?"
    },
    {
        "stage": "ask_condition",
        "advance_keywords": ["how are you", "how do you feel", "what hurts", "what's wrong"],
        "prompt_if_asked": "My tummy hurts... and I feel sleepy.",
        "prompt_if_missed": "I don’t feel good...",
        "hint": "Ouch! It hurts.",
        "fallback": "Can you help me feel better?"
    },
    {
        "stage": "call_provider",
        "advance_keywords": ["call", "help", "nurse", "doctor", "get someone"],
        "prompt_if_asked": "Will they help me?",
        "prompt_if_missed": "Mommy! I feel weird...",
        "hint": "You can say you’ll call someone to help me.",
        "fallback": "I don’t like this... I want someone else here."
    },
    {
        "stage": "explain_treatment",
        "advance_keywords": ["iv", "medicine", "shot", "oxygen", "fluids"],
        "prompt_if_asked": "Is that going to hurt?",
        "prompt_if_missed": "What is that? I don’t like tubes...",
        "hint": "What are you doing?",
        "fallback": "I’m scared. Please tell me first."
    },
    {
        "stage": "reassurance",
        "advance_keywords": ["you're okay", "you're safe", "we're watching", "it's helping", "you're getting better"],
        "prompt_if_asked": "Okay... I’m trying to be brave.",
        "prompt_if_missed": "Is it gonna be okay?",
        "hint": "You can tell me it’s going to help.",
        "fallback": "I wanna go home..."
    },
    {
        "stage": "prevention",
        "advance_keywords": ["won't happen again", "follow up", "medicine plan", "stay safe"],
        "prompt_if_asked": "I don’t wanna be back here again...",
        "prompt_if_missed": "I don’t like this place...",
        "hint": "Do I have to take yucky medicine?",
        "fallback": "Will I get sick again?"
    },
    {
        "stage": "closure",
        "advance_keywords": ["goodbye", "all done", "rest now", "feel better", "thank you"],
        "prompt_if_asked": "Okay... bye-bye.",
        "prompt_if_missed": "Are we done now?",
        "hint": "Can I go home now?",
        "fallback": "I want to go home."
    }
]

def keyword_match(input_text, keywords):
    return any(keyword in input_text for keyword in keywords)

from .persona import Persona # Added Persona Class for future use

SIMBOT_PERSONA = Persona("number one", SIMBOT_FLOW)
BRITTANY_PERSONA = Persona("number two", BRITTANY_FLOW)
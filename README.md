# Gemini-Live-Agent-Challenge
Live agent challenge for gemini hackathon, adding code here for Cpts 360 class EA-1

The idea is to make a live agent that can read emails given to it, to try and see if 
there are any phishing related issues present in the email. The agent will scan the email
then it will conversate with the user and explain to them if there are any problems with the email
presented in a understandable manner to the average person who may not have an eye for certain
phishing red-flags that may be apparent to a more tech savvy person.

This is the outline for the agent so far.
phishing-analyzer/
├── main.py               # Entry point

├── src/
│   ├── agent.py          # Gemini Live API voice agent setup

│   └── analyzer.py       # Phishing analysis logic & prompts

├── tests/

│   └── test_analyzer.py  # Unit tests

├── docs/                 # Additional documentation

├── requirements.txt

├── .env.example


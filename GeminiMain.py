from src.agent import create_agent, start_chat
from src.analyzer import build_analysis_prompt

def main():
    print("🎣 PhishGuard — Phishing Email Analyzer")
    print("=" * 45)
    print("Paste a suspicious email below, or describe it.")
    print("Type 'quit' to exit.\n")

    model = create_agent()
    chat = start_chat(model)
    
    #input for the email here
    email_input = input("📧 Paste email content here:\n> ").strip()
    if email_input.lower() == "quit":
        return
    prompt = build_analysis_prompt(email_input)
    response = chat.send_message(prompt)
    print(f"\n🛡️  PhishGuard: {response.text}\n")

#for actual conversation loop

while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Stay safe out there! 👋")
            break
        if not user_input:
            continue
        response = chat.send_message(user_input)
        print(f"\n🛡️  PhishGuard: {response.text}\n")
        
        if __name__ == "__main__":
            main()
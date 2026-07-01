"""
Jarvis AI

Application Entry Point
"""

from core.agent import chat
from voice.service import start as start_voice


def run():
    """
    Start the Jarvis application.
    """

    while True:

        print("\n" + "=" * 40)
        print("         JARVIS AI")
        print("=" * 40)
        print("1. Voice Assistant")
        print("2. Chat Assistant")
        print("3. Exit")
        print("=" * 40)

        choice = input("Select an option: ").strip()

        if choice == "1":
            try:
                start_voice()
            except KeyboardInterrupt:
                print("\nVoice Assistant stopped.")

        elif choice == "2":
            chat()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    run()
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_present_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Running menu action")
        dispatcher.utter_message(text="Welcome to our menu", buttons=[{"payload": "/ask_for_menu", "title": "📜 Menu"}])

        return []

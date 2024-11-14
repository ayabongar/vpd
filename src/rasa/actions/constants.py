from typing import Text

SERVICE_UNAVAILABLE = "A system error occurred. Please try again later."
OUTAGE_EVENT = "events"


class DEFAULT_MENU():
    custom_Json: Text = {  "type": "INTERACTIVE_LIST",
                    "text":"Main menu options", 
                    "buttons":[
                        {"payload": "/check_outage", "title": "🌍 Check outage", "desc": "Check if ther is an outage in your area."},
                        {"payload": "/option_2", "title": "⛑️ Option 2", "desc": "Description 2"},
                        {"payload": "/option_3", "title": "👑 Option 3", "desc": "Description 3"}
                ]}

from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

class ExecuteAction(Action):
    def name(self) -> Text:
        return "execute_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        command = tracker.slots['detected_command']
        parameter = tracker.slots['example_parameter']
        if command != None and parameter != None:
            dispatcher.utter_message(text="EXECUTE " + command + " " + parameter)
        return [SlotSet("example_parameter", None), SlotSet("detected_command", None)]

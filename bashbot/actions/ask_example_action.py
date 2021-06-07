from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

class AskExampleAction(Action):
    mkdir_ask = """Please give me the name of the directory to create."""
    cat_ask = """Please give me the name of the file to read."""
    rm_ask = """Please give me the name of the file to remove."""
    rmrf_ask = """Please give me the name of the directory to remove."""
    cd_ask = """Please give me the name of the directory to jump into."""

    def name(self) -> Text:
        return "ask_explain_action"

    def get_question(self, command):
        return {
            'mkdir': AskExampleAction.mkdir_ask,
            'cat': AskExampleAction.cat_ask,
            'rm': AskExampleAction.rm_ask,
            'rmrf': AskExampleAction.rmrf_ask,
            'cd': AskExampleAction.cd_ask
        }[command]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        detected_command = tracker.slots['detected_command']
        if detected_command != None:
            message = self.get_question(detected_command)
            dispatcher.utter_message(text=message)
        return []


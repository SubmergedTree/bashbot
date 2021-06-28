from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

class ExplainResetAction(Action):
    def name(self) -> Text:
        return "explain_reset_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            return [SlotSet("example_parameter", None), SlotSet("detected_command", None)]

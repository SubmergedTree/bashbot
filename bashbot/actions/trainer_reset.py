from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

class ResetTrainerAction(Action):
    def name(self) -> Text:
        return "reset_trainer_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("cd_answer", None),
            SlotSet("mkdir_answer", None),
            SlotSet("cat_answer", None),
            SlotSet("rm_answer", None),
            SlotSet("rmrf_answer", None)]

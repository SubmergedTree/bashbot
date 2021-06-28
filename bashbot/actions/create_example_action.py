from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

class CreateExampleAction(Action):
    mkdir_example = "\"mkdir %s\""
    cat_example = "\"cat %s\""
    rm_example = "\"rm %s\""
    rmrf_example = "\"rm -rf %s\""
    cd_example = "\"cd %s\""

    def name(self) -> Text:
        return "create_example_action"

    def build_example(self, command, parameter):
        return {
            'mkdir': CreateExampleAction.mkdir_example % parameter,
            'cat': CreateExampleAction.cat_example % parameter,
            'rm': CreateExampleAction.rm_example % parameter,
            'rmrf': CreateExampleAction.rmrf_example % parameter,
            'cd': CreateExampleAction.cd_example % parameter
        }[command]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        command = tracker.slots['detected_command']
        parameter = tracker.slots['example_parameter']
        if command != None and parameter != None:
            example = self.build_example(command, parameter)
            dispatcher.utter_message(text=example)
            return [SlotSet("example_parameter", None), SlotSet("detected_command", None)] #todo reset in seperate action becase of execute
        else:
            return []

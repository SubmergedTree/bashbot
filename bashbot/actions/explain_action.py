from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

class ExplainAction(Action):
    mkdir_explanation = """Use \"mkdir <name>\" to create a new directory"""
    cat_explanation = """Use \"cat <filename>\" to read a file"""
    rm_explanation = """Use \"rm <filename>\" to delete a file"""
    rmrf_explanation = """Use \"rm -rf <name>\" to delete a new directory"""
    cd_explanation = """Use \"cd <name>\" to jump into a directory"""

    def name(self) -> Text:
        return "explain_action"

    def get_explanation_from_intent(self, command):
        return {
            'explain_mkdir': ('mkdir', ExplainAction.mkdir_explanation),
            'explain_cat': ('cat', ExplainAction.cat_explanation),
            'explain_rm': ('rm', ExplainAction.rm_explanation),
            'explain_rmrf': ('rmrf', ExplainAction.rmrf_explanation),
            'explain_cd': ('cd', ExplainAction.cd_explanation)
        }[command]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # todo get text and do keyword matching with levenshtein distance
        intent = tracker.latest_message['intent']['name']
        if intent != None:
            (command, description) = self.get_explanation_from_intent(intent)
            dispatcher.utter_message(text=description)
            dispatcher.utter_message(text="Do you need an example?")
            return [SlotSet("detected_command", command)]
        else:
            return []


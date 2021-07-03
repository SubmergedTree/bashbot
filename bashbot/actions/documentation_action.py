from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

import subprocess

class DocumentationAction(Action):
    def name(self) -> Text:
        return "documentation_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        detected_command = tracker.slots['detected_command']
        if detected_command == None:
            dispatcher.utter_message(text="Sorry I did not understand you")
            return []
        docs = self.query_man_pages(detected_command)
        dispatcher.utter_message(text=docs)
        return []

    def query_man_pages(self, command):
        filtered_command = self.filter_rmrf(command)
        process = subprocess.Popen(["man", "--pager=cat", filtered_command],
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        print(stderr.decode("utf-8"))
        return stdout.decode("utf-8").replace("\n\n", "\n")   

    def filter_rmrf(self, command):
        if command == "rmrf":
            return "rm"
        return command

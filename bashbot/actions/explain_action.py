from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

from Levenshtein import distance as levenshtein_distance

class ExplainAction(Action):
    mkdir_explanation = """Use \"mkdir <name>\" to create a new directory"""
    cat_explanation = """Use \"cat <filename>\" to read a file"""
    rm_explanation = """Use \"rm <filename>\" to delete a file"""
    rmrf_explanation = """Use \"rm -rf <name>\" to delete a new directory"""
    cd_explanation = """Use \"cd <name>\" to jump into a directory"""

    explain_command_matcher = {
        'explain_mkdir': [["create", "make"], ["folder", "directory"]],
        'explain_cat': [["read", "open", "show"], ["file"]],
        'explain_rm': [["remove", "delete"], ["file"]],
        'explain_rmrf': [["remove", "delete"], ["folder", "directory"]],
        'explain_cd': [["change", "jump"], ["folder", "directory"]]
    }

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

        fallback_intent = tracker.latest_message['intent']['name']
        print(tracker.latest_message['text'])
        print(self.detect_command(tracker.latest_message['text']))
        intent = self.detect_command(tracker.latest_message['text'])
        if intent == 'N/A':
            intent = fallback_intent
        print("Detected intent " + intent)
        if intent != None:
            (command, description) = self.get_explanation_from_intent(intent)
            dispatcher.utter_message(text=description)
            dispatcher.utter_message(text="Do you need an example or more documentation?")
            return [SlotSet("detected_command", command)]
        else:
            return []


    def detect_command(self, input_sentence):
        splitted_input = input_sentence.split()
        best = {
            'distance': 10000,
            'what': 'N/A'
        }
        for command, to_match in ExplainAction.explain_command_matcher.items():
            new_distance = self.calc_distance(splitted_input, to_match)
            if new_distance < best['distance']:
                best['distance'] = new_distance
                best['what'] = command
        return best['what']


    def calc_distance(self, input_sentence, to_match):
        verb_matchers = to_match[0]
        object_matchers = to_match[1]
        verb_distance = self.distance_of_matcher_in_sentence(input_sentence, verb_matchers)
        object_distance = self.distance_of_matcher_in_sentence(input_sentence, object_matchers)
        return (verb_distance + object_distance) / 2


    def distance_of_matcher_in_sentence(self, input_sentence, matchers):
        smallest_distance = 10000
        for matcher in matchers:
            for word in input_sentence:
                distance = levenshtein_distance(word, matcher)
                if (distance < smallest_distance):
                    smallest_distance  = distance
        return smallest_distance

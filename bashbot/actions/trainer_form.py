from typing import Any, Text, Dict, List, Optional
import random


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict


class ValidateTrainerForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_trainer_form"

    async def required_slots(
        self,
        slots_mapped_in_domain: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Optional[List[Text]]:
      #  print(slots_mapped_in_domain)
      #  next_question = ["mkdir_answer"]
      #  if tracker.slots.get("cd_answer") is True:
      #  additional_slots.append("mkdir_answer")
      #  return slots_mapped_in_domain
        return slots_mapped_in_domain # [ "outdoor_seating"] #slots_mapped_in_domain + ["outdoor_seating"]

    def validate_cd_answer(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if self.should_deactivate(slot_value):
            return {"requested_slot":None, "quiz_aborted": True}
        if "cd foo" in slot_value:
            dispatcher.utter_message(text="correct answer")
        else:
            dispatcher.utter_message(text="wrong answer")
        return {"cd_answer": slot_value, "quiz_aborted": False}

    def validate_mkdir_answer(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if self.should_deactivate(slot_value):
            return {"requested_slot":None, "quiz_aborted": True}
        if "mkdir foo" in slot_value:
            dispatcher.utter_message(text="correct answer")
        else:
            dispatcher.utter_message(text="wrong answer")
        return {"cd_answer": slot_value, "quiz_aborted": False}

    def validate_cat_answer(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if self.should_deactivate(slot_value):
            return {"requested_slot":None, "quiz_aborted": True}
        if "cat foo" in slot_value:
            dispatcher.utter_message(text="correct answer")
        else:
            dispatcher.utter_message(text="wrong answer")
        return {"cd_answer": slot_value, "quiz_aborted": False}

    def validate_rm_answer(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if self.should_deactivate(slot_value):
            return {"requested_slot":None, "quiz_aborted": True}
        if "rm foo" in slot_value:
            dispatcher.utter_message(text="correct answer")
        else:
            dispatcher.utter_message(text="wrong answer")
        return {"cd_answer": slot_value, "quiz_aborted": False}

    def validate_rmrf_answer(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if self.should_deactivate(slot_value):
            return {"requested_slot":None, "quiz_aborted": True}
        if "rm -rf foo" in slot_value:
            dispatcher.utter_message(text="correct answer")
        else:
            dispatcher.utter_message(text="wrong answer")
        return {"cd_answer": slot_value, "quiz_aborted": False}

    def should_deactivate(self, message):
        return "stop" in message or "deactivate" in message or "leave" in message or "quit" in message or "exit quiz" in message or "exit" in message
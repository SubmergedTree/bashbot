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
     #   return slots_mapped_in_domain
        
        return  [ "outdoor_seating"] #slots_mapped_in_domain + ["outdoor_seating"]


    def validate_cd_answer(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value == "cd foo": # TODO do not use ==. check if wantend substring is in message. 
            dispatcher.utter_message(text="correct answer")
        else:
            dispatcher.utter_message(text="wrong answer")
        return {"cd_answer": slot_value}


    def validate_mkdir_answer(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value == "mkdir foo":
            dispatcher.utter_message(text="correct answer")
        else:
            dispatcher.utter_message(text="wrong answer")
        return {"cd_answer": slot_value}


  #  async def extract_outdoor_seating(
  #      self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
  #  ) -> Dict[Text, Any]:
  #      text_of_last_user_message = tracker.latest_message.get("text")
  #      print(text_of_last_user_message)
  #      sit_outside = "outdoor" in text_of_last_user_message
  #      return {"outdoor_seating": sit_outside}
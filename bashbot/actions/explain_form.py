from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


#TODO search for keywords eg. delete and directory to print hint how to delete a directory
# TODO should be an Action https://forum.rasa.com/t/set-slot-value-in-custom-action/11891
class ValidateExplainForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_explain_form"

    @staticmethod
    def cuisine_db() -> List[Text]:
        """Database of supported cuisines"""

        return {"directory", "chinese", "french"}

    def validate_cuisine(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        message = tracker.latest_message.text


        if slot_value.lower() in self.cuisine_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"cuisine": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"cuisine": None}
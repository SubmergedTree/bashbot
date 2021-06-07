from typing import Any, Text, Dict, List, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict


class ValidateParameterForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_example_parameter_form"

    def validate_cd_answer(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value == "":
            return {"example_parameter": None}
        return {"example_parameter": slot_value}

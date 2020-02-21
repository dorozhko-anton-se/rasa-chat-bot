import requests
from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionChuckFact(Action):

    def name(self) -> Text:
        return "action_chuck_fact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(
            'https://api.chucknorris.io/jokes/random').json()
        dispatcher.utter_message(text=response['value'])

        return []


class BeerSelectionForm(FormAction):
    def name(self) -> Text:
        return "beer_selection_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["isOrganic", "hasLabels", "styleId"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "isOrganic": self.from_entity(entity="isOrganic"),
            "hasLabels": self.from_entity(entity="hasLabels"),
            "styleId": self.from_entity(entity="styleId"),
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        isOrganic = "Y" if tracker.get_slot("isOrganic") else "N"
        hasLabels = "Y" if tracker.get_slot("hasLabels") else "N"
        styleId = tracker.get_slot("styleId")

        key = "1f748a4023e7a80ab29f84834d9bd8f6"
        response = requests.get(
            "https://sandbox-api.brewerydb.com/v2/beer/random/?key={}&isOrganic={}&hasLabels={}&categoryId={}".format(key, isOrganic, hasLabels, styleId)).json()

        dispatcher.utter_message(
            text="Думаю, вам понравится {}".format(response["data"]["name"]))
        return []

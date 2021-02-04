# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_project"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Running actions serverr")
        value=(tracker.latest_message)['text']
        print(value)

        if (value=="General Link solution"):
            message = {"payload": "Links", "data": "https://www.mospi.gov.in/general-survey-solution-ni"}
        if (value=="NCAVES"):
            message = {"payload": "Links", "data": "https://www.mospi.gov.in/natural-capital-accounting-and-valuation-of-ecosystem-services-ncaves-"}
        if (value=="Data Innovation Lab"):
            message = {"payload": "Links", "data": "https://www.mospi.gov.in/di-labs-ni"}
        if (value=="National Data Bank"):
            message = {"payload": "Links", "data": "https://www.mospi.gov.in/national-data-bank"}
        if (value=="NPIQSI"):
            message = {"payload": "Links", "data": "https://www.mospi.gov.in/npiqsi"}
        dispatcher.utter_message(json_message=message)
        return []


class FAQLink(Action):

    def name(self) -> Text:
        return "action_FAQ_Link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        message = {"payload": "Links", "data": "https://www.mospi.gov.in/web/mospi/faq-s"}
        dispatcher.utter_message(json_message=message)
        return []


class Bot_Start(Action):

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = {"payload": "GIF"}
        dispatcher.utter_message(json_message=message)
        # message = {"payload": "Links", "data": "https://www.mospi.gov.in/web/mospi/faq-s"}
        # dispatcher.utter_message("Hi this is Mospi-bot at your service")
        return [UserUtteranceReverted()]

class GIF(Action):

    def name(self) -> Text:
        return "action_greet_gif"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = {"payload": "GIF"}
        dispatcher.utter_message(image="https://media.tenor.com/images/6691ce39e02f80cb5d2c62416a0d36a2/tenor.gif")
        return [UserUtteranceReverted()]

class Feedback(Action):

    def name(self) -> Text:
        return "action_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = {"payload": "Feedback"}
        dispatcher.utter_message(json_message=message)
        return []
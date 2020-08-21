# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

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

# class ActionHelloWorld(FormAction):
# 
#      def name(self) -> Text:
#          return "admission_form"
#      
# 
#      @staticmethod
#      def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#         
#         print("required_slots(tracker: Tracker)")
#         return ["name",  "ssn", "subject"]
# 
#      def submit(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any],
#      ) -> List[Dict]:
# 
#          dispatcher.utter_message(template="utter_submit")
# 
#          return []

class ActionHelloWorld(FormAction):

     def name(self) -> Text:
         return "admission_form"
     

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        
        print("required_slots(tracker: Tracker)")
        return ["name",  "aadhaar", "statename","districtname",  "cityname", "postofficename","villagename",  "muncorppanchname", "pinnumber","phone_number","mailid"]

     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        print("slot_mappings(self) ")

        return []

     def submit(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any],
     ) -> List[Dict]:

         dispatcher.utter_message(template="utter_submit")

         return []
## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## chuck path
* greet
  - utter_greet
* chuck_fact
  - action_chuck_fact

## beer path
* greet
  - utter_greet
* request_beer_selection
  - beer_selection_form
  - form{"name": "beer_selection_form"}
  - slot{"isOrganic": true}
  - slot{"hasLabels": true}
  - slot{"styleId": "7"}
  - form{"name": null}
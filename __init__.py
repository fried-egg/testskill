# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


# Visit https://docs.mycroft.ai/skill.creation for more detailed information
# on the structure of this skill and its containing folder, as well as
# instructions for designing your own skill based on this template.


# Import statements: the list of outside modules you'll be using in your
# skills, whether from other files in mycroft-core or from external libraries
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests
import json
import re
import os

__author__ = '1605044'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)

# Function to get wait time
def get_no_steps():
    # Getting the wait times for the airport code and getting the airport codes api so we can get the full airport
    # name for the response back
    r_stepcount = requests.get('http://mayar.abertay.ac.uk/~1605044/recipeskill/api.php', verify=False)
    return r_stepcount
# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"

def get_recipe_line(i):

    r_recipeline = requests.get('http://mayar.abertay.ac.uk/~1605044/recipeskill/recipe.php', params=i, verify=False)
    return r_recipeline
class BakingSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(BakingSkill, self).__init__(name="BakingSkill")

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.
    @intent_handler(IntentBuilder("").require("Lets").require("Bake"))
    def handle_lets_bake_intent(self, message):
        i = 1
        recipe_line = get_recipe_line(i)
        self.speak(recipe_line)

    @intent_handler(IntentBuilder("").require("Next").require("Step"))
    def handle_next_step_intent(self, message):
        step_no = get_no_steps()
        if i < step_no:
            i = i+1:
        recipe_line = get_recipe_line(i)
        self.speak(recipe_line)
    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return BakingSkill()

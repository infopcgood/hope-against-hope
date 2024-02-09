import json

import src.constants.preference_constants as Preference_Constants
from src.base.errors import *


# class to manage preferences (not used since it was not fully implemented)
class Preferences:
    def __init__(self):
        # save preferences into a dictionary
        self.preferences_dict = {}
        self.load_preferences()

    # load preferences from a file (JSON format)
    def load_preferences(self):
        try:
            # load and parse preferences from preferences file
            preferences_file = open(Preference_Constants.PREFERENCES_FILENAME, "r")
            preferences_json = json.load(preferences_file)
            preferences_file.close()
            # check if parsed preference data is valid
            for key in Preference_Constants.PREFERENCES_KEYS_AND_TYPES.keys():
                if key in preferences_json.keys():
                    try:
                        self.preferences_dict[key] = Preference_Constants.PREFERENCES_KEYS_AND_TYPES[key](
                            preferences_json[key])
                    except:
                        raise ValueError
                else:
                    raise InvalidPreferenceError
        except Exception as exception:
            # preferences failed to load, reset to default value
            print(f"Error while loading preferences: {type(exception)}" + (
                f"({exception.message})" if hasattr(exception, "message") else "") \
                  + ", preferences was reset to default value.")
            self.reset_preferences()
            self.load_preferences()
            return

    # set preference
    def set_preference(self, key, value):
        self.preferences_dict[key] = value
        self.save_preferences()

    # get preference by key
    def get_preference(self, key):
        return self.preferences_dict[key]

    # save modified preferences to file
    def save_preferences(self):
        preferences_file = open(Preference_Constants.PREFERENCES_FILENAME, "w")
        json.dump(self.preferences_dict, preferences_file)
        preferences_file.close()

    # reset preferences to default value
    def reset_preferences(self):
        self.preferences_dict = Preference_Constants.DEFAULT_PREFERENCES
        self.save_preferences()


preferences = Preferences()

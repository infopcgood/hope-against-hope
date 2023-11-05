import json
import src.constants.preference_constants as Preference_Constants
from src.base.errors import *


class Preferences:
    def __init__(self):
        self.preferences_dict = {}
        self.load_preferences()

    def load_preferences(self):
        try:
            preferences_file = open(Preference_Constants.PREFERENCES_FILENAME, "r")
            preferences_json = json.load(preferences_file)
            preferences_file.close()
            for key in preferences_json.keys():
                if key in Preference_Constants.PREFERENCES_KEYS_AND_TYPES.keys():
                    try:
                        self.preferences_dict[key] = Preference_Constants.PREFERENCES_KEYS_AND_TYPES[key](
                            preferences_json[key])
                    except:
                        raise ValueError
                else:
                    raise InvalidPreferenceError
        except Exception as exception:
            print(f"Error while loading preferences: {type(exception)}" + (
                f"({exception.message})" if hasattr(exception, "message") else "") \
                  + ", preferences was reset to default value.")
            self.reset_preferences()
            self.load_preferences()
            return

    def set_preference(self, key, value):
        self.preferences_dict[key] = value
        self.save_preferences()

    def get_preference(self, key):
        return self.preferences_dict[key]

    def save_preferences(self):
        preferences_file = open(Preference_Constants.PREFERENCES_FILENAME, "w")
        json.dump(self.preferences_dict, preferences_file)
        preferences_file.close()

    def reset_preferences(self):
        self.preferences_dict = Preference_Constants.DEFAULT_PREFERENCES
        self.save_preferences()


preferences = Preferences()

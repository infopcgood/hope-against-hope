import src.constants.i18n_constants as I18N_Constants
from src.base.assets import assets
from src.base.preferences import preferences


# translation and locale management class
class I18N:
    def __init__(self, lang='ko_KR'):
        # set language preferences and load language data
        self.lang = lang
        self.lang_json = assets.get_asset(I18N_Constants.I18N_DIRECTORY + self.lang + '.json')
        self.development_lang_json = assets.get_asset(
            I18N_Constants.I18N_DIRECTORY + I18N_Constants.DEVELOPMENT_LANG + '.json')

    # get string from id
    def get_string_from_id(self, string_id):
        if string_id in self.lang_json.keys():
            return self.lang_json[string_id]
        else:
            raise NotImplementedError

    # get string from reference string, useful for fast and easy translation
    def get_string_from_reference_string(self, reference_string):
        if reference_string in self.development_lang_json.values():
            if (self.development_lang_json.keys()[self.development_lang_json.values().index(reference_string)]
                    in self.lang_json.keys()):
                return self.lang_json[
                    self.development_lang_json.keys()[self.development_lang_json.values().index(reference_string)]]
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError


i18n = I18N(preferences.get_preference('lang'))

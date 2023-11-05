class InvalidPreferenceError(Exception):
    def __init__(self, value, message):
        super.__init__(value, message)
        self.message = f"Preference file has an invalid key {value} in it."

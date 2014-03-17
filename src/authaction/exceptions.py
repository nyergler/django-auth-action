class ConditionFailed(Exception):

    def __init__(self, action_hint=None, *args):
        super(ConditionFailed, self).__init__(*args)

        self.action_hint = action_hint

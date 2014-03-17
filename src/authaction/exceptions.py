class ConditionFailed(Exception):

    def __init__(self, action_hint=None, target=None, *args):
        super(ConditionFailed, self).__init__(*args)

        self.action_hint = action_hint
        self.target = target

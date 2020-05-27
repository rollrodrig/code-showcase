import json
from .question_reporter import QuestionReporter


class DemoChildrenReporter(QuestionReporter):
    def __init__(self, survey_definition):
        QuestionReporter.__init__(self, survey_definition, "DemoChildren", 1)

    def _spread_users_ids_on_each_option(self):
        children_list = [
            "Under 1 year",
            "1 year",
            "2 to 4 years",
            "5 years",
            "6 to 10 years",
            "11 or 12 years",
            "13 or 14 years",
            "15 to 17 years",
            "18 years or over",
        ]
        o = {
            'children': [],
            'no children': []
        }
        for option_id, users in self._users_responses.items():
            u = []
            for user in users:
                u.append(str(user))
            key = self._id_string[option_id]
            if key in children_list:
                key = 'children'
            else:
                key = 'no children'
            o[key] += u
        self._users_responses = o

import json
from .question_reporter import QuestionReporter


class CategoryUsageReporter(QuestionReporter):
    def __init__(self, survey_definition):
        QuestionReporter.__init__(self, survey_definition, "CategoryUsage", 1)

    def _store_option_string(self):
        valid_options = ['heavy', 'medium', 'light', 'others']
        responses = self._question['responses']
        for index, r in enumerate(responses):
            self._options_strings.append(valid_options[index])

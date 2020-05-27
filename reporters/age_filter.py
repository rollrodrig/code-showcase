import json
from .question_reporter import QuestionReporter


class AgeFilterReporter(QuestionReporter):
    def __init__(self, survey_definition):
        QuestionReporter.__init__(self, survey_definition, "AGE_FILTER", 2)

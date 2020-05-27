import json
from .question_reporter import QuestionReporter
from .multi_question_reporter import MultiQuestionReporter


class DifferentiationReporter(MultiQuestionReporter):
    def __init__(self, survey_definition):
        MultiQuestionReporter.__init__(self, survey_definition, "Differentiation", 1)

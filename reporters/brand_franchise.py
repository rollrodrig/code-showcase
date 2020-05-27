import json
from .multi_question_reporter import MultiQuestionReporter


class BrandFranchiseReporter(MultiQuestionReporter):
    def __init__(self, survey_definition):
        MultiQuestionReporter.__init__(self, survey_definition, "BrandFranchise", 1)

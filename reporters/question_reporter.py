import json
# from ...reporter import get_variable, get_question
from ..fake_data.reporter_fake import get_variable, get_question

'''
UnitTest
for testing comment line 2 and 3 and uncomment line 4, 5

This class stores:
- question detail
- question options ids
- users responses ordered by option
- generate its payload
- total users
- total users per option

# Variables
_question = {question data here}
_question_id = 33
_options_ids = [1,2]
_payload = [{questionId: 33, responseId: 1}, {questionId: 33, responseId: 2}]
_options_strings = [a,b]
_users_responses = {
    a: [11,22], // user 11 and 22 selected option 'a'
    b: [45,87]
}
_users_responses_count = {
    a: 2, // two person selected 'a' as option
    b: 2,
}
_total_users = 4
_string_id = {
    a: 1,
    b: 2,
}
_id_string = {
    1: a,
    2: b,
}
_option_index = { // the order
    a: 1, // this appear first
    b: 2, // this appear second
}
_type = 1 //-> 1 is section. 2 is variable
_name = "AgeFilter"
_filter = {
    AgeFilter: {
        a: {
            "questionId": 33,
            "total": 2,
            "type": 1,
            "users": [11,22],
            "id": 1
        },
        b: {
            "questionId": 33,
            "total": 2,
            "type": 1,
            "users": [45,87],
            "id": 1
        }
    }
}
'''


class QuestionReporter:
    def __init__(self, survey_definition, name, type):
        self._survey_definition = survey_definition
        self._name = name
        self._type = type
        self._question = None
        self._question_id = None
        self._options_strings = []
        self._brands = []
        # store the question option ids in order
        self._options_ids = []
        self._payload = []
        self._users_responses = {}
        self._option_index = {}
        self._index_option = {}
        self._total_users = 0
        self._users_responses_count = {}
        self._string_id = {}
        self._id_string = {}
        self._filter = {}
        self._users_responses_by_key = {}

    def options_ids(self):
        return self._options_ids

    def get_question_id(self):
        return self._question_id

    def brands(self):
        self._brands = self._options_strings
        return self._brands

    def option_index(self):
        return self._option_index

    def index_option(self):
        return self._index_option

    def users_responses_by_key(self):
        return self._users_responses_by_key

    def swith_user_responses(self):
        tmp = {}
        for option, users in self._users_responses.items():
            tmp.update({option: {}})
            tmp_users = {}
            for user_id in users:
                tmp_users.update({user_id: 1})
            tmp[option] = tmp_users
        self._users_responses_by_key = tmp

    def _set_option_index(self):
        for index, value in enumerate(self._options_strings):
            self._option_index.update({value: index + 1})
            self._index_option.update({str(index + 1): value})

    def _store_option_string(self):
        if len(self._options_strings) <= 0:
            for r in self._question['responses']:
                self._options_strings.append(r['contents'][0]['value'])

    def _fill_option_ids(self):
        # we are assuming that responses are in order
        # TODO, order responses by ordinal value
        for r in self._question['responses']:
            value = r['contents'][0]['value']
            self._options_ids.append(str(r['id']))

    # def _link_string_id(self):
    #     for r in self._question['responses']:
    #         value = r['contents'][0]['value']
    #         index = r['id']
    #         self._string_id.update({str(value): str(index)})
    #         self._id_string.update({str(index): str(value)})

    def _link_string_id(self):
        for index, value in enumerate(self._options_strings):
            self._string_id.update({value: self._options_ids[index]})
            self._id_string.update({self._options_ids[index]: value})

    def total_users(self):
        return self._total_users

    def total_sample(self):
        return self._total_users

    def _get_question(self):
        return get_question(self._survey_definition, self._name)

    def _get_variable(self):
        return get_variable(self._survey_definition, self._name)

    def question(self):
        return self._question

    def _store_question(self):
        tmp = {}
        if self._type == 1:
            question = self._get_question()
        elif self._type == 2:
            question = self._get_variable()
        tmp['id'] = str(question['id'])
        tmp['name'] = question['name']
        tmp['responses'] = question['responseList']['responseGroups'][0]['responses']
        self._question = tmp
        self._question_id = tmp['id']
        return self._question

    def _generate_payload(self):
        payload = []
        for o in self._options_ids:
            if self._type == 1:
                key = "questionId"
            elif self._type == 2:
                key = "variableId"
            tmp = {key: self._question_id, 'responseId': o}
            payload.append(tmp)
        self._payload = payload
        return self._payload

    def payload(self):
        return self._payload

    def store_user_responses(self, data):
        self._users_responses = data

    def _spread_users_ids_on_each_option(self):
        o = {}
        for option, users in self._users_responses.items():
            u = []
            for user in users:
                u.append(str(user))
            t = {self._id_string[option]: u}
            o.update(t)
        self._users_responses = o

    def _add_total_users_count(self, num):
        self._total_users += num

    def _count_responses(self):
        tmp = {}
        for option, users in self._users_responses.items():
            tmp.update({option: len(users)})
        self._users_responses_count = tmp

    def _count_total_users(self):
        total = 0
        for option in self._users_responses_count:
            total += self._users_responses_count[option]
        self._total_users = total

    def _add_users_responses_count(self, key, total):
        current = self._users_responses_count.get(key)
        if current is None:
            self._users_responses_count.update({key: total})
        else:
            current += total
            self._users_responses_count[key] = current

    def users_responses(self):
        return self._users_responses

    def users_responses_count(self):
        return self._users_responses_count

    def get_weights(self):
        return self._users_responses

    def build_filter(self):
        question = {}
        for k, value in self._users_responses.items():
            option = {
                "questionId": self._question_id,
                "total": self._users_responses_count[k],
                "type": self._type,
                "users": value,
                "id": ""
            }
            question.update({k: option})
        self._filter = {
            self._name: question
        }
        return self._filter

    def filter(self):
        return self._filter

    def execute(self):
        self._store_question()
        self._store_option_string()
        self._fill_option_ids()
        self._link_string_id()
        self._set_option_index()
        self._generate_payload()

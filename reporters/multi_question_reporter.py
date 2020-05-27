import json
from .question_reporter import QuestionReporter

"""
MultiQuestionReporter options are handled as other question, this is why this
class overrides many features in QuestionReporter

This class stores:
_users_responses: organice responses by brand->option-> users that marked that option
_options_ids: because each option is handled as other question, it stores those question option ids

# Variables
_options_ids = [[1,2,3],[4,5,6]]
_options_question_ids = [77,88]
_option_names = [a,b]
_brands = [coca, pepsi]
_users_responses = {
    'coca':{
        'a':[11,22,33], // users 11,22,33 selected 'a' as option
        'b':[44,55],
    },
    'pepsi':{
        'a':[22,55],
        'b':[11,44,33],
    },
}
_child_responses_ids = {
    'coca': [1,2,3], // question id and options ids
    'pepsi': [4,5,6],
}
_users_responses_count = {
    'coca':{
        'a': 3, // three persons marked 'a'
        'b': 2,
    },
    'pepsi':{
        'a': 2,
        'b': 3,
    },
}
_users_responses_heavy = {
    'coca':{'a': 3},
    'pepsi':{'a': 2},
}
_users_responses_medium = {
    'coca':{'a': 3},
    'pepsi':{'a': 2},
}
_users_responses_light = {
    'coca':{'a': 3},
    'pepsi':{'a': 2},
}
_users_responses_others = {
    'coca':{'a': 3},
    'pepsi':{'a': 2},
}
"""


class MultiQuestionReporter(QuestionReporter):
    def __init__(self, survey_definition, name, type):
        QuestionReporter.__init__(self, survey_definition, name, type)
        self._brands = []
        self._option_names = []
        self._child_responses_ids = {}
        self._questions_group = None
        self._options_question_ids = []
        self._users_responses_count = None
        self._users_responses_heavy = {}
        self._users_responses_medium = {}
        self._users_responses_light = {}
        self._users_responses_others = {}
        self._users_weight = None

    def users_responses_count(self):
        return self._users_responses_count

    def users_responses_heavy(self):
        return self._users_responses_heavy

    def users_responses_medium(self):
        return self._users_responses_medium

    def users_responses_light(self):
        return self._users_responses_light

    def users_responses_others(self):
        return self._users_responses_others

    def brands(self):
        return self._brands

    def option_names(self):
        return self._option_names

    def options_question_ids(self):
        return self._options_question_ids

    def _get_question(self):
        for section in self._survey_definition.get('sections'):
            for page in section.get('pages'):
                for question in page.get('questions'):
                    if question.get('name') == self._name:
                        self._questions_group = page.get('questions')
                        return question

    def _store_question(self):
        tmp = {}
        question = self._get_question()
        tmp['id'] = str(question['id'])
        tmp['name'] = question['name']
        tmp['primary_list'] = question['primaryResponseList']['responseGroups'][0]['responses']
        tmp['secondary_list'] = question['secondaryResponseList']['responseGroups'][0]['responses']
        self._question = tmp
        self._question_id = tmp['id']
        return self._question

    def _store_brands(self):
        for r in self._question['primary_list']:
            self._brands.append(r['contents'][0]['value'])

    def _store_option_names(self):
        for r in self._question['secondary_list']:
            self._option_names.append(r['contents'][0]['value'])

    def _get_child_responses(self):
        for q in self._questions_group:
            if str(q['parentQuestionId']) == str(self._question_id):
                responses = q['responseList']['responseGroups'][0]['responses']
                tmp_ids = self._loop_child_responses(responses)
                tmp = {str(q["id"]): tmp_ids}
                self._child_responses_ids.update(tmp)
                self._options_question_ids.append(q["id"])

    def _loop_child_responses(self, responses):
        tmp_ids = []
        for r in responses:
            tmp_ids.append(str(r['id']))
        return tmp_ids

    def _generate_payload(self):
        payload = []
        for parent_id, child_ids in self._child_responses_ids.items():
            for id in child_ids:
                tmp = {"questionId": parent_id, "responseId": id}
                payload.append(tmp)
        self._payload = payload
        return self._payload

    def _fill_option_ids(self):
        for r in self._child_responses_ids:
            self._options_ids.append(self._child_responses_ids[r])

    def _link_string_id(self):
        for index, value in enumerate(self._options_question_ids):
            self._id_string.update({str(value): self._brands[index]})
            self._string_id.update({self._brands[index]: str(value)})

    def _spread_users_ids_on_each_option(self):
        '''
        We should build somethign like this
        _users_responses = {
            'coca':{
                'a':[11,22,33], // users 11,22,33 selected 'a' as option
                'b':[44,55],
            },
            'pepsi':{
                'a':[22,55],
                'b':[11,44,33],
            },
        }
        '''
        # fase 1: transfor users ids in to array
        for question, options in self._users_responses.items():
            for opt_id, users in options.items():
                option_with_users = {}
                users_array = []
                for user in users:
                    users_array.append(user)
                options[opt_id] = users_array

        # fase 2: transform option id number in to brand name
        for question, options in self._users_responses.items():
            brand_name = self._id_string[question]
            self._users_responses.update({brand_name: options})
            del self._users_responses[question]
        return self._users_responses

    def _count_users_responses(self):
        tmp = {}
        for brand, options in self._users_responses.items():
            tmp.update({brand: {}})
            for opt, users in options.items():
                count = {opt: len(users)}
                tmp[brand].update(count)
        self._users_responses_count = tmp
        return self._users_responses_count

    def _count_responses(self):
        self._count_users_responses()

    def _count_total_users(self):
        total = 0
        for brand, options in self._users_responses_count.items():
            for option in options:
                total += self._users_responses_count[brand][option]
            '''All option have the same number of users'''
            break
        self._total_users = total

    def _urw_add_brand(self, brand):
        self._users_responses_heavy.update({brand: {}})
        self._users_responses_medium.update({brand: {}})
        self._users_responses_light.update({brand: {}})
        self._users_responses_others.update({brand: {}})

    def _urw_add_option(self, brand, option):
        self._users_responses_heavy[brand].update({option: []})
        self._users_responses_medium[brand].update({option: []})
        self._users_responses_light[brand].update({option: []})
        self._users_responses_others[brand].update({option: []})

    def _urw_add_users(self, user_id, tmp):

        # TODO, this a heavy operation, should be optimized
        if user_id in self._users_weight['heavy']:
            tmp['heavy'].append(user_id)
        if user_id in self._users_weight['medium']:
            tmp['medium'].append(user_id)
        if user_id in self._users_weight['light']:
            tmp['light'].append(user_id)
        if user_id in self._users_weight['others']:
            tmp['others'].append(user_id)

    def _urw_add_to_res(self, brand, option, tmp):
        self._users_responses_heavy[brand].update({option: tmp['heavy']})
        self._users_responses_medium[brand].update({option: tmp['medium']})
        self._users_responses_light[brand].update({option: tmp['light']})
        self._users_responses_others[brand].update({option: tmp['others']})

    def create_users_weight(self, users_weight):
        self._users_weight = users_weight
        for brand, options in self._users_responses.items():
            self._urw_add_brand(brand)
            # TODO, this should be optimized. Recomendatiom: use hash
            for option, users in options.items():
                self._urw_add_option(brand, option)
                tmp = {
                    'heavy': [],
                    'medium': [],
                    'light': [],
                    'others': [],
                }

                # TODO, this a heavy operation, should be optimized
                for user_id in users:
                    self._urw_add_users(user_id, tmp)
                self._urw_add_to_res(brand, option, tmp)

    def execute(self):
        self._store_question()
        self._store_brands()
        self._store_option_names()
        self._get_child_responses()
        self._fill_option_ids()
        self._link_string_id()
        self._generate_payload()

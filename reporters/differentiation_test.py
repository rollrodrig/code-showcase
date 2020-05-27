import unittest
import json
import copy
from .differentiation import DifferentiationReporter
from ..fake_data.reporters.survey_definition import FAKE_SURVEY_DEFINITION
from ..fake_data.reporters.differentiation_expects import EXPECTED_OPTION_NAMES
from ..fake_data.reporters.differentiation_expects import EXPECTED_BRANDS
from ..fake_data.reporters.differentiation_expects import EXPECTED_ID_STRING
from ..fake_data.reporters.differentiation_expects import EXPECTED_STRING_ID
from ..fake_data.reporters.differentiation_expects import EXPECTED_USERS_HEAVY
from ..fake_data.reporters.differentiation_expects import EXPECTED_USERS_MEDIUM
from ..fake_data.reporters.differentiation_expects import EXPECTED_USERS_LIGHT
from ..fake_data.reporters.differentiation_expects import EXPECTED_USERS_OTHERS
from ..fake_data.reporters.differentiation_expects import EXPECTED_OPTION_IDS
from ..fake_data.reporters.differentiation_expects import EXPECTED_USER_RESPONSE_COUNT
from ..fake_data.reporters.differentiation_expects import EXPECTED_USERS_RESPONSE
from ..fake_data.reporters.differentiation_expects import EXPECTED_QUESTION_IDS
from ..fake_data.reporters.differentiation_expects import EXPECTED_GROUP_CHILDS_IDS
from ..fake_data.reporters.differentiation_expects import EXPECTED_PAYLOAD
from ..fake_data.reporters.differentiation_fakes import FAKE_CMIX_RESPONSE
from ..fake_data.reporters.differentiation_fakes import FAKE_CATEGORY_USAGE


class DifferentiationReporterTestCase(unittest.TestCase):

    def test_should_store_question(self):
        print "---> test_should_store_question"
        i = DifferentiationReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        question = i.question()
        self.assertIsNotNone(i.question())
        self.assertEqual(question['name'], 'Differentiation')

    def test_should_store_brands(self):
        print "---> test_should_store_brands"
        i = DifferentiationReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        self.assertEqual(i.brands(), EXPECTED_BRANDS)

    def test_should_store_option_names(self):
        print "---> test_should_store_option_names"
        i = DifferentiationReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        self.assertEqual(i.option_names(), EXPECTED_OPTION_NAMES)

    def test_should_get_child_responses(self):
        print "---> test_should_get_child_responses"
        i = DifferentiationReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        i._get_child_responses()
        self.assertEqual(i._child_responses_ids, EXPECTED_GROUP_CHILDS_IDS)
        self.assertEqual(i.options_question_ids(), EXPECTED_QUESTION_IDS)

    def test_should_fill_option_ids(self):
        print "---> test_should_fill_option_ids"
        i = DifferentiationReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        i._get_child_responses()
        i._fill_option_ids()
        self.assertEqual(i._options_ids, EXPECTED_OPTION_IDS)

    def test_should_link_string_id(self):
        print "---> test_should_link_string_id"
        i = DifferentiationReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        i._get_child_responses()
        i._fill_option_ids()
        i._link_string_id()
        self.assertEqual(i._id_string, EXPECTED_ID_STRING)
        self.assertEqual(i._string_id, EXPECTED_STRING_ID)

    def test_should_generate_payload(self):
        print "---> test_should_generate_payload"
        i = DifferentiationReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        i._get_child_responses()
        i._fill_option_ids()
        i._link_string_id()
        i._generate_payload()
        self.assertEqual(i.payload(), EXPECTED_PAYLOAD)

    def test_should_store_user_responses(self):
        print "---> test_should_store_user_responses"
        i = DifferentiationReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        i._get_child_responses()
        i._fill_option_ids()
        i._link_string_id()
        i._generate_payload()
        i.store_user_responses(copy.deepcopy(FAKE_CMIX_RESPONSE))
        i._spread_users_ids_on_each_option()
        i._count_responses()
        i._count_total_users()
        self.assertEqual(i.users_responses(), EXPECTED_USERS_RESPONSE)

    def test_should_count_users_responses(self):
        print "---> test_should_count_users_responses"
        i = DifferentiationReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        i._get_child_responses()
        i._fill_option_ids()
        i._link_string_id()
        i._generate_payload()
        i.store_user_responses(copy.deepcopy(FAKE_CMIX_RESPONSE))
        i._spread_users_ids_on_each_option()
        i._count_responses()
        i._count_total_users()
        i._count_users_responses()
        self.assertEqual(i.users_responses_count(), EXPECTED_USER_RESPONSE_COUNT)

    def test_should_create_users_weight(self):
        print "---> test_should_create_users_weight"
        i = DifferentiationReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        i._get_child_responses()
        i._fill_option_ids()
        i._link_string_id()
        i._generate_payload()
        i.store_user_responses(copy.deepcopy(FAKE_CMIX_RESPONSE))
        i._spread_users_ids_on_each_option()
        i._count_responses()
        i._count_total_users()
        i._count_users_responses()
        i.create_users_weight(FAKE_CATEGORY_USAGE)
        self.assertEqual(i.users_responses_heavy(), EXPECTED_USERS_HEAVY)
        self.assertEqual(i.users_responses_medium(), EXPECTED_USERS_MEDIUM)
        self.assertEqual(i.users_responses_light(), EXPECTED_USERS_LIGHT)
        self.assertEqual(i.users_responses_others(), EXPECTED_USERS_OTHERS)

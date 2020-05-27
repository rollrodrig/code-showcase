import unittest
import json
import copy
from .category_usage import CategoryUsageReporter
from ..fake_data.reporters.survey_definition import FAKE_SURVEY_DEFINITION
from ..fake_data.reporters.category_usage_expects import EXPECTED_SWITCHED_USERS
from ..fake_data.reporters.category_usage_expects import EXPECTED_USERS_RESPONSES_COUNT
from ..fake_data.reporters.category_usage_expects import EXPECTED_FILTER
from ..fake_data.reporters.category_usage_expects import EXPECTED_USERS_RESPONSES
from ..fake_data.reporters.category_usage_expects import EXPECTED_PAYLOAD
from ..fake_data.reporters.category_usage_expects import EXPECTED_QUESTION
from ..fake_data.reporters.category_usage_fakes import FAKE_CMIX_RESPONSE
from ..fake_data.reporters.category_usage_fakes import FAKE_SURVEY_DEFINITION_1
from ..fake_data.reporters.category_usage_fakes import FAKE_SURVEY_DEFINITION_2


class CategoryUsageReporterTestCase(unittest.TestCase):

    def test_should_store_question(self):
        print "---> test_should_store_question"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        self.assertEqual(i.question(), EXPECTED_QUESTION)
        self.assertEqual(i._question_id, '200020700')

    def test_should_store_option_string(self):
        print "---> test_should_store_option_string"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        expected = ["heavy", "medium", "light", "others"]
        self.assertEqual(i._options_strings, expected)

        i1 = CategoryUsageReporter(FAKE_SURVEY_DEFINITION_1)
        i1._store_question()
        i1._store_option_string()
        self.assertEqual(i1._options_strings, expected)

        i2 = CategoryUsageReporter(FAKE_SURVEY_DEFINITION_2)
        i2._store_question()
        i2._store_option_string()
        self.assertEqual(i1._options_strings, expected)

    def test_should_fill_option_ids(self):
        print "---> test_should_fill_option_ids"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        self.assertEqual(i._options_ids, ["20701", "20702", "20703", "20704"])

    def test_should_link_string_id(self):
        print "---> test_should_link_string_id"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        expected = {
            "heavy": "20701",
            "medium": "20702",
            "light": "20703",
            "others": "20704"
        }
        self.assertEqual(i._string_id, expected)

    def test_should_set_option_index(self):
        print "---> test_should_set_option_index"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        expected_a = {
            "heavy": 1,
            "medium": 2,
            "light": 3,
            "others": 4,
        }
        expected_b = {
            "1": "heavy",
            "2": "medium",
            "3": "light",
            "4": "others"
        }
        self.assertEqual(i._option_index, expected_a)
        self.assertEqual(i._index_option, expected_b)
        self.assertEqual(i.option_index(), expected_a)
        self.assertEqual(i.index_option(), expected_b)

    def test_should_generate_payload(self):
        print "---> test_should_generate_payload"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        self.assertEqual(i.payload(), EXPECTED_PAYLOAD)

    def test_should_store_user_responses(self):
        print "---> test_should_store_user_responses"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(FAKE_CMIX_RESPONSE)
        self.assertEqual(i._users_responses, FAKE_CMIX_RESPONSE)

    def test_should_spread_users_ids_on_each_option(self):
        self.maxDiff = None
        print "---> test_should_spread_users_ids_on_each_option"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(FAKE_CMIX_RESPONSE)
        i._spread_users_ids_on_each_option()
        self.assertEqual(i.users_responses(), EXPECTED_USERS_RESPONSES)

    def test_should_count_responses(self):
        print "---> test_should_count_responses"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(FAKE_CMIX_RESPONSE)
        i._spread_users_ids_on_each_option()
        i._count_responses()
        self.assertEqual(i.users_responses_count(), EXPECTED_USERS_RESPONSES_COUNT)

    def test_should_count_total_users(self):
        print "---> test_should_count_total_users"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(FAKE_CMIX_RESPONSE)
        i._spread_users_ids_on_each_option()
        i._count_responses()
        i._count_total_users()
        self.assertEqual(i.total_users(), 120)

    def test_should_build_filter(self):
        print "---> test_should_build_filter"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(FAKE_CMIX_RESPONSE)
        i._spread_users_ids_on_each_option()
        i._count_responses()
        i._count_total_users()
        i.build_filter()
        self.assertEqual(i.filter(), EXPECTED_FILTER)

    def test_should_swith_user_responses(self):
        print "---> test_should_swith_user_responses"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(FAKE_CMIX_RESPONSE)
        i._spread_users_ids_on_each_option()
        i._count_responses()
        i._count_total_users()
        i.swith_user_responses()
        self.assertEqual(i._users_responses_by_key, EXPECTED_SWITCHED_USERS)

    def test_should_swith_user_responses_survey_1(self):
        print "---> test_should_swith_user_responses_survey_1"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION_1)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(FAKE_CMIX_RESPONSE)
        i._spread_users_ids_on_each_option()
        i._count_responses()
        i._count_total_users()
        i.swith_user_responses()
        self.assertEqual(i._users_responses_by_key, EXPECTED_SWITCHED_USERS)

    def test_should_swith_user_responses_survey_2(self):
        print "---> test_should_swith_user_responses_survey_2"
        i = CategoryUsageReporter(FAKE_SURVEY_DEFINITION_2)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(FAKE_CMIX_RESPONSE)
        i._spread_users_ids_on_each_option()
        i._count_responses()
        i._count_total_users()
        i.swith_user_responses()
        self.assertEqual(i._users_responses_by_key, EXPECTED_SWITCHED_USERS)

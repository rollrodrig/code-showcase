import unittest
import json
import copy
from .demo_children import DemoChildrenReporter
from ..reporter_fake import FAKE_SURVEY_DEFINITION


class DemoChildrenReporterTestCase(unittest.TestCase):

    def test_should_store_question(self):
        self.maxDiff = None
        print "---> test_should_store_question"
        i = DemoChildrenReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        self.assertEqual(i.question(), EXPECTED_QUESTION)
        self.assertEqual(i._question_id, '200020100')

    def test_should_store_option_string(self):
        self.maxDiff = None
        print "---> test_should_store_option_string"
        i = DemoChildrenReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        self.assertEqual(i._options_strings, EXPECTED_OPTION_STRING)

    def test_should_fill_option_ids(self):
        print "---> test_should_fill_option_ids"
        i = DemoChildrenReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        self.assertEqual(i._options_ids, EXPECTED_OPTION_IDS)

    def test_should_link_string_id(self):
        print "---> test_should_link_string_id"
        i = DemoChildrenReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        expected = {
            "5 years": "20105",
            "Prefer not to answer": "20111",
            "Under 1 year": "20102",
            "2 to 4 years": "20104",
            "6 to 10 years": "20106",
            "13 or 14 years": "20108",
            "18 years or over": "20110",
            "No children": "20101",
            "11 or 12 years": "20107",
            "15 to 17 years": "20109",
            "1 year": "20103"
        }
        self.assertEqual(i._string_id, expected)

    def test_should_set_option_index(self):
        print "---> test_should_set_option_index"
        i = DemoChildrenReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        expected_a = {
            "5 years": 5,
            "Prefer not to answer": 11,
            "Under 1 year": 2,
            "2 to 4 years": 4,
            "6 to 10 years": 6,
            "13 or 14 years": 8,
            "18 years or over": 10,
            "No children": 1,
            "11 or 12 years": 7,
            "15 to 17 years": 9,
            "1 year": 3
        }
        expected_b = {
            "1": "No children",
            "2": "Under 1 year",
            "3": "1 year",
            "4": "2 to 4 years",
            "5": "5 years",
            "6": "6 to 10 years",
            "7": "11 or 12 years",
            "8": "13 or 14 years",
            "9": "15 to 17 years",
            "10": "18 years or over",
            "11": "Prefer not to answer"
        }
        self.assertEqual(i._option_index, expected_a)
        self.assertEqual(i._index_option, expected_b)
        self.assertEqual(i.option_index(), expected_a)
        self.assertEqual(i.index_option(), expected_b)

    def test_should_generate_payload(self):
        print "---> test_should_generate_payload"
        i = DemoChildrenReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        self.assertEqual(i.payload(), EXPECTED_PAYLOAD)

    def test_should_store_user_responses(self):
        print "---> test_should_store_user_responses"
        i = DemoChildrenReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(DUMMY_USER_RESPONSES)
        self.assertEqual(i._users_responses, DUMMY_USER_RESPONSES)

    def test_should_spread_users_ids_on_each_option(self):
        self.maxDiff = None
        print "---> test_should_spread_users_ids_on_each_option"
        i = DemoChildrenReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(DUMMY_USER_RESPONSES)
        i._spread_users_ids_on_each_option()
        i._count_responses()
        i._count_total_users()
        self.assertEqual(i._users_responses, EXPECTED_USERS_RESPONSES)
        self.assertEqual(i.users_responses_count(), EXPECTED_USERS_RESPONSES_COUNT)
        self.assertEqual(i.total_users(), 120)

    def test_should_build_filter(self):
        print "---> test_should_build_filter"
        i = DemoChildrenReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(DUMMY_USER_RESPONSES)
        i._spread_users_ids_on_each_option()
        i._count_responses()
        i._count_total_users()
        i.build_filter()
        self.assertEqual(i.filter(), EXPECTED_FILTER)

    def test_should_swith_user_responses(self):
        print "---> test_should_swith_user_responses"
        i = DemoChildrenReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_option_string()
        i._fill_option_ids()
        i._link_string_id()
        i._set_option_index()
        i._generate_payload()
        i.store_user_responses(DUMMY_USER_RESPONSES)
        i._spread_users_ids_on_each_option()
        i._count_responses()
        i._count_total_users()
        i.swith_user_responses()
        self.assertEqual(i._users_responses_by_key, EXPECTED_SWITCHED_USERS)

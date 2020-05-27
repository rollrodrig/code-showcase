import unittest
import json
import copy
from .brand_franchise import BrandFranchiseReporter
from ..fake_data.survey_definition import FAKE_SURVEY_DEFINITION
from ..fake_data.reporters.brand_franchise_expects import EXPECTED_OPTION_NAMES
from ..fake_data.reporters.brand_franchise_expects import EXPECTED_GROUP_CHILDS_IDS
from ..fake_data.reporters.brand_franchise_expects import EXPECTED_OPTION_IDS
from ..fake_data.reporters.brand_franchise_expects import EXPECTED_PAYLOAD
from ..fake_data.reporters.brand_franchise_expects import EXPECTED_USERS_RESPONSE
from ..fake_data.reporters.brand_franchise_expects import EXPECTED_USER_RESPONSE_COUNT
from ..fake_data.reporters.brand_franchise_expects import EXPECTED_USERS_HEAVY
from ..fake_data.reporters.brand_franchise_expects import EXPECTED_USERS_MEDIUM
from ..fake_data.reporters.brand_franchise_expects import EXPECTED_USERS_LIGHT
from ..fake_data.reporters.brand_franchise_expects import EXPECTED_USERS_OTHERS
from ..fake_data.reporters.brand_franchise_fakes import FAKE_CMIX_RESPONSE
from ..fake_data.reporters.brand_franchise_fakes import FAKE_CATEGORY_USAGE


class BrandFranchiseReporterTestCase(unittest.TestCase):

    def test_should_store_question(self):
        print "---> test_should_store_question."
        i = BrandFranchiseReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        self.assertIsNotNone(i.question())

    def test_should_store_brands(self):
        print "---> test_should_store_brands"
        i = BrandFranchiseReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        self.assertEqual(i.brands(), ["cocacola", "pepsi", "sevenup"])

    def test_should_store_option_names(self):
        print "---> test_should_store_option_names"
        i = BrandFranchiseReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        self.assertEqual(i.option_names(), EXPECTED_OPTION_NAMES)

    def test_should_get_child_responses(self):
        print "---> test_should_get_child_responses"
        i = BrandFranchiseReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        i._get_child_responses()
        self.assertEqual(i._child_responses_ids, EXPECTED_GROUP_CHILDS_IDS)
        self.assertEqual(i.options_question_ids(), [200020800, 200020900, 200021000])

    def test_should_fill_option_ids(self):
        print "---> test_should_fill_option_ids"
        i = BrandFranchiseReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        i._get_child_responses()
        i._fill_option_ids()
        self.assertEqual(i._options_ids, EXPECTED_OPTION_IDS)

    def test_should_link_string_id(self):
        print "---> test_should_link_string_id"
        i = BrandFranchiseReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        i._get_child_responses()
        i._fill_option_ids()
        i._link_string_id()
        self.assertEqual(i._id_string, {"200020900": "pepsi", "200020800": "cocacola", "200021000": "sevenup"})
        self.assertEqual(i._string_id, {"cocacola": "200020800", "pepsi": "200020900", "sevenup": "200021000"})

    def test_should_get_child_responses(self):
        print "---> test_should_store_secondary_list"
        i = BrandFranchiseReporter(FAKE_SURVEY_DEFINITION)
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
        i = BrandFranchiseReporter(FAKE_SURVEY_DEFINITION)
        i._store_question()
        i._store_brands()
        i._store_option_names()
        i._get_child_responses()
        i._fill_option_ids()
        i._link_string_id()
        i._generate_payload()
        i.store_user_responses(copy.deepcopy(FAKE_CMIX_RESPONSE))
        i._spread_users_ids_on_each_option()
        self.assertEqual(i.users_responses(), EXPECTED_USERS_RESPONSE)

    def test_should_count_users_responses(self):
        print "---> test_should_count_users_responses"
        i = BrandFranchiseReporter(FAKE_SURVEY_DEFINITION)
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
        self.assertEqual(i.users_responses_count(), EXPECTED_USER_RESPONSE_COUNT)

    def test_should_count_total_users(self):
        print "---> test_should_count_total_users"
        i = BrandFranchiseReporter(FAKE_SURVEY_DEFINITION)
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
        self.assertEqual(i._total_users, 120)

    def test_should_create_users_weight(self):
        print "---> test_should_create_users_weight"
        i = BrandFranchiseReporter(FAKE_SURVEY_DEFINITION)
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
        i.create_users_weight(FAKE_CATEGORY_USAGE)
        self.assertEqual(i.users_responses_heavy(), EXPECTED_USERS_HEAVY)
        self.assertEqual(i.users_responses_medium(), EXPECTED_USERS_MEDIUM)
        self.assertEqual(i.users_responses_light(), EXPECTED_USERS_LIGHT)
        self.assertEqual(i.users_responses_others(), EXPECTED_USERS_OTHERS)

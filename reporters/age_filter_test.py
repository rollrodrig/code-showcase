import unittest
import json
import copy
from .age_filter import AgeFilterReporter
from ..reporter_fake import FAKE_SURVEY_DEFINITION


class DemoChildrenReporterTestCase(unittest.TestCase):

    def test_should_swith_user_responses(self):
        print "---> test_should_swith_user_responses"
        i = AgeFilterReporter(FAKE_SURVEY_DEFINITION)
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
        i.swith_user_responses()
        self.assertEqual(i.users_responses_count(), EXPECTED_USERS_RESPONSES_COUNT)
        self.assertEqual(i.total_users(), 120)
        self.assertEqual(i.filter(), EXPECTED_FILTER)
        self.assertEqual(i._users_responses_by_key, EXPECTED_SWITCHED_USERS)

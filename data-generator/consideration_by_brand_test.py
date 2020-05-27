import unittest
import random
import json
from ...color_brand import ColorBrand
from .consideration_by_brand import ConsiderationByBrand
from ...reporters.waves import WavesReporter
from ...reporters.brand_franchise import BrandFranchiseReporter
from ...fake_data.generator.prepost.consideration_by_brand_fakes import FAKES_CATEGORY_USAGE
from ...fake_data.generator.prepost.consideration_by_brand_fakes import FAKES_WAVES_USERS
from ...fake_data.generator.prepost.consideration_by_brand_fakes import FAKES_WAVES_USERS_COUNT
from ...fake_data.generator.prepost.consideration_by_brand_fakes import FAKES_BRAND_FRANCHISE_USERS
from ...fake_data.generator.prepost.consideration_by_brand_fakes import FAKES_BRAND_FRANCHISE_USERS_HEAVY
from ...fake_data.generator.prepost.consideration_by_brand_fakes import FAKES_BRAND_FRANCHISE_USERS_MEDIUM
from ...fake_data.generator.prepost.consideration_by_brand_fakes import FAKES_BRAND_FRANCHISE_USERS_LIGHT
from ...fake_data.generator.prepost.consideration_by_brand_fakes import FAKES_OPTION_NAMES
from ...fake_data.generator.prepost.consideration_by_brand_fakes import FAKES_OPTION_IDS
from ...fake_data.generator.prepost.consideration_by_brand_expects import EXPECTED_OPTION_IDS
from ...fake_data.generator.prepost.consideration_by_brand_expects import EXPECTED_BF_PRE_USER_COUNT
from ...fake_data.generator.prepost.consideration_by_brand_expects import EXPECTED_BF_POST_USER_COUNT
from ...fake_data.generator.prepost.consideration_by_brand_expects import EXPECTED_BF_PRE_USERS
from ...fake_data.generator.prepost.consideration_by_brand_expects import EXPECTED_BF_POST_USERS
from ...fake_data.generator.prepost.consideration_by_brand_expects import EXPECTED_WAVE_PRE_INVERTED
from ...fake_data.generator.prepost.consideration_by_brand_expects import EXPECTED_WAVE_POST_INVERTED
from ...fake_data.generator.prepost.consideration_by_brand_expects import EXPECTED_DATA

waves = WavesReporter({})
waves._users_responses = FAKES_WAVES_USERS
waves._users_responses_count = FAKES_WAVES_USERS_COUNT

brand_franchise = BrandFranchiseReporter({})
brand_franchise._users_responses = FAKES_BRAND_FRANCHISE_USERS
brand_franchise._users_responses_heavy = FAKES_BRAND_FRANCHISE_USERS_HEAVY
brand_franchise._users_responses_medium = FAKES_BRAND_FRANCHISE_USERS_MEDIUM
brand_franchise._users_responses_light = FAKES_BRAND_FRANCHISE_USERS_LIGHT
brand_franchise._option_names = FAKES_OPTION_NAMES
brand_franchise._options_ids = FAKES_OPTION_IDS


# python -m unittest discover backend.apps.popresearch.cmix.reporting.bsm.chart_generators.prepost consideration_by_brand_test.py
class ConsiderationByBrandTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "---> setUpClass"
        c = ColorBrand.getInstance()
        c.set_brands(["cocacola", "pepsi", "sevenup"])
        c.generate()

    def test_should_init_class(self):
        print "--> test_should_init_class"
        r = ConsiderationByBrand(waves, brand_franchise)
        self.assertIsNotNone(r._waves)
        self.assertIsNotNone(r._brand_franchise)
        self.assertIsNotNone(r._brand_franchise_users)
        self.assertIsNotNone(r._brand_franchise_users_heavy)
        self.assertIsNotNone(r._brand_franchise_users_medium)
        self.assertIsNotNone(r._brand_franchise_users_light)

    def test_should_filter_option_ids(self):
        print "--> test_should_filter_option_ids"
        r = ConsiderationByBrand(waves, brand_franchise)
        r._filter_option_ids()
        self.assertEqual(r._option_ids, EXPECTED_OPTION_IDS)

    def test_should_invert_wave_pre(self):
        print "--> test_should_invert_wave_pre"
        r = ConsiderationByBrand(waves, brand_franchise)
        r._filter_option_ids()
        r._invert_wave_pre()
        self.assertEqual(r._wave_pre, EXPECTED_WAVE_PRE_INVERTED)

    def test_should_invert_wave_post(self):
        print "--> test_should_invert_wave_post"
        r = ConsiderationByBrand(waves, brand_franchise)
        r._filter_option_ids()
        r._invert_wave_post()
        self.assertEqual(r._wave_post, EXPECTED_WAVE_POST_INVERTED)

    def test_should_filter_users_in(self):
        print "--> test_should_filter_users_in"
        r = ConsiderationByBrand(waves, brand_franchise)
        r._filter_option_ids()
        r._invert_waves()
        data = r._filter_users_in(r._brand_franchise_users)
        self.assertEqual(data['pre'], EXPECTED_BF_PRE_USERS)
        self.assertEqual(data['post'], EXPECTED_BF_POST_USERS)

    def test_should_filter_pre_post_users(self):
        print "--> test_should_filter_pre_post_users"
        r = ConsiderationByBrand(waves, brand_franchise)
        r._filter_option_ids()
        r._invert_waves()
        r._filter_pre_post_users()
        self.assertEqual(r._brand_franchise_pre_users, EXPECTED_BF_PRE_USERS)
        self.assertEqual(r._brand_franchise_post_users, EXPECTED_BF_POST_USERS)

    def test_should_count_pre_post_users(self):
        print "--> test_should_count_pre_post_users"
        r = ConsiderationByBrand(waves, brand_franchise)
        r._filter_option_ids()
        r._invert_waves()
        r._filter_pre_post_users()
        r._count_pre_post_users()
        self.assertEqual(r._brand_franchise_pre_users, EXPECTED_BF_PRE_USER_COUNT)
        self.assertEqual(r._brand_franchise_post_users, EXPECTED_BF_POST_USER_COUNT)

    def test_should_build_chart(self):
        print "--> test_should_build_chart"
        r = ConsiderationByBrand(waves, brand_franchise)
        r._filter_option_ids()
        r._invert_waves()
        r._filter_pre_post_users()
        r._count_pre_post_users()
        r._build_chart()
        # print json.dumps(r.data())
        self.assertEqual(r.data(), EXPECTED_DATA)

    def test_should_generate(self):
        print "--> test_should_generate"
        r = ConsiderationByBrand(waves, brand_franchise)
        r.generate()
        self.assertEqual(r.data(), EXPECTED_DATA)

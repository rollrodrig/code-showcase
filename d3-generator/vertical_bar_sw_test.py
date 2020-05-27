import unittest
import json
from random import random
from .vertical_bar_sw import VerticalBarSW
from ..fake_data.charts.vertical_bar_sw_fakes import FAKES_OPTION_NAMES
from ..fake_data.charts.vertical_bar_sw_fakes import FAKES_OPTION_IDS
from ..fake_data.charts.vertical_bar_sw_fakes import FAKES_RESPONSES
from ..fake_data.charts.vertical_bar_sw_expects import EXPECTED_USERS_BY_BRAND
from ..fake_data.charts.vertical_bar_sw_expects import EXPECTED_CHART_NAME_IDS
from ..fake_data.charts.vertical_bar_sw_expects import EXPECTED_DATA_CHART
from ..fake_data.charts.vertical_bar_sw_expects import EXPECTED_DATA


# python -m unittest discover backend.apps.popresearch.cmix.reporting.bsm.charts vertical_bar_sw_test.py
class StackedBarTestCase(unittest.TestCase):
    def test_should_init(self):
        print "----> test_should_init"
        r = VerticalBarSW(FAKES_RESPONSES, FAKES_OPTION_NAMES, FAKES_OPTION_IDS)

    def test_should_count_total_sample(self):
        print "----> test_should_count_total_sample"
        r = VerticalBarSW(FAKES_RESPONSES, FAKES_OPTION_NAMES, FAKES_OPTION_IDS)
        r._count_total_sample()
        self.assertEqual(r.total_sample(), 120)

    def test_should_count_users_by_brand(self):
        print "----> test_should_count_users_by_brand"
        r = VerticalBarSW(FAKES_RESPONSES, FAKES_OPTION_NAMES, FAKES_OPTION_IDS)
        r._count_total_sample()
        r._fill_data_titles()
        r._count_users_by_brand()
        self.assertEqual(r._users_by_brand, EXPECTED_USERS_BY_BRAND)

    def test_should_count_users_by_brand(self):
        print "----> test_should_count_users_by_brand"
        r = VerticalBarSW(FAKES_RESPONSES, FAKES_OPTION_NAMES, FAKES_OPTION_IDS)
        r._count_total_sample()
        r._fill_data_titles()
        r._count_users_by_brand()
        r._def_trial_aware_ids()
        r._def_current_trialist()
        r._def_attracted_nontrialists()
        r._def_loyalists_current()
        self.assertEqual(r._chart_name_ids, EXPECTED_CHART_NAME_IDS)

    def test_should_count_users(self):
        print "----> test_should_count_users"
        r = VerticalBarSW(FAKES_RESPONSES, FAKES_OPTION_NAMES, FAKES_OPTION_IDS)
        r._count_total_sample()
        r._fill_data_titles()
        r._count_users_by_brand()
        a_question_indexs = [4, 5, 6, 7]
        b_question_indexs = [1, 2, 3, 4, 5, 6, 7]
        total_users_by_index = [2, 2, 4, 0, 3, 3, 2, 2]
        '''10*100/16 = 62.5%'''
        calc = r._count_users(a_question_indexs, b_question_indexs, total_users_by_index)
        self.assertEqual(calc, {"a": 10, "p": 62.5, "b": 16})

    def test_should_calc_competitive_charts(self):
        print "----> test_should_calc_competitive_charts"
        r = VerticalBarSW(FAKES_RESPONSES, FAKES_OPTION_NAMES, FAKES_OPTION_IDS)
        r._count_total_sample()
        r._fill_data_titles()
        r._count_users_by_brand()
        r._def_trial_aware_ids()
        r._def_current_trialist()
        r._def_attracted_nontrialists()
        r._def_loyalists_current()
        r._calc_competitive_charts()
        self.assertEqual(r._data_chart, EXPECTED_DATA_CHART)

    def test_should_fill_data(self):
        print "----> test_should_fill_data"
        r = VerticalBarSW(FAKES_RESPONSES, FAKES_OPTION_NAMES, FAKES_OPTION_IDS)
        r._count_total_sample()
        r._fill_data_titles()
        r._count_users_by_brand()
        r._def_trial_aware_ids()
        r._def_current_trialist()
        r._def_attracted_nontrialists()
        r._def_loyalists_current()
        r._calc_competitive_charts()
        r._fill_data()
        self.assertIsNotNone(r._data['data'])
        self.assertEqual(r.data(), EXPECTED_DATA)

    def test_should_generate(self):
        print "----> test_should_generate"
        r = VerticalBarSW(FAKES_RESPONSES, FAKES_OPTION_NAMES, FAKES_OPTION_IDS)
        r.generate()
        self.assertIsNotNone(r._data['data'])
        self.assertEqual(r.data(), EXPECTED_DATA)

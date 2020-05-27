import unittest
import json
from .awareness_consideration_chart import AwarenessConsiderationChart
from ..fake_data.charts.awareness_consideration_chart_fake_data import FAKE_OPTION_NAMES
from ..fake_data.charts.awareness_consideration_chart_fake_data import FAKE_OPTION_IDS
from ..fake_data.charts.awareness_consideration_chart_fake_data import FAKE_BRAND_FRANCHISE_RES
from ..fake_data.charts.awareness_consideration_chart_fake_data import FAKE_BRAND_PREF_RESPONSE
from ..fake_data.charts.awareness_consideration_chart_expected import EXPECTED_PERCENTS
from ..fake_data.charts.awareness_consideration_chart_expected import EXPECTED_DATA
from ..fake_data.charts.awareness_consideration_chart_expected import EXPECTED_RESPONSES_COUNT


# python -m unittest discover backend.apps.popresearch.cmix.reporting.bsm.charts  awareness_consideration_chart_test.py
class AwarenessConsiderationChartTestCase(unittest.TestCase):

    def test_should_init_class(self):
        print "test_should_init_class"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)

    def test_should_calc_response_count(self):
        print "test_should_calc_response_count"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        self.assertEqual(r._responses_count, EXPECTED_RESPONSES_COUNT)

    def test_should_count_total_sample(self):
        print "test_should_count_total_sample"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        r._count_total_sample()
        self.assertEqual(r._total_sample, 120)

    def test_should_to_percent(self):
        print "test_should_to_percent"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        r._count_total_sample()
        percent = r._to_percent(60)
        self.assertEqual(percent, 50)
        percent = r._to_percent(12)
        self.assertEqual(percent, 10)
        percent = r._to_percent(100)
        self.assertEqual(percent, 83.3)

    def test_should_create_x(self):
        print "test_should_create_x"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        r._count_total_sample()
        r._create_x()
        self.assertEqual(r._x, ['pepsi', 'cocacola', 'inkacola', 'sevenup'])

    def test_should_create_values_aware(self):
        print "test_should_create_values_aware"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        r._count_total_sample()
        r._create_x()
        r._create_values_aware()
        self.assertEqual(r._values_aware, [92.5, 88.3, 89.2, 93.3])

    def test_should_create_values_consider(self):
        print "test_should_create_values_consider"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        r._count_total_sample()
        r._create_x()
        r._create_values_consider()
        self.assertEqual(r._values_consider, [25.0, 39.2, 38.3, 25.8])

    def test_should_create_values_use(self):
        print "test_should_create_values_use"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        r._count_total_sample()
        r._create_x()
        r._create_values_use()
        self.assertEqual(r._values_use, [21.7, 25.0, 25.0, 15.0])

    def test_should_count_brand_pref_percents(self):
        print "test_should_count_brand_pref_percents"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        r._count_total_sample()
        r._create_x()
        r._count_brand_pref_percents()
        expected = {
            "pepsi": 28.3,
            "others": 7.5,
            "cocacola": 20.8,
            "inkacola": 22.5,
            "sevenup": 20.8
        }
        self.assertEqual(r._brand_preference, expected)

    def test_should_create_values_prefer(self):
        print "test_should_create_values_prefer"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        r._count_total_sample()
        r._create_x()
        r._create_values_prefer()
        self.assertEqual(r._values_prefer, [28.3, 20.8, 22.5, 20.8])

    def test_should_create_values(self):
        print "test_should_create_values"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        r._count_total_sample()
        r._create_x()
        r._create_values()
        expected = [
            [92.5, 88.3, 89.2, 93.3],
            [25.0, 39.2, 38.3, 25.8],
            [21.7, 25.0, 25.0, 15.0],
            [28.3, 20.8, 22.5, 20.8]
        ]
        self.assertEqual(r._values, expected)

    def test_should_create_percents(self):
        print "test_should_create_percents"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        r._count_total_sample()
        r._create_x()
        r._create_values()
        r._create_percents()
        self.assertEqual(r._s, EXPECTED_PERCENTS)

    def test_should_fill_data(self):
        print "test_should_fill_data"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r._calc_response_count()
        r._count_total_sample()
        r._create_x()
        r._create_values()
        r._create_percents()
        r.survey_type("singlewave")
        r._fill_data()
        self.assertEqual(r._data, EXPECTED_DATA)

    def test_should_generate(self):
        print "test_should_fill_data"
        r = AwarenessConsiderationChart(18, FAKE_BRAND_FRANCHISE_RES, FAKE_OPTION_NAMES, FAKE_OPTION_IDS, FAKE_BRAND_PREF_RESPONSE)
        r.survey_type("singlewave")
        r.generate()
        self.assertEqual(r._data, EXPECTED_DATA)

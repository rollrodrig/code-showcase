import unittest
import json
from .simple_linepath import SimpleLinepath
from ..color_brand import ColorBrand
from ..fake_data.charts.simple_linepath_fakes import FAKES_OPTIONS_TO_CONSIDER
from ..fake_data.charts.simple_linepath_fakes import FAKE_PRE_RESPONSES
from ..fake_data.charts.simple_linepath_fakes import FAKE_POST_RESPONSES
from ..fake_data.charts.simple_linepath_expects import EXPECTED_BRANDS
from ..fake_data.charts.simple_linepath_expects import EXPECTED_PRE_PERCENTS
from ..fake_data.charts.simple_linepath_expects import EXPECTED_POST_PERCENTS
from ..fake_data.charts.simple_linepath_expects import EXPECTED_LINES
from ..fake_data.charts.simple_linepath_expects import EXPECTED_DATA


class SimpleLinepathTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "---> setUpClass"
        c = ColorBrand.getInstance()
        c.set_brands(["cocacola", "pepsi", "sevenup"])
        c.generate()

    def test_should_init(self):
        print "----> test_should_init"
        r = SimpleLinepath(FAKE_PRE_RESPONSES, FAKE_POST_RESPONSES, FAKES_OPTIONS_TO_CONSIDER)
        self.assertIsNotNone(r._pre_responses)
        self.assertIsNotNone(r._post_responses)
        self.assertIsNotNone(r._option_ids)

    def test_should_fill_brands(self):
        print "----> test_should_fill_brands"
        r = SimpleLinepath(FAKE_PRE_RESPONSES, FAKE_POST_RESPONSES, FAKES_OPTIONS_TO_CONSIDER)
        r._fill_brands()
        self.assertEqual(r._brands, EXPECTED_BRANDS)

    def test_should_calc_total_sample(self):
        print "----> test_should_calc_total_sample"
        r = SimpleLinepath(FAKE_PRE_RESPONSES, FAKE_POST_RESPONSES, FAKES_OPTIONS_TO_CONSIDER)
        r._fill_brands()
        r._calc_total_samples()
        self.assertEqual(r._total_pre_sample, 200)
        self.assertEqual(r._total_pre_sample, 200)

    def test_should_calc_option_percents(self):
        print "----> test_should_calc_option_percents"
        r = SimpleLinepath(FAKE_PRE_RESPONSES, FAKE_POST_RESPONSES, FAKES_OPTIONS_TO_CONSIDER)
        r._fill_brands()
        r._calc_total_samples()
        data = r._calc_option_percents(r._pre_responses, r._total_pre_sample)
        self.assertEqual(data, EXPECTED_PRE_PERCENTS)

    def test_should_calc_percents_by_brand(self):
        print "----> test_should_calc_percents_by_brand"
        r = SimpleLinepath(FAKE_PRE_RESPONSES, FAKE_POST_RESPONSES, FAKES_OPTIONS_TO_CONSIDER)
        r._fill_brands()
        r._calc_total_samples()
        r._calc_percents_by_brand()
        self.assertEqual(r._pre_responses, EXPECTED_PRE_PERCENTS)
        self.assertEqual(r._post_responses, EXPECTED_POST_PERCENTS)

    def test_should_fill_lines(self):
        print "----> test_should_fill_lines"
        r = SimpleLinepath(FAKE_PRE_RESPONSES, FAKE_POST_RESPONSES, FAKES_OPTIONS_TO_CONSIDER)
        r._fill_brands()
        r._calc_total_samples()
        r._calc_percents_by_brand()
        r._fill_lines()
        self.assertEqual(r._lines, EXPECTED_LINES)

    def test_should_buil_chart(self):
        print "----> test_should_buil_chart"
        r = SimpleLinepath(FAKE_PRE_RESPONSES, FAKE_POST_RESPONSES, FAKES_OPTIONS_TO_CONSIDER)
        r._fill_brands()
        r._calc_total_samples()
        r._calc_percents_by_brand()
        r._fill_lines()
        r._buil_chart()
        self.assertEqual(r.data(), EXPECTED_DATA)

    def test_should_generate(self):
        print "----> test_should_generate"
        r = SimpleLinepath(FAKE_PRE_RESPONSES, FAKE_POST_RESPONSES, FAKES_OPTIONS_TO_CONSIDER)
        r.generate()
        self.assertEqual(r.data(), EXPECTED_DATA)

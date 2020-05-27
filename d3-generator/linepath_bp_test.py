import unittest
import json
from .linepath_bp import LinepathBP
from ..color_brand import ColorBrand
from ..fake_data.charts.linepath_bp_fakes import FAKE_RESPONSES
from ..fake_data.charts.linepath_bp_expects import EXPECTED_COUNT_BY_WAVE
from ..fake_data.charts.linepath_bp_expects import EXPECTED_LABELS
from ..fake_data.charts.linepath_bp_expects import EXPECTED_BRANDS
from ..fake_data.charts.linepath_bp_expects import EXPECTED_OPTION_PERCENTAGES
from ..fake_data.charts.linepath_bp_expects import EXPECTED_LINES
from ..fake_data.charts.linepath_bp_expects import EXPECTD_BUILDED_LINES
from ..fake_data.charts.linepath_bp_expects import EXPECTED_DATA


class LinepathBPTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "---> setUpClass"
        c = ColorBrand.getInstance()
        c.set_brands(["cocacola", "pepsi", "sevenup", "others"])
        c.generate()

    def test_should_init(self):
        print "---> test_should_init"
        r = LinepathBP(FAKE_RESPONSES)
        self.assertIsNotNone(r._responses)

    def test_should_fill_labels(self):
        print "----> test_should_fill_labels"
        r = LinepathBP(FAKE_RESPONSES)
        r._fill_labels()
        self.assertEqual(r._labels, EXPECTED_LABELS)

    def test_should_fill_brands(self):
        print "----> test_should_fill_brands"
        r = LinepathBP(FAKE_RESPONSES)
        r._fill_brands()
        self.assertEqual(r._brands, EXPECTED_BRANDS)

    def test_should_calc_total_sample(self):
        print "----> test_should_calc_total_sample"
        r = LinepathBP(FAKE_RESPONSES)
        r._fill_brands()
        r._calc_total_sample()
        self.assertEqual(r._total_sample, 200)

    def test_should_calc_total_sample_by_wave(self):
        print "----> test_should_calc_total_sample_by_wave"
        r = LinepathBP(FAKE_RESPONSES)
        r._fill_brands()
        r._calc_total_sample()
        r._calc_total_sample_by_wave()
        self.assertEqual(r._total_sample_by_wave, EXPECTED_COUNT_BY_WAVE)

    def test_should_calc_brand_percents(self):
        print "----> test_should_calc_brand_percents"
        r = LinepathBP(FAKE_RESPONSES)
        r._fill_brands()
        r._calc_total_sample()
        r._calc_total_sample_by_wave()
        percent = r._calc_brand_percents('wave 1', 20)
        self.assertEqual(percent, 10)
        percent = r._calc_brand_percents('wave 1', 100)
        self.assertEqual(percent, 50)

    def test_should_calc_percents_by_brand(self):
        print "----> test_should_calc_percents_by_brand"
        r = LinepathBP(FAKE_RESPONSES)
        r._fill_brands()
        r._calc_total_sample()
        r._calc_total_sample_by_wave()
        r._calc_percents_by_brand()
        self.assertEqual(r._responses, EXPECTED_OPTION_PERCENTAGES)

    def test_should_fill_lines(self):
        print "----> test_should_fill_lines"
        r = LinepathBP(FAKE_RESPONSES)
        r._fill_brands()
        r._calc_total_sample()
        r._calc_total_sample_by_wave()
        r._calc_percents_by_brand()
        r._fill_lines()
        self.assertEqual(r._lines, EXPECTED_LINES)

    def test_should_build_lines(self):
        print "----> test_should_build_lines"
        r = LinepathBP(FAKE_RESPONSES)
        r._fill_brands()
        r._calc_total_sample()
        r._calc_total_sample_by_wave()
        r._calc_percents_by_brand()
        r._fill_lines()
        r._build_lines()
        self.assertEqual(r._lines, EXPECTD_BUILDED_LINES)

    def test_should_buil_chart(self):
        print "----> test_should_buil_chart"
        r = LinepathBP(FAKE_RESPONSES)
        r._fill_brands()
        r._calc_total_sample()
        r._calc_total_sample_by_wave()
        r._calc_percents_by_brand()
        r._fill_lines()
        r._build_lines()
        r._buil_chart()
        self.assertEqual(r.data(), EXPECTED_DATA)

    def test_should_generate(self):
        print "----> test_should_generate"
        r = LinepathBP(FAKE_RESPONSES)
        r.generate()
        self.assertEqual(r.data(), EXPECTED_DATA)

import unittest
import copy
import json
from .brand_strength_monitor_reporter import BrandStrengthMonitorReporter
from .survey_db import SurveyDB
from .survey_db_test import SurveyModelFake
from .survey_db_test import EXPECTED_BRANDS
from .survey_db_test import EXPECTED_PARENT_BRANDS
from .survey_db_test import EXPECTED_PRODUCT_BRANDS
from .survey_db_test import EXPECTED_PARENT_PRODUCT_LIST


# python -m unittest discover backend.apps.popresearch.cmix.reporting.bsm brand_strength_monitor_reporter_test.py
class BrandStrengthMonitorReporterTestCase(unittest.TestCase):

    def test_should_setup_reporters(self):
        print "---> test_should_setup_reporters"
        r = BrandStrengthMonitorReporter(569)
        r._pull_survey_definition()
        r._setup_reporters()

    def test_should_build_filter_payload(self):
        print "---> test_should_build_filter_payload"
        r = BrandStrengthMonitorReporter(569)
        r._pull_survey_definition()
        r._setup_reporters()

    def test_should_setup_brand_colors(self):
        print "---> test_should_setup_brand_colors"
        r = BrandStrengthMonitorReporter(569)
        r._pull_survey_definition()
        r._setup_reporters()
        r._setup_brand_colors()
        expected_color_brands = {
            'Ambasa': '#6a3d9a',
            'Canada Dry': '#9464bf',
            'Coca Cola': '#1675b6',
            'Cream Soda': '#d8231e',
            'Crush': '#8d5649',
            'Dasani': '#7eb2d0',
            'Dr Pepper': '#bcbe00',
            'Fanta': '#cc5292',
            'Fresca': '#4e79a7',
            'Mirinda': '#f28e2c',
            'Mountain Dew': '#7f7f7f',
            'Pepsi': '#ff7f00',
            'Schweppes': '#e574c3',
            'Seven Up': '#23a121',
            'Sierra Mist': '#e15659',
            'Sprite': '#00bed0',
            'others': '#75b7b2'
        }
        self.assertEqual(r._color_brand.brands_color(), expected_color_brands)

    def test_should_build_filter_payload(self):
        print "---> test_should_build_filter_payload"
        r = BrandStrengthMonitorReporter(569)
        r._pull_survey_definition()
        r._setup_reporters()
        r._build_payload()

    def test_should_pull_filter_responses(self):
        print "---> test_should_pull_filter_responses"
        r = BrandStrengthMonitorReporter(569)
        r._pull_survey_definition()
        r._setup_reporters()
        r._build_payload()
        r._pull_responses()

    def test_should_transform_responses(self):
        print "---> test_should_transform_responses"
        r = BrandStrengthMonitorReporter(569)
        r._pull_survey_definition()
        r._setup_reporters()
        r._build_payload()
        r._pull_responses()
        r._transform_responses()

    def test_should_add_responses_to_reporters(self):
        print "---> test_should_pull_filter_responses"
        r = BrandStrengthMonitorReporter(569)
        r._pull_survey_definition()
        r._setup_reporters()
        r._build_payload()
        r._pull_responses()
        r._transform_responses()
        r._add_responses_to_reporters()

    def test_should_build_filters(self):
        print "---> test_should_build_filters"
        r = BrandStrengthMonitorReporter(569)
        r._pull_survey_definition()
        r._setup_reporters()
        r._build_payload()
        r._pull_responses()
        r._transform_responses()
        r._add_responses_to_reporters()
        r._build_filters()

    def test_should_generate_charts(self):
        print "---> test_should_generate_charts"
        r = BrandStrengthMonitorReporter(569)
        r._pull_survey_definition()
        r._setup_reporters()
        r._build_payload()
        r._pull_responses()
        r._transform_responses()
        r._add_responses_to_reporters()
        r._build_filters()
        r._generate_charts()

    def test_should_set_survey_data(self):
        print "---> test_should_set_survey_data"
        fake_model = SurveyModelFake()
        survey = SurveyDB(fake_model)
        survey.run()
        r = BrandStrengthMonitorReporter(569)
        r.set_survey_data(survey)
        self.assertEquals(r._survey_data._brands, EXPECTED_BRANDS)
        self.assertEquals(r._survey_data._parent_brands, EXPECTED_PARENT_BRANDS)
        self.assertEquals(r._survey_data._product_brands, EXPECTED_PRODUCT_BRANDS)
        self.assertEquals(r._survey_data._parent_product_list, EXPECTED_PARENT_PRODUCT_LIST)
        self.assertEquals(r._survey_data._brand_on_test, "KIND")
        self.assertEquals(r._survey_data._brand_on_test_products, ['KIND Healthy Grains Bar', 'KIND Healthy Grains Clusters'])

    def test_should_execute(self):
        print "---> test_should_execute"
        fake_model = SurveyModelFake()
        survey = SurveyDB(fake_model)
        survey.run()
        r = BrandStrengthMonitorReporter(569)
        r.set_survey_data(survey)
        response = r.execute()
        self.assertEqual(response, EXPECTED_DATA)

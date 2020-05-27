import unittest
import json
from .stacked_bar_2b import StackedBar2B


class StackedBarTestCase(unittest.TestCase):
    def test_should_init(self):
        print "----> test_should_init"
        r = StackedBar2B(PRE_RESPONSES, POST_RESPONSES, OPTIONS_TO_CONSIDER)
        self.assertIsNotNone(r._pre_responses)
        self.assertIsNotNone(r._post_responses)

    def test_should_add_brands(self):
        print("----> test_should_add_brands")
        r = StackedBar2B(PRE_RESPONSES, POST_RESPONSES, OPTIONS_TO_CONSIDER)
        r._add_brands()
        self.assertEqual(r._brands, ['colgate', 'crest', 'sensodyne'])

    def test_should_count_total_users(self):
        print("----> test_should_count_total_users")
        r = StackedBar2B(PRE_RESPONSES, POST_RESPONSES, OPTIONS_TO_CONSIDER)
        r._add_brands()
        r._count_total_users()
        self.assertEqual(r._total_pre_users, 200)
        self.assertEqual(r._total_post_users, 190)

    def test_should_count_responses(self):
        print "----> test_should_count_responses"
        r = StackedBar2B(PRE_RESPONSES, POST_RESPONSES, OPTIONS_TO_CONSIDER)
        r._add_brands()
        r._count_total_users()
        r._count_responses()
        self.assertEqual(r._pre_percents, {"colgate": 85.0, "crest": 95.0, "sensodyne": 95.0})
        self.assertEqual(r._post_percents, {"colgate": 94.7, "crest": 94.7, "sensodyne": 84.2})

    def test_should_calc_significantly(self):
        print "----> test_should_calc_significantly"
        r = StackedBar2B(PRE_RESPONSES, POST_RESPONSES, OPTIONS_TO_CONSIDER)
        r._add_brands()
        r._count_total_users()
        r._count_responses()
        r._calc_significantly()
        self.assertEqual(r._significantly, {"colgate": "post", "crest": "", "sensodyne": "pre"})

    def test_should_fill_data(self):
        print "----> test_should_fill_data"
        r = StackedBar2B(PRE_RESPONSES, POST_RESPONSES, OPTIONS_TO_CONSIDER)
        r._add_brands()
        r._count_total_users()
        r._count_responses()
        r._calc_significantly()
        r._fill_data()
        self.assertEqual(r.data(), EXPECTED_DATA)

    def test_should_fill_data(self):
        print "----> test_should_fill_data"
        r = StackedBar2B(PRE_RESPONSES, POST_RESPONSES, OPTIONS_TO_CONSIDER)
        r.generate()
        self.assertEqual(r.data(), EXPECTED_DATA)


EXPECTED_DATA = {
    "survey": "",
    "base_size": 200,
    "name": "",
    "data": {
        "values": [
            {
                "pre": 85,
                "post": 94.7,
                "sig": "post",
                "label": "colgate"
            },
            {
                "pre": 95,
                "post": 94.7,
                "sig": "",
                "label": "crest"
            },
            {
                "pre": 95,
                "post": 84.2,
                "sig": "pre",
                "label": "sensodyne"
            }
        ],
        "n": [
            200,
            190
        ]
    }
}
OPTIONS_TO_CONSIDER = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
]
PRE_RESPONSES = {
    "colgate": {
        "1": 20,
        "2": 20,
        "3": 40,
        "4": 10,
        "5": 30,
        "6": 30,
        "7": 20,
        "8": 30
    },
    "sensodyne": {
        "1": 40,
        "2": 10,
        "3": 10,
        "4": 40,
        "5": 40,
        "6": 20,
        "7": 30,
        "8": 10
    },
    "crest": {
        "1": 30,
        "2": 40,
        "3": 40,
        "4": 20,
        "5": 20,
        "6": 20,
        "7": 20,
        "8": 30
    }
}
POST_RESPONSES = {
    "colgate": {
        "1": 30,
        "2": 10,
        "3": 30,
        "4": 40,
        "5": 20,
        "6": 20,
        "7": 30,
        "8": 10
    },
    "sensodyne": {
        "1": 10,
        "2": 30,
        "3": 20,
        "4": 20,
        "5": 30,
        "6": 30,
        "7": 20,
        "8": 40
    },
    "crest": {
        "1": 40,
        "2": 40,
        "3": 10,
        "4": 20,
        "5": 30,
        "6": 20,
        "7": 20,
        "8": 20
    }
}

import unittest
import copy
import json
from .color_brand import ColorBrand


# python -m unittest discover backend.apps.popresearch.cmix.reporting.bsm color_brand_test.py
class ColorBrandTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "---> setUpClass"
        '''It is a single, only one should be availabe'''
        r = ColorBrand()

    def test_should_should_raise_exception(self):
        print "---> test_should_should_raise_exception"
        self.assertRaises(Exception, ColorBrand)

    def test_should_is_singleton(self):
        print "---> test_should_is_singleton"
        r = ColorBrand.getInstance()
        r.set_brands(['cocacola', 'pepsi'])
        self.assertEquals(r._brands, ['cocacola', 'pepsi'])

        r1 = ColorBrand.getInstance()
        self.assertEquals(r1._brands, ['cocacola', 'pepsi'])

        r2 = ColorBrand.getInstance()
        r2.set_brands(['incakola', 'sevenup'])

        self.assertEquals(r._brands, ['incakola', 'sevenup'])
        self.assertEquals(r1._brands, ['incakola', 'sevenup'])

    def test_should_init(self):
        print "---> test_should_init"
        brands = ['cocacola', 'pepsi', 'sevenup', 'incakola', 'guarana']
        r = ColorBrand.getInstance()
        r.set_brands(brands)
        self.assertIsNotNone(r._brands)

    def test_should_set_brand_colors(self):
        print "---> test_should_set_brand_colors"
        brands = ['cocacola', 'pepsi', 'sevenup', 'incakola', 'guarana']
        r = ColorBrand.getInstance()
        r.set_brands(brands)
        r._set_brand_colors()
        expected = {
            "guarana": "#9464bf",
            "incakola": "#d8231e",
            "cocacola": "#1675b6",
            "pepsi": "#ff7f00",
            "sevenup": "#23a121"
        }
        self.assertEquals(r._brands_color, expected)
        self.assertEquals(r.brands_color(), expected)

    def test_should_get_color(self):
        print "---> test_should_get_color"
        brands = ['cocacola', 'pepsi', 'sevenup', 'incakola', 'guarana']
        r = ColorBrand.getInstance()
        r.set_brands(brands)
        r._set_brand_colors()
        self.assertEquals(r._get_color('pepsi'), '#ff7f00')
        self.assertEquals(r._get_color('sevenup'), '#23a121')
        self.assertEquals(r._get_color('guarana'), '#9464bf')
        self.assertIsNotNone(r._get_color('something_weird'))

    def test_should_generate(self):
        print "---> test_should_generate"
        brands = ['cocacola', 'pepsi', 'sevenup', 'incakola', 'guarana']
        r = ColorBrand.getInstance()
        r.set_brands(brands)
        r.generate()
        self.assertEquals(r._get_color('pepsi'), '#ff7f00')
        self.assertEquals(r._get_color('sevenup'), '#23a121')
        self.assertEquals(r._get_color('guarana'), '#9464bf')
        self.assertIsNotNone(r._get_color('something_weird'))

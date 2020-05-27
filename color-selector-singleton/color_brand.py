import random
from .constants import BASIC_COLORS


class ColorBrand:
    '''
    Each brand should have a unique color and should keep
    the same color along other charts
    '''
    __instance = None

    @staticmethod
    def getInstance():
        if ColorBrand.__instance is None:
            ColorBrand()
        return ColorBrand.__instance

    def __init__(self):
        if ColorBrand.__instance is not None:
            raise Exception("This class is a singleton! use ColorBrand.getInstance()")
        else:
            ColorBrand.__instance = self

        self._brands = None
        self._colors = BASIC_COLORS
        self._brands_color = {}
        self._name = ""

    def set_brands(self, brands):
        self._brands = brands

    def brands_color(self):
        return self._brands_color

    def colors(self):
        return self._brands_color

    def brands(self):
        return self._brands_color

    def _set_brand_colors(self):
        for index, brand in enumerate(self._brands):
            self._brands_color.update({brand: self._colors[index]})

    def _get_color(self, brand):
        color = self._brands_color.get(brand)
        if color is None:
            i = random.randrange(len(self._brands) - 1, len(self._colors) - 1, 1)
            color = self._colors[i]
        return color

    def get_color(self, brand):
        return self._get_color(brand)

    def color_to_brand(self, brand):
        return self._get_color(brand)

    def generate(self):
        self._set_brand_colors()

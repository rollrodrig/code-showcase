import json
from .awareness_by_brand import AwarenessByBrand


class ConsiderationByBrand(AwarenessByBrand):
    def __init__(self, waves, brand_franchise):
        AwarenessByBrand.__init__(self, waves, brand_franchise)

    def _filter_option_ids(self):
        '''
        It is the percent of respondents who picked
        c) Would consider trying in the future
        g) One of a number of brands that I use
        h) My preferred brand in this category
        '''
        self._option_ids = self._option_ids[0]
        tmp_ids = []
        tmp_ids.append(self._option_ids[2])
        tmp_ids.append(self._option_ids[6])
        tmp_ids.append(self._option_ids[7])
        self._option_ids = tmp_ids

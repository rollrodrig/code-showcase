import json
from ..color_brand import ColorBrand


class LinepathBP:
    def __init__(self, responses):
        self._responses = responses
        self._data = {}
        self._survey = ""
        self._waves_index = [
            'wave 1',
            'wave 2',
            'wave 3',
            'wave 4',
            'wave 5',
            'wave 6',
            'wave 7',
            'wave 8',
            'wave 9',
            'wave 10',
            'wave 11',
            'wave 12',
        ]
        self._total_sample = 0
        self._total_sample_by_wave = {}
        self._brands = []
        self._labels = self._waves_index
        self._lines = {}
        self._color_brand = ColorBrand.getInstance()

    def survey_type(self, survey):
        self._survey = survey

    def _fill_labels(self):

        # TODO, it should populate labels
        pass

    def _fill_brands(self):
        '''
        All waves have the same brands
        so we need only list it once
        '''
        for wave, brands in self._responses.items():
            for brand in brands:
                self._brands.append(brand)
            break

    def _calc_total_sample(self):
        '''
        total sample for one wave
        '''
        wave1 = self._responses['wave 1']
        for brand in wave1:
            t = 0
            self._total_sample += wave1[brand]
        if self._total_sample <= 0:
            self._total_sample = 1

    def _calc_total_sample_by_wave(self):
        tmp = {}
        for wave_name, brands in self._responses.items():
            tmp_brand = {}
            count = 0
            for brand in brands:
                count += brands[brand]
            tmp.update({wave_name: count})
        self._total_sample_by_wave = tmp

    def _calc_brand_percents(self, wave, value):
        divisor = self._total_sample_by_wave[wave]
        if divisor <= 0:
            divisor = 1
        percent = value / (divisor * 1.0) * 100
        percent = round(percent, 1)
        return percent

    def _calc_percents_by_brand(self):
        tmp_responses = {}
        for wave, brands in self._responses.items():
            tmp_brand = {}
            for brand in brands:
                percent = self._calc_brand_percents(wave, brands[brand])
                tmp_brand.update({brand: percent})
            tmp_responses.update({wave: tmp_brand})
        self._responses = tmp_responses

    def _fill_lines(self):
        for b in self._brands:
            self._lines.update({b: []})

        for wave in self._waves_index:
            brands = self._responses[wave]
            for b in brands:
                self._lines[b].append(brands[b])

    def _build_lines(self):
        tmp = []
        t = {}
        for brand in self._lines:
            t = {
                "legend": brand,
                "color": self._color_brand.get_color(brand),
                "points": self._lines[brand]
            }
            tmp.append(t)
        self._lines = tmp

    def _buil_chart(self):
        self._data = {
            'data': {
                'labels': self._labels,
                'lines': self._lines
            },
            'base_size_by_wave': self._total_sample_by_wave,
            'base_size': self._total_sample,
            'survey': self._survey
        }

    def data(self):
        return self._data

    def generate(self):
        self._fill_brands()
        self._calc_total_sample()
        self._calc_total_sample_by_wave()
        self._calc_percents_by_brand()
        self._fill_lines()
        self._build_lines()
        self._buil_chart()
        return self._data

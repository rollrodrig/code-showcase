import json
from ..color_brand import ColorBrand


class SimpleLinepath:
    def __init__(self, pre_responses, post_responses, option_ids):
        self._pre_responses = pre_responses
        self._post_responses = post_responses
        self._option_ids = option_ids
        self._labels = [
            'pre',
            'post',
        ]
        self._lines = []
        self._total_pre_sample = 0
        self._total_post_sample = 0
        self._survey = ""
        self._data = {}
        self._brands = []
        self._color_brand = ColorBrand.getInstance()

    def survey_type(self, survey):
        self._survey = survey

    def _fill_brands(self):
        for brand, options in self._pre_responses.items():
                self._brands.append(brand)

    def _calc_total_samples(self):
        for brand, options in self._pre_responses.items():
            for option in options:
                self._total_pre_sample += options[option]
            break

        for brand, options in self._post_responses.items():
            for option in options:
                self._total_post_sample += options[option]
            break

    def _calc_option_percents(self, response, total):
        if total <= 0:
            total = 1
        tmp = {}
        for brand, options in response.items():
            count = 0
            for opt in self._option_ids:
                count += options[str(opt)]
                percent = count * 100 / (total * 1.0)
                percent = round(percent, 1)
            tmp.update({brand: percent})
        return tmp

    def _calc_percents_by_brand(self):
        data = self._calc_option_percents(self._pre_responses, self._total_pre_sample)
        self._pre_responses = data
        data = self._calc_option_percents(self._post_responses, self._total_post_sample)
        self._post_responses = data

    def _fill_lines(self):
        lines = []
        for brand in self._pre_responses:
            tmp = {
                'legend': brand,
                'color': self._color_brand.get_color(brand),
                'points': [self._pre_responses[brand], self._post_responses[brand]],
            }
            lines.append(tmp)
        self._lines = lines

    def _buil_chart(self):
        self._data = {
            'data': {
                'labels': self._labels,
                'lines': self._lines
            },
            'base_size': self._total_pre_sample,
            'pre_size': self._total_pre_sample,
            'post_size': self._total_post_sample,
            'survey': self._survey
        }

    def data(self):
        return self._data

    def generate(self):
        self._fill_brands()
        self._calc_total_samples()
        self._calc_percents_by_brand()
        self._fill_lines()
        self._buil_chart()
        return self._data


linepath = {
    'labels': [
        'pre',
        'post',
    ],
    'lines': [
        {
            'legend': 'Toms of Maine',
            'color': '#1675b6',
            'points': [32, 35],
        },
        {
            'legend': 'Sensodyne',
            'color': '#ff7f00',
            'points': [34, 39],
        },
        {
            'legend': 'Colgate',
            'color': '#23a121',
            'points': [40, 55],
        },
    ],
}

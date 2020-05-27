import json

'''
Awareness for each brand comes from question 12 (BrandFranchise).
It reflects the percent of respondents who answer anything but
"Never heard of this brand before today"

Consideration also comes from question 12 (BrandFranchise).
It reflects the percent of respondents who answered
"Would consider trying in the future"
"One of a number of brands that I use" or
"My preferred brand in this category.

Usage also comes from question 12 (BrandFranchise).
It is the percent of respondents who answered either
"One of a number of brands that I use" or "My preferred brand in this category".

Finally, prefer comes from the BRAND PREFERENCE EXERCISE
and is the percent of respondents who selected that brand
in the prize drawing (combining across products if there are
multiple products for the brand in the competitive set).
Note this requires some connection be made between the brands
in the Brand Preference Exercise and those in the Brand Franchise
question at the time the user sets-up the project.

The percents in the table are each metric
from the funnel as a percent of the metric
above it in the funnel. So for Toms of Maine:
Consider As % of Aware = 28 / 73 = 38%
Use As % of Consider = 5 / 28 = 18%
Prefer As % of Usage = 5 / 5 = 100%

The data should be displayed for total sample by default,
but there should be a dropdown box that will allow data
to be displayed for the usage level subsamples
(heavy, medium and light users as defined
in question 10 (CategoryUsage).
'''


class AwarenessConsiderationChart:
    def __init__(self, total_sample, brand_franchise_responses, option_names, option_ids, brand_preference):
        self._total_sample = 0
        self._responses = brand_franchise_responses
        self._responses_count = {}
        self._option_names = option_names
        '''only one is needed'''
        self._option_ids = option_ids[0]
        self._brand_preference = brand_preference
        self._x = []
        self._y = [
            'Aware',
            'Consider',
            'Use',
            'Prefer',
        ]
        self._s = [
            {
                "l": "Consider As % of aware",
                "v": [],
            },
            {
                "l": "Use As % of consider",
                "v": []
            },
            {
                "l": "Prefer As % of Usage",
                "v": []
            }
        ]
        self._values = []
        self._values_aware = []
        self._values_consider = []
        self._values_use = []
        self._values_prefer = []
        self._survey = ""
        self._data = {
            'base_size': 0,
            'survey': '',
            'name': '',
            'data': {
                'x': [],
                'y': [],
                'values': [],
                's': []
            }
        }

    def survey_type(self, survey):
        self._survey = survey

    def _calc_response_count(self):
        '''
        Count the number of users who responded
        that option on each brand
        {'cocacola': {a: 25, b: 30}, ...}
        Example: 25 users marked option a on cocacola
        '''
        tmp = {}
        for brand, options in self._responses.items():
            tmp.update({brand: {}})
            for opt, users in options.items():
                count = {opt: len(users)}
                tmp[brand].update(count)
        self._responses_count = tmp
        return self._responses_count

    def _count_total_sample(self):
        total = 0
        for brand, options in self._responses_count.items():
            for option in options:
                total += options[option]
            '''
            All brands have the same number of users
            we only need to count one time
            '''
            break
        self._total_sample = total

    def data(self):
        return self._data

    def _to_percent(self, value):
        percent = (value * 100) / (self._total_sample * 1.0)
        percent = round(percent, 1)
        return percent

    def _create_x(self):
        for r in self._responses:
            self._x.append(r)

    def _create_values_aware(self):
        '''
        It reflects the percent of respondents who answer anything
        but "a) Never heard of this brand before today"
        '''
        values = []
        option_a_id = self._option_ids[0]
        '''
        On each brand take the option 'a' and substract from total
        '''
        for brand in self._x:
            responses = self._responses_count[brand]
            t = responses[str(option_a_id)]
            t = self._total_sample - t
            values.append(self._to_percent(t))
        self._values_aware = values
        return self._values_aware

    def _create_values_consider(self):
        '''
        It reflects the percent of respondents who answered
        c) Would consider trying in the future
        g) One of a number of brands that I use
        h) My preferred brand in this category
        '''
        values = []
        opt_c = self._option_ids[2]
        opt_g = self._option_ids[6]
        opt_h = self._option_ids[7]
        '''
        on each brand add the total users who picked option C, G or H
        '''
        for brand in self._x:
            responses = self._responses_count[brand]
            count = 0
            count += responses[str(opt_c)]
            count += responses[str(opt_g)]
            count += responses[str(opt_h)]
            values.append(self._to_percent(count))
        self._values_consider = values
        return self._values_consider

    def _create_values_use(self):
        '''
        It is the percent of respondents who answered
        either G or H
        g) One of a number of brands that I use
        h) My preferred brand in this category.
        '''
        values = []
        opt_g = self._option_ids[6]
        opt_h = self._option_ids[7]
        '''
        on each brand add the total users who picked option G or H
        '''
        for brand in self._x:
            responses = self._responses_count[brand]
            count = 0
            count += responses[str(opt_g)]
            count += responses[str(opt_h)]
            values.append(self._to_percent(count))
        self._values_use = values
        return self._values_use

    def _count_brand_pref_percents(self):
        '''Percent of responses on each brand'''
        tmp = {}
        for brand, users in self._brand_preference.items():
            percent = self._to_percent(len(users))
            tmp.update({brand: percent})
        self._brand_preference = tmp

    def _create_values_prefer(self):
        self._count_brand_pref_percents()
        '''
        Finally, prefer comes from the BRAND PREFERENCE EXERCISE
        and is the percent of respondents who selected that brand
        in the prize drawing
        '''
        values = []
        for brand in self._x:
            '''When a brand have products it is not listed on brand_preference'''
            v = self._brand_preference.get(brand)
            if v is not None:
                values.append(v)
            else:
                ''' Store values 1 because it will be used later as divisor and also to keep the same array length'''
                values.append(1)
        self._values_prefer = values
        return self._values_prefer

    def _create_values(self):
        self._create_values_aware()
        self._create_values_consider()
        self._create_values_use()
        self._create_values_prefer()
        self._values.append(self._values_aware)
        self._values.append(self._values_consider)
        self._values.append(self._values_use)
        self._values.append(self._values_prefer)
        return self._values

    def _create_percents(self):
        consider_as_aware = []
        use_as_consider = []
        prefer_as_usage = []
        '''For each brand calc percents according to the formula'''
        for index, b in enumerate(self._x):
            ca = self._calc_consider_as_aware(index)
            consider_as_aware.append(ca)
            uc = self._calc_use_as_consider(index)
            use_as_consider.append(uc)
            pu = self._calc_pref_use(index)
            prefer_as_usage.append(pu)
        self._s[0]['v'] = consider_as_aware
        self._s[1]['v'] = use_as_consider
        self._s[2]['v'] = prefer_as_usage

    '''
    The following three methods looks similar but
    are different and cant be merged
    '''
    def _calc_consider_as_aware(self, index):
        '''Consider As / of Aware -> example: 28 / 73 = 38%'''
        divisor = self._values_aware[index]
        if divisor <= 0:
            divisor = 1
        c = self._values_consider[index] / (divisor * 1.0)
        c = int(round(c * 100, 0))
        return c

    def _calc_use_as_consider(self, index):
        '''Use As / of Consider -> example: 5 -> example:/ 28 = 18%'''
        divisor = self._values_consider[index]
        if divisor <= 0:
            divisor = 1
        c = self._values_use[index] / (divisor * 1.0)
        c = int(round(c * 100, 0))
        return c

    def _calc_pref_use(self, index):
        '''Prefer As / of Usage -> example: 5 / 5 = 100%'''
        divisor = self._values_use[index]
        if divisor <= 0:
            divisor = 1
        c = self._values_prefer[index] / (divisor * 1.0)
        c = int(round(c * 100, 0))
        return c

    def _fill_data(self):
        self._data['data']['x'] = self._x
        self._data['data']['y'] = self._y
        self._data['data']['values'] = self._values
        self._data['data']['s'] = self._s
        self._data['survey'] = self._survey
        self._data['base_size'] = self._total_sample

    def generate(self):
        self._calc_response_count()
        self._count_total_sample()
        self._create_x()
        self._create_values()
        self._create_percents()
        self._fill_data()
        return self._data


DATA_AwarenessConsideration = {
    'x': [
        'Toms of Maine',
        'Sensodyn',
        'Colgate',
        'Arm & Hammer',
        'Aquafresh',
        'Aim',
        'Crest',
    ],
    'y': [
        'Aware',
        'Consider',
        'Use',
        'Prefer',
    ],
    "values": [
        [73, 92, 98, 88, 90, 90, 99],
        [28, 46, 50, 21, 18, 16, 68],
        [5, 20, 28, 5, 5, 3, 34],
        [5, 26, 25, 4, 3, 1, 36],
    ],
    "s": [
        {
            "l": "Consider As % of aware",
            "v": [38, 50, 51, 24, 20, 20, 69],
        },
        {
            "l": "Use As % of consider",
            "v": [18, 43, 56, 24, 28, 19, 50]
        },
        {
            "l": "Prefer As % of Usage",
            "v": [100, 130, 89, 80, 60, 33, 106]
        }
    ]
}

import json
import math


class StackedBar2B:
    def __init__(self, pre_responses, post_responses, option_ids):
        self._pre_responses = pre_responses
        self._post_responses = post_responses
        self._option_ids = option_ids
        self._total_users = 0
        self._total_pre_users = 0
        self._total_post_users = 0
        self._brands = []
        self._pre_percents = {}
        self._post_percents = {}
        self._significantly = {}
        self._survey = ""
        self._data = {
            'base_size': -1,
            'survey': '',
            'name': '',
            'data': {
                'n': [],
                'values': []
            }
        }

    def survey_type(self, survey):
        self._survey = survey

    def _add_brands(self):
        for brand in self._pre_responses:
            self._brands.append(brand)
        return self._brands

    def _count_total_users(self):
        for brand, options in self._pre_responses.items():
            for option in options:
                self._total_pre_users += options[option]
            break
        if self._total_pre_users <= 0:
            self._total_pre_users = 1

        for brand, options in self._post_responses.items():
            for option in options:
                self._total_post_users += options[option]
            break
        if self._total_post_users <= 0:
            self._total_post_users = 1

    def _count_responses(self):
        '''
        Awareness is drawn from question BrandFranchise.
        It is the percent of respondents who picked anything except
        "Never heard of this brand before today" for that particular brand
        '''
        for brand, options in self._pre_responses.items():
            pre_considered_users = 0
            post_considered_users = 0
            for opt_id in self._option_ids:
                pre_users = self._pre_responses[brand][str(opt_id)]
                pre_considered_users += pre_users
                post_users = self._post_responses[brand][str(opt_id)]
                post_considered_users += post_users

            pre = pre_considered_users / (self._total_pre_users * 1.0) * 100.0
            pre = round(pre, 1)
            self._pre_percents.update({brand: pre})

            post = post_considered_users / (self._total_post_users * 1.0) * 100.0
            post = round(post, 1)
            self._post_percents.update({brand: post})

    def _calc_significantly(self):
        '''
        For the Pre/Post deliverable, awareness is shown
        with a clustered bar chart where the percent aware
        for the before and after waves are clustered together
        for each brand.  For this deliverable, stat testing
        is conducted between the pre and post awareness levels
        for each brand.

        Use the following formula to conduct this stat test:
        t = (Pre - Post)/sqrt(P*Q*(1/N1 + 1/N2)), where:
        Pre = Awareness in pre wave
        Post = Awareness in post wave
        N1 = Base size of pre wave
        N2=Base size of post wave
        P=(N1*Pre + N2*Post)/(N1+N2)
        Q=100 - P

        For significance at the 90% Confidence Level:
        If t-value <= -1.645 then post significantly above pre;
        If t-value > -1.645 and t-value <1.645 then pre and post are not significantly different;
        If t-value >= 1.645 then pre significantly above post.
        '''
        significantly = 1.645
        N1 = self._total_pre_users * 1.0
        N2 = self._total_post_users * 1.0
        for brand in self._pre_percents:
            pre = self._pre_percents[brand]
            post = self._post_percents[brand]
            npre = N1 * pre
            npost = N2 * post
            n1_n2 = N1 + N2
            P = (npre + npost) / n1_n2
            Q = 100 - P
            d = (1 / N1) + (1 / N2)
            sqrt = math.sqrt(P * Q * d)
            if sqrt == 0:
                sqrt = 1
            T = (pre - post) / sqrt
            T = round(T, 3)
            if T <= -significantly:
                self._significantly.update({brand: 'post'})
            elif T > significantly:
                self._significantly.update({brand: 'pre'})
            else:
                self._significantly.update({brand: ''})

    def _fill_data(self):
        data = []
        for brand in self._pre_percents:
            tmp = {
                'label': brand,
                'pre': self._pre_percents[brand],
                'post': self._post_percents[brand],
                'sig': self._significantly[brand]
            }
            data.append(tmp)
        self._data['data']['values'] = data
        self._data['data']['n'] = [self._total_pre_users, self._total_post_users]

        # TODO, base_size should be calculated from another source
        self._data['base_size'] = self._total_pre_users
        self._data['survey'] = self._survey

    def data(self):
        return self._data

    def generate(self):
        self._add_brands()
        self._count_total_users()
        self._count_responses()
        self._calc_significantly()
        self._fill_data()
        return self._data


DATA__StackedBar2b = {
    'base_size': -1,
    'name': '',
    'data': {
        'n': [450, 350],
        'values': [
            {'label': 'Toms of Maine', 'pre': 65, 'post': 75, 'sig': 'pre'},
            {'label': 'Sensodyne', 'pre': 72, 'post': 92, 'sig': 'pre'},
            {'label': 'Colgate', 'pre': 68, 'post': 98, 'sig': ''},
            {'label': 'Arm & Hammer', 'pre': 78, 'post': 88, 'sig': ''},
            {'label': 'Aquafresh', 'pre': 80, 'post': 90, 'sig': ''},
            {'label': 'Aim', 'pre': 60, 'post': 80, 'sig': 'post'},
            {'label': 'Crest', 'pre': 65, 'post': 99, 'sig': 'post'},
        ]
    }
}

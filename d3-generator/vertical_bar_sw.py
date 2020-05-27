import json
from collections import OrderedDict
'''
Unaware             0) Never heard of this brand before today
Indifferent         1) A brand I had heard of but had no opinion about
Attracted           2) Would consider trying in the future
Hostile             3) No experience with the brand, but would never use
Lapsed              4) Used to use in the past
Rejecters           5) Tried in the past and will never use again
Repertoire Users    6) One of a number of brands that I use
Loyalists           7) My preferred brand in this category

For Trial as a % of Aware
    Trial
        Lapsed              Used to use in the past
        Rejecters           Tried in the past and will never use again
        Repertoire Users    One of a number of brands that I use
        Loyalists           My preferred brand in this category

    Aware
        Loyalists           My preferred brand in this category
        Repertoire Users    One of a number of brands that I use
        Lapsed              Used to use in the past
        Attracted           Would consider trying in the future
        Indifferent         A brand I had heard of but had no opinion about
        Hostile             No experience with the brand, but would never use
        Rejecters           Tried in the past and will never use again

Current users as a % of trialists
    Current
        Loyalists           My preferred brand in this category
        Repertoire Users    One of a number of brands that I use
    Trialists
        Lapsed              Used to use in the past
        Rejecters           Tried in the past and will never use again
        Repertoire Users    One of a number of brands that I use
        Loyalists           My preferred brand in this category

Attracted as a % of Aware Non-Trialists
    Attracted
        Attracted           Would consider trying in the future
    Aware Non-Trialists
        Attracted           Would consider trying in the future
        Indifferent         A brand I had heard of but had no opinion about
        Hostile             No experience with the brand, but would never use

of Loyalists as a % of Current Users
    Loyalists
        Loyalists           My preferred brand in this category

    Current Users
        Loyalists           My preferred brand in this category
        Repertoire Users    One of a number of brands that I use
'''


class VerticalBarSW:
    def __init__(self, user_responses, option_names, option_ids):
        self._data = {
            'base_size': 0,
            'survey': '',
            'data': None,
            'name': ""
        }
        self._user_responses = user_responses
        self._option_names = option_names
        self._option_ids = option_ids
        self._users_by_brand = {}
        self._data_chart = {}
        self._survey = ""
        self._total_sample = 0
        '''
        It has the option id for each competitive chart
        {string: [int[], int[]], ...}
        '''
        self._chart_name_ids = {
            'trial_aware': [],
            'current_trialist': [],
            'attracted_nontrialists': [],
            'loyalists_current': []
        }

        self._chart_name_index = [
            'trial_aware',
            'current_trialist',
            'attracted_nontrialists',
            'loyalists_current'
        ]

        self._data_titles = None

    def survey_type(self, survey):
        self._survey = survey

    def total_sample(self):
        return self._total_sample

    def _count_total_sample(self):
        count = 0
        for brand, options in self._user_responses.items():
            for option, users in options.items():
                count += len(users)
            break
        self._total_sample = count
        self._data['base_size'] = count
        return self._total_sample

    def _fill_data_titles(self):
        self._data_titles = {
            'trial_aware': {
                'title': 'Trial As % of Aware ',
                'color': '#1675b6',
                'id': '10001'
            },
            'current_trialist': {
                'title': 'Current User As % of Trialist',
                'color': '#f28e2c',
                'id': '10002'
            },
            'attracted_nontrialists': {
                'title': 'Attracted As % Aware Non-Trialist',
                'color': '#e15659',
                'id': '10003'
            },
            'loyalists_current': {
                'title': 'Loyalists As % of Current Users',
                'color': '#84c85a',
                'id': '10004'
            }
        }

    def _def_trial_aware_ids(self):
        '''
        For Trial as a % of Aware, trial is the percent of respondents
        who are classified as loyal, repertoire, lapsed or rejecter
        while aware is percent of respondents classified as anything
        except unaware

        Trial
            4) Lapsed, 5) Rejecters, 6) Repertoire, 7) Loyalists
        Aware
            1) Loyalists, 2) Repertoire User, 3) Lapsed,
            4) Attracted, 5) Indifferent, 6) Hostile, 7) Rejecters
        '''
        trial_question_ids = [4, 5, 6, 7]
        self._chart_name_ids['trial_aware'].append(trial_question_ids)
        aware_question_ids = [1, 2, 3, 4, 5, 6, 7]
        self._chart_name_ids['trial_aware'].append(aware_question_ids)

    def _def_current_trialist(self):
        '''
        For the chart of current users as a % of trialists,
        current users is the percent of respondents
        classified as loyal or repertoire.

        Current
            6) Repertoire User, 7) Loyalists
        Trialists
            4) Lapsed, 5) Rejecters, 6) Repertoire, 7) Loyalists
        '''
        current_question_ids = [2, 7]
        self._chart_name_ids['current_trialist'].append(current_question_ids)
        aware_question_ids = [4, 5, 6, 7]
        self._chart_name_ids['current_trialist'].append(aware_question_ids)

    def _def_attracted_nontrialists(self):
        '''
        For the chart of Attracted as a % of Aware Non-Trialists,
        attracted is the percent of respondents classified
        as Attracted and Aware Non Trialists are the percent
        classified as Attracted, Indifferent or Hostile

        Attracted
            2) Attracted
        Aware Non-Trialists
            1) Indifferent, 2) Attracted, 3) Hostile
        '''
        attracted_question_ids = [2]
        self._chart_name_ids['attracted_nontrialists'].append(attracted_question_ids)
        aware_question_ids = [1, 2, 3]
        self._chart_name_ids['attracted_nontrialists'].append(aware_question_ids)

    def _def_loyalists_current(self):
        '''
        Finally, for the chart of Loyalists as a % of Current Users,
        Loyalists is the percent of respondents classified
        as Loyal and current users are the percent of respondents
        classified as Loyal or Repertoire

        Loyalists
            7) Loyalists
        Current Users
            6) Repertoire User, 7) Loyalists
        '''
        loyalist_question_ids = [7]
        self._chart_name_ids['loyalists_current'].append(loyalist_question_ids)
        current_question_ids = [6, 7]
        self._chart_name_ids['loyalists_current'].append(current_question_ids)

    def _calc_competitive_charts(self):
        data_chart = {}
        for brand, users in self._users_by_brand.items():
            data_chart.update({brand: {}})
            chart_ordered = OrderedDict()
            for chart in self._chart_name_index:
                competitive_ids = self._chart_name_ids[chart]
                data = self._count_users(competitive_ids[0], competitive_ids[1], users)
                competitive_chart = {chart: data}
                chart_ordered.update(competitive_chart)

            data_chart[brand] = chart_ordered

        self._data_chart = data_chart

    def _count_users(self, a_question_indexs, b_question_indexs, total_users_by_index):
        '''
        @a_question_indexs: int[]   list of question index
        @b_question_indexs: int[]   list of question index
        @total_users: int[]   Each element is the number of users
        @return: {a: int, b: int, p: double}
        '''
        total_a_users = 0
        total_b_users = 0
        '''
        Each element in 'a_question_indexs' has number,
        that number represent an index in 'total_users_by_index'
        '''
        for id in a_question_indexs:
            '''pick some total users and add them up'''
            total_a_users += total_users_by_index[id]

        for id in b_question_indexs:
            '''pick some total users and add them up'''
            total_b_users += total_users_by_index[id]

        if total_b_users <= 0:
            total_b_users = 1

        '''Decimal division fix'''
        total_b_users = total_b_users * 1.0

        '''
        Percent of total_a_users respect of total_b_users
        '''
        percent = total_a_users * 100 / total_b_users
        percent = round(percent, 1)
        data = {
            'a': total_a_users,
            'b': total_b_users,
            'p': percent
        }
        return data

    def _fill_data(self):
        '''
        Arrange data in the format that frontend expects
        '''
        data = []
        for brand, charts in self._data_chart.items():
            charts_in_brand = []
            for chart_name, calculus in charts.items():
                each_chart = {
                    'title': self._data_titles[chart_name]['title'],
                    'color': self._data_titles[chart_name]['color'],
                    'data': [
                        {
                            'id': self._data_titles[chart_name]['id'],
                            'value': calculus['p']
                        }
                    ]
                }
                charts_in_brand.append(each_chart)
            each_brand = {
                'brand': brand,
                'data': charts_in_brand
            }
            data.append(each_brand)
        self._data['data'] = data
        self._data['survey'] = self._survey
        return self._data

    def _count_users_by_brand(self):
        '''
        Count the total users on each option on each brand
        @return {string: int[], ...}
        '''
        for brand, options in self._user_responses.items():
            t = []
            for opt_id in self._option_ids:
                users = self._user_responses[brand][str(opt_id)]
                t.append(len(users))
            self._users_by_brand.update({brand: t})
        return self._users_by_brand

    def data(self):
        return self._data

    def generate(self):
        self._count_total_sample()
        self._fill_data_titles()
        self._count_users_by_brand()
        self._def_trial_aware_ids()
        self._def_current_trialist()
        self._def_attracted_nontrialists()
        self._def_loyalists_current()
        self._calc_competitive_charts()
        self._fill_data()
        return self._data

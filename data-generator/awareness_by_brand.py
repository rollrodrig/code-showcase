import json
import copy
from ...charts.simple_linepath import SimpleLinepath
from ...charts.grid2d_small2 import Grid2DSmall2


class AwarenessByBrand:
    def __init__(self, waves, brand_franchise):
        self._data = {}
        self._waves = waves
        self._waves_respones = self._waves.users_responses()
        self._wave_pre = {}
        self._wave_post = {}

        self._brand_franchise = brand_franchise
        self._brand_franchise_users = self._brand_franchise.users_responses()
        self._brand_franchise_users_heavy = self._brand_franchise.users_responses_heavy()
        self._brand_franchise_users_medium = self._brand_franchise.users_responses_medium()
        self._brand_franchise_users_light = self._brand_franchise.users_responses_light()

        self._brand_franchise_pre_users = {}
        self._brand_franchise_post_users = {}
        self._brand_franchise_pre_users_heavy = {}
        self._brand_franchise_post_users_heavy = {}
        self._brand_franchise_pre_users_medium = {}
        self._brand_franchise_post_users_medium = {}
        self._brand_franchise_pre_users_light = {}
        self._brand_franchise_post_users_light = {}

        self._option_ids = self._brand_franchise._options_ids

    def _filter_option_ids(self):
        '''remove (a) Never heard of this brand before today '''
        self._option_ids = self._option_ids[0]
        self._option_ids = copy.deepcopy(self._option_ids)
        del self._option_ids[0]

    def _invert_wave_pre(self):
        wave = self._waves_respones['wave 1']
        for w in wave:
            self._wave_pre.update({w: 1})

    def _invert_wave_post(self):
        wave = self._waves_respones['wave 2']
        for w in wave:
            self._wave_post.update({w: 1})

    def _invert_waves(self):
        self._invert_wave_pre()
        self._invert_wave_post()

    def _filter_users_in(self, franchise_users):
        '''
        Build two list and keep only pre or post users respectively
        '''
        data = {
            "pre": {},
            "post": {}
        }
        tmp_pre_options = {}
        tmp_post_options = {}

        for brand, options in franchise_users.items():
            tmp_pre_options.update({brand: {}})
            tmp_post_options.update({brand: {}})

            for option, users in options.items():
                tmp_pre_users = []
                tmp_post_users = []

                for user in users:
                    if self._wave_pre.get(user) == 1:
                        tmp_pre_users.append(user)

                    if self._wave_post.get(user) == 1:
                        tmp_post_users.append(user)

                tmp_pre_options[brand].update({option: tmp_pre_users})
                tmp_post_options[brand].update({option: tmp_post_users})

        data['pre'] = tmp_pre_options
        data['post'] = tmp_post_options
        return data

    def _filter_pre_post_users(self):
        data = self._filter_users_in(self._brand_franchise_users)
        self._brand_franchise_pre_users = data['pre']
        self._brand_franchise_post_users = data['post']

        data = self._filter_users_in(self._brand_franchise_users_heavy)
        self._brand_franchise_pre_users_heavy = data['pre']
        self._brand_franchise_post_users_heavy = data['post']

        data = self._filter_users_in(self._brand_franchise_users_medium)
        self._brand_franchise_pre_users_medium = data['pre']
        self._brand_franchise_post_users_medium = data['post']

        data = self._filter_users_in(self._brand_franchise_users_light)
        self._brand_franchise_pre_users_light = data['pre']
        self._brand_franchise_post_users_light = data['post']

    def _count_pre_post_users(self):
        '''only total number users are needed'''
        for brand, options in self._brand_franchise_users.items():
            for option in options:
                self._brand_franchise_pre_users[brand][option] = len(self._brand_franchise_pre_users[brand][option])
                self._brand_franchise_post_users[brand][option] = len(self._brand_franchise_post_users[brand][option])

                self._brand_franchise_pre_users_heavy[brand][option] = len(self._brand_franchise_pre_users_heavy[brand][option])
                self._brand_franchise_post_users_heavy[brand][option] = len(self._brand_franchise_post_users_heavy[brand][option])

                self._brand_franchise_pre_users_medium[brand][option] = len(self._brand_franchise_pre_users_medium[brand][option])
                self._brand_franchise_post_users_medium[brand][option] = len(self._brand_franchise_post_users_medium[brand][option])

                self._brand_franchise_pre_users_light[brand][option] = len(self._brand_franchise_pre_users_light[brand][option])
                self._brand_franchise_post_users_light[brand][option] = len(self._brand_franchise_post_users_light[brand][option])

    def _build_chart(self):
        linepath_total = SimpleLinepath(self._brand_franchise_pre_users, self._brand_franchise_post_users, self._option_ids)
        linepath_total.survey_type("prepost")
        linepath_total.generate()
        linepath_total_data = linepath_total.data()
        grid_total = Grid2DSmall2(self._brand_franchise_pre_users, self._brand_franchise_post_users, self._option_ids)
        grid_total.survey_type("prepost")
        grid_total.generate()
        grid_total_data = grid_total.data()

        linepath_heavy = SimpleLinepath(self._brand_franchise_pre_users_heavy, self._brand_franchise_post_users_heavy, self._option_ids)
        linepath_heavy.survey_type("prepost")
        linepath_heavy.generate()
        linepath_heavy_data = linepath_heavy.data()
        grid_heavy = Grid2DSmall2(self._brand_franchise_pre_users_heavy, self._brand_franchise_post_users_heavy, self._option_ids)
        grid_heavy.survey_type("prepost")
        grid_heavy.generate()
        grid_heavy_data = grid_heavy.data()

        linepath_medium = SimpleLinepath(self._brand_franchise_pre_users_medium, self._brand_franchise_post_users_medium, self._option_ids)
        linepath_medium.survey_type("prepost")
        linepath_medium.generate()
        linepath_medium_data = linepath_medium.data()
        grid_medium = Grid2DSmall2(self._brand_franchise_pre_users_medium, self._brand_franchise_post_users_medium, self._option_ids)
        grid_medium.survey_type("prepost")
        grid_medium.generate()
        grid_medium_data = grid_medium.data()

        linepath_light = SimpleLinepath(self._brand_franchise_pre_users_light, self._brand_franchise_post_users_light, self._option_ids)
        linepath_light.survey_type("prepost")
        linepath_light.generate()
        linepath_light_data = linepath_light.data()
        grid_light = Grid2DSmall2(self._brand_franchise_pre_users_light, self._brand_franchise_post_users_light, self._option_ids)
        grid_light.survey_type("prepost")
        grid_light.generate()
        grid_light_data = grid_light.data()

        self._data = {
            'Total': {
                "base_size": linepath_total_data['base_size'],
                "survey": "prepost",
                "name": "",
                "data": {
                    'linepath': linepath_total_data,
                    'grid': grid_total_data,
                },
            },
            'Heavy': {
                "base_size": linepath_heavy_data['base_size'],
                "survey": "prepost",
                "name": "",
                "data": {
                    'linepath': linepath_heavy_data,
                    'grid': grid_heavy_data,
                },
            },
            'Medium': {
                "base_size": linepath_medium_data['base_size'],
                "survey": "prepost",
                "name": "",
                "data": {
                    'linepath': linepath_medium_data,
                    'grid': grid_medium_data,
                },
            },
            'Light': {
                "base_size": linepath_light_data['base_size'],
                "survey": "prepost",
                "name": "",
                "data": {
                    'linepath': linepath_light_data,
                    'grid': grid_light_data,
                },
            },
        }

    def data(self):
        return self._data

    def generate(self):
        self._filter_option_ids()
        self._invert_waves()
        self._filter_pre_post_users()
        self._count_pre_post_users()
        self._build_chart()
        return self._data


FAKE = {
    "base_size": "114",
    "survey": "prepost",
    "name": "",
    "data": {
        'linepath': {
            'title': '',
            'width': 500,
            'height': 300,
            'data': {
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
            },
        },
        'grid': {
            'title': 'Title example',
            'data': {
                'x': [
                    'Before',
                    'After',
                ],
                'y': [
                    'N=',
                    'Crest 3D white Arctic Fresh',
                    'Crest 3D white Brillance',
                    'Crest 3D white radiant mint',
                    'etc',
                ],
                'values': [
                    [400, 400],
                    [5, 4],
                    [2, 3],
                    [4, 6],
                    [4, 6],
                ],
            },
        },
    }
}

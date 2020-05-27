import json
from .fake_data.reporter_fake import get_survey_definition, get_bsm_response_map
from .utils import transform_responses
from .reporters.age_filter import AgeFilterReporter
from .reporters.demo_children import DemoChildrenReporter
from .reporters.demo_hispanic import DemoHispanicReporter
from .reporters.demo_race import DemoRaceReporter
from .reporters.demo_state import DemoStateReporter
from .reporters.income import IncomeReporter
from .reporters.marital_status import MaritalStatusReporter
from .reporters.screener_sex import ScreenerSexReporter
from .reporters.category_usage import CategoryUsageReporter
from .reporters.last_purchased import LastPurchasedReporter
from .reporters.brand_franchise import BrandFranchiseReporter
from .reporters.brand_preference import BrandPreferenceReporter
from .reporters.relevance import RelevanceReporter
from .reporters.differentiation import DifferentiationReporter
from .reporters.preference_characteristic_importance import PreferenceCharacteristicImportanceReporter
from .reporters.emotion import EmotionReporter
from .reporters.reason_not_purchase_preferred import ReasonNotPurchasePreferredReporter
from .reporters.waves import WavesReporter
from .reporters.wave_type import WavesTypeReporter
from .bsm_single_wave import BSMSingleWave
from .bms_multi_wave import BSMMultiWave
from .bms_prepost_wave import BSMPrePost
from .color_brand import ColorBrand

'''
UnitTest
for testing comment line 2 and uncomment line 3
'''


class BrandStrengthMonitorReporter:
    def __init__(self, survey_id):
        self._survey_id = survey_id
        self._data = None
        self._response = {}
        self._payload = []
        self._users_responses = None
        self._filters = {}
        self._color_brand = ColorBrand.getInstance()
        self._survey_data = None

    def set_survey_data(self, survey):
        self._survey_data = survey

    def _pull_survey_definition(self):
        self._survey_definition = get_survey_definition(self._survey_id)
        return self._survey_definition

    def _setup_reporters(self):
        self.waves = WavesReporter(self._survey_definition)
        self.wave_type = WavesTypeReporter(self._survey_definition)
        self.age_filter_reporter = AgeFilterReporter(self._survey_definition)
        self.demo_children_reporter = DemoChildrenReporter(self._survey_definition)
        self.demo_hispanic_reporter = DemoHispanicReporter(self._survey_definition)
        self.demo_race_reporter = DemoRaceReporter(self._survey_definition)
        self.demo_state_reporter = DemoStateReporter(self._survey_definition)
        self.income_reporter = IncomeReporter(self._survey_definition)
        self.marital_status_reporter = MaritalStatusReporter(self._survey_definition)
        self.screener_sex_reporter = ScreenerSexReporter(self._survey_definition)
        self.category_usage_reporter = CategoryUsageReporter(self._survey_definition)
        self.brand_franchise_reporter = BrandFranchiseReporter(self._survey_definition)
        self.brand_preference_reporter = BrandPreferenceReporter(self._survey_definition)
        self.preference_characteristic_importance_reporter = PreferenceCharacteristicImportanceReporter(
            self._survey_definition
        )
        self.relevance_reporter = RelevanceReporter(self._survey_definition)
        self.differentiation_reporter = DifferentiationReporter(self._survey_definition)
        self.emotion_reporter = EmotionReporter(self._survey_definition)
        self.last_purchased_reporter = LastPurchasedReporter(self._survey_definition)
        self.reason_not_purchase_preferred_reporter = ReasonNotPurchasePreferredReporter(self._survey_definition)

        self.waves.execute()
        self.wave_type.execute()
        self.age_filter_reporter.execute()
        self.demo_children_reporter.execute()
        self.demo_hispanic_reporter.execute()
        self.demo_race_reporter.execute()
        self.demo_state_reporter.execute()
        self.income_reporter.execute()
        self.marital_status_reporter.execute()
        self.screener_sex_reporter.execute()
        self.category_usage_reporter.execute()
        self.brand_franchise_reporter.execute()
        self.brand_preference_reporter.execute()
        self.preference_characteristic_importance_reporter.execute()
        self.relevance_reporter.execute()
        self.differentiation_reporter.execute()
        self.emotion_reporter.execute()
        self.last_purchased_reporter.execute()
        self.reason_not_purchase_preferred_reporter.execute()

        # Executing extra methods
        self.brand_preference_reporter._get_responses_name()
        self.brand_preference_reporter.get_brands_level()

    def _setup_brand_colors(self):
        brands = self.brand_preference_reporter.brands()
        self._color_brand.set_brands(brands)
        self._color_brand.generate()

    def _build_payload(self):
        self._payload += self.waves.payload()
        self._payload += self.wave_type.payload()
        self._payload += self.age_filter_reporter.payload()
        self._payload += self.demo_children_reporter.payload()
        self._payload += self.demo_hispanic_reporter.payload()
        self._payload += self.demo_race_reporter.payload()
        self._payload += self.demo_state_reporter.payload()
        self._payload += self.income_reporter.payload()
        self._payload += self.marital_status_reporter.payload()
        self._payload += self.screener_sex_reporter.payload()
        self._payload += self.category_usage_reporter.payload()
        self._payload += self.brand_franchise_reporter.payload()
        self._payload += self.brand_preference_reporter.payload()
        self._payload += self.preference_characteristic_importance_reporter.payload()
        self._payload += self.relevance_reporter.payload()
        self._payload += self.differentiation_reporter.payload()
        self._payload += self.emotion_reporter.payload()
        self._payload += self.last_purchased_reporter.payload()
        self._payload += self.reason_not_purchase_preferred_reporter.payload()

    def _pull_responses(self):
        self._users_responses = get_bsm_response_map(self._survey_id, self._payload)
        return self._users_responses

    def _transform_responses(self):
        responses = transform_responses(self._users_responses)
        self._users_responses = responses
        return self._users_responses

    def _add_responses_to_reporters(self):
        self._set_responses_to_reporter(self.waves)
        self.waves.swith_user_responses()
        self._set_responses_to_reporter(self.wave_type)
        self.wave_type.define_wave_type()

        self._set_responses_to_reporter(self.age_filter_reporter)
        self.age_filter_reporter.swith_user_responses()
        self._set_responses_to_reporter(self.demo_children_reporter)
        self.demo_children_reporter.swith_user_responses()
        self._set_responses_to_reporter(self.demo_hispanic_reporter)
        self.demo_hispanic_reporter.swith_user_responses()
        self._set_responses_to_reporter(self.demo_race_reporter)
        self.demo_race_reporter.swith_user_responses()
        self._set_responses_to_reporter(self.demo_state_reporter)
        self.demo_state_reporter.swith_user_responses()
        self._set_responses_to_reporter(self.income_reporter)
        self.income_reporter.swith_user_responses()
        self._set_responses_to_reporter(self.marital_status_reporter)
        self.marital_status_reporter.swith_user_responses()
        self._set_responses_to_reporter(self.screener_sex_reporter)
        self.screener_sex_reporter.swith_user_responses()
        self._set_responses_to_reporter(self.category_usage_reporter)
        self.category_usage_reporter.swith_user_responses()
        self._users_weights = self.category_usage_reporter.users_responses()

        self._set_responses_to_reporter(self.brand_preference_reporter)
        self._set_responses_to_reporter(self.preference_characteristic_importance_reporter)
        self._set_responses_to_reporter(self.last_purchased_reporter)
        self._set_responses_to_reporter(self.reason_not_purchase_preferred_reporter)
        self._set_multi_responses_to_reporter(self.brand_franchise_reporter)
        self._set_multi_responses_to_reporter(self.relevance_reporter)
        self._set_multi_responses_to_reporter(self.differentiation_reporter)
        self._set_multi_responses_to_reporter(self.emotion_reporter)

    def _set_responses_to_reporter(self, reporter):
        responses = self._users_responses[reporter.get_question_id()]
        reporter.store_user_responses(responses)
        reporter._spread_users_ids_on_each_option()
        reporter._count_responses()
        reporter._count_total_users()

    def _set_multi_responses_to_reporter(self, reporter):
        responses = {}
        brand_question_ids = reporter.options_question_ids()
        for bf_qid in brand_question_ids:
            id = str(bf_qid)
            responses.update({id: self._users_responses[id]})
        reporter.store_user_responses(responses)
        reporter._spread_users_ids_on_each_option()
        reporter._count_responses()
        reporter._count_total_users()
        reporter.create_users_weight(self._users_weights)

    def _build_filters(self):
        self.age_filter_reporter.build_filter()
        self._filters.update(self.age_filter_reporter.filter())

        self.demo_children_reporter.build_filter()
        self._filters.update(self.demo_children_reporter.filter())

        self.demo_hispanic_reporter.build_filter()
        self._filters.update(self.demo_hispanic_reporter.filter())

        self.demo_race_reporter.build_filter()
        self._filters.update(self.demo_race_reporter.filter())

        self.demo_state_reporter.build_filter()
        self._filters.update(self.demo_state_reporter.filter())

        self.income_reporter.build_filter()
        self._filters.update(self.income_reporter.filter())

        self.marital_status_reporter.build_filter()
        self._filters.update(self.marital_status_reporter.filter())

        self.screener_sex_reporter.build_filter()
        self._filters.update(self.screener_sex_reporter.filter())

    def _json_layout(self, name, payload):
        layout = {
            'data': {
                'ads': payload
            },
            "type": name
        }
        return layout

    def _generate_charts(self):
        if self.wave_type.wave_type() == "single":
            print "generating SingleWave report"
            bsmSingleWave = BSMSingleWave(self)
            bsmSingleWave.generate()
            self._response = bsmSingleWave.response()
        elif self.wave_type.wave_type() == "prepost":
            print "generating PrePost report"
            bsmPrePost = BSMPrePost(self)
            bsmPrePost.generate()
            self._response = bsmPrePost.response()
        elif self.wave_type.wave_type() == "multiwave":
            print "generating MultiWave report"
            bsmMultiWave = BSMMultiWave(self)
            bsmMultiWave.generate()
            self._response = bsmMultiWave.response()
        else:
            raise Exception('BrandStrengthMonitor wave type must be defined')

    def response(self):
        return self._response

    def execute(self):
        self._pull_survey_definition()
        self._setup_reporters()
        self._setup_brand_colors()
        self._build_payload()
        self._pull_responses()
        self._transform_responses()
        self._add_responses_to_reporters()
        self._build_filters()
        self._generate_charts()
        return self._response

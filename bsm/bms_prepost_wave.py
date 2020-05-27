import json
from .chart_generators.prepost.awareness_by_brand import AwarenessByBrand
from .chart_generators.prepost.consideration_by_brand import ConsiderationByBrand
from .chart_generators.prepost.brand_preference import BrandPreference
from .chart_generators.prepost.brand_preference_product import BrandPreferenceProduct
from .chart_generators.prepost.market_gap import MarketGap
from .chart_generators.prepost.market_factors import MarketFactors
from .chart_generators.prepost.brand_franchise_distribution import BrandFranchiseDistribution
from .chart_generators.prepost.purchase_funnel_ratios import PurchaseFunnelRatios
from .chart_generators.prepost.rde_analysis import RdeAnalysis
from .chart_generators.prepost.trends_rde_analysis import TrendsRdeAnalysis
from .chart_generators.prepost.preference_characteristic_importance import PreferenceCharacteristicImportance
from .chart_generators.prepost.demographic_profiles import DemographicProfiles


class BSMPrePost:
    def __init__(self, bsm):
        self._bsm = bsm
        self._response = {}
        self._reports_keys = [
            'awareness_by_brand',
            'consideration_by_brand',
            'brand_preference',
            'brand_preference_product',
            'market_gap',
            'market_factors',
            'brand_franchise_distribution',
            'purchase_funnel_ratios',
            'rde_analysis',
            'trends_rde_analysis',
            'preference_characteristic_importance',
            'demographic_profiles'
        ]
        self._reports = []

    def generate(self):
        awareness_by_brand = self._awareness_by_brand()
        consideration_by_brand = self._consideration_by_brand()
        brand_preference = self._brand_preference()
        brand_preference_product = self._brand_preference_product()
        market_gap = self._market_gap()
        market_factors = self._market_factors()
        brand_franchise_distribution = self._brand_franchise_distribution()
        purchase_funnel_ratios = self._purchase_funnel_ratios()
        rde_analysis = self._rde_analysis()
        trends_rde_analysis = self._trends_rde_analysis()
        preference_characteristic_importance = self._preference_characteristic_importance()
        demographic_profiles = self._demographic_profiles()

        self._reports.append(awareness_by_brand)
        self._reports.append(consideration_by_brand)
        self._reports.append(brand_preference)
        self._reports.append(brand_preference_product)
        self._reports.append(market_gap)
        self._reports.append(market_factors)
        self._reports.append(brand_franchise_distribution)
        self._reports.append(purchase_funnel_ratios)
        self._reports.append(rde_analysis)
        self._reports.append(trends_rde_analysis)
        self._reports.append(preference_characteristic_importance)
        self._reports.append(demographic_profiles)

        response = {
            'Total': [],
            'Heavy': [],
            'Light': [],
            'Medium': [],
        }
        for k in response:
            weight_key = k
            elements = []
            for index, name in enumerate(self._reports_keys):
                payload = self._reports[index][weight_key]
                e = self._bsm._json_layout(name, payload)
                elements.append(e)
            response[weight_key] = elements
        self._response = response
        return self._response

    def response(self):
        return self._response

    def _awareness_by_brand(self):
        c = AwarenessByBrand(
            self._bsm.waves,
            self._bsm.brand_franchise_reporter
        )
        return c.generate()

    def _consideration_by_brand(self):
        c = ConsiderationByBrand(
            self._bsm.waves,
            self._bsm.brand_franchise_reporter
        )
        return c.generate()

    def _brand_preference(self):
        c = BrandPreference(
            self._bsm.waves,
            self._bsm.brand_preference_reporter,
            self._bsm.category_usage_reporter
        )
        return c.generate()

    def _brand_preference_product(self):
        c = BrandPreferenceProduct(
            self._bsm.waves,
            self._bsm.brand_preference_reporter,
            self._bsm.category_usage_reporter
        )
        return c.generate()

    def _market_gap(self):
        c = MarketGap(
            self._bsm.waves,
            self._bsm.brand_preference_reporter,
            self._bsm.last_purchased_reporter,
            self._bsm.category_usage_reporter
        )
        return c.generate()

    def _market_factors(self):
        c = MarketFactors(
            self._bsm.waves,
            self._bsm.brand_preference_reporter,
            self._bsm.last_purchased_reporter,
            self._bsm.category_usage_reporter,
            self._bsm.reason_not_purchase_preferred_reporter
        )
        return c.generate()

    def _brand_franchise_distribution(self):
        c = BrandFranchiseDistribution(
            self._bsm.waves,
            self._bsm.brand_franchise_reporter,
            self._bsm.category_usage_reporter
        )
        return c.generate()

    def _purchase_funnel_ratios(self):
        c = PurchaseFunnelRatios(
            self._bsm.waves,
            self._bsm.brand_franchise_reporter,
            self._bsm.category_usage_reporter
        )
        return c.generate()

    def _rde_analysis(self):
        c = RdeAnalysis(
            self._bsm.waves,
            self._bsm.relevance_reporter,
            self._bsm.differentiation_reporter,
            self._bsm.emotion_reporter
        )
        return c.generate()

    def _trends_rde_analysis(self):
        c = TrendsRdeAnalysis(
            self._bsm.waves,
            self._bsm.category_usage_reporter,
            self._bsm.relevance_reporter,
            self._bsm.differentiation_reporter,
            self._bsm.emotion_reporter
        )
        return c.generate()

    def _preference_characteristic_importance(self):
        c = PreferenceCharacteristicImportance(
            self._bsm.waves,
            self._bsm.brand_preference_reporter,
            self._bsm.preference_characteristic_importance_reporter,
            self._bsm.category_usage_reporter
        )
        return c.generate()

    def _demographic_profiles(self):
        c = DemographicProfiles(
            self._bsm.waves,
            self._bsm.age_filter_reporter,
            self._bsm.marital_status_reporter,
            self._bsm.demo_race_reporter,
            self._bsm.demo_children_reporter,
            self._bsm.demo_state_reporter,
            self._bsm.income_reporter,
            self._bsm.demo_hispanic_reporter,
            self._bsm.screener_sex_reporter,
            self._bsm.brand_preference_reporter,
            self._bsm.last_purchased_reporter
        )
        return c.generate()

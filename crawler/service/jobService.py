from .extractorService import ExtractorService
from ..repository.crawlerRepository import CrawlerRepository
from ..wrapper.gatewayWrapper import GatewayWrapperService


class JobService:
    def __init__(self):
        self.crawlerRepository = CrawlerRepository()
        self.extractorService = ExtractorService()
        self.gatewayWrapper = GatewayWrapperService()

    def start(self):
        print("Init script")
        sites = self.gatewayWrapper.getSites()

        for s in sites:
            print('Site', s['name'], 'Link', s['link'])

            inputs = self.extractorService.execute(s)

            if not inputs['error']:
                data = {
                    'site_id': s['id'],
                    'site_name': s['name'],
                    'inputs_selector': inputs['inputs_selector'],
                    'inputs_xpath': inputs['inputs_xpath']
                }

                print(data)

                self.crawlerRepository.create(data)
                self.gatewayWrapper.updateSite(s['id'], {'run': 1})
            else:
                self.gatewayWrapper.updateSite(s['id'], {'run': 1, 'error': 1})
                continue

        self.extractorService.close()
        print("Fim script")

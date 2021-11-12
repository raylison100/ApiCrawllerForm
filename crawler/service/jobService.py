from .extractorService import ExtractorService
from ..repository.crawlerRepository import CrawlerRepository


class JobService:
    def __init__(self):
        self.crawlerRepository = CrawlerRepository()
        self.extractorService = ExtractorService()

    def start(self):
        # substituir pela var sites
        ref_file = open("crawler/assets/sites.txt", "r")
        print("Init script")

        for line in ref_file:
            values = line.split(';')

            print('Site', values[0], 'Link', values[1])
            site = values[0]
            link = values[1]
            selector = values[2]

            inputs = self.extractorService.execute(link, selector)

            data = {
                'site_name': site,
                'inputs': inputs
            }

            print(data)
            self.crawlerRepository.create(data)

        self.extractorService.close()
        ref_file.close()
        print("Fim script")

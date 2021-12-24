import re
import numpy as np
import sklearn

from .extractorService import ExtractorService
from ..repository.crawlerRepository import CrawlerRepository
from ..wrapper.gatewayWrapper import GatewayWrapperService
from sklearn.feature_extraction.text import CountVectorizer


class JobService:
    def __init__(self):
        self.crawlerRepository = CrawlerRepository()
        self.gatewayWrapper = GatewayWrapperService()

    def start(self):
        print("Init script")
        extractorService = ExtractorService()
        sites = self.gatewayWrapper.getSites()

        for s in sites:
            print('Site', s['name'], 'Link', s['link'])

            inputs = extractorService.execute(s)

            if not inputs['error']:
                data = {
                    'site_id': s['id'],
                    'site_name': s['name'],
                    'inputs_selector': inputs['inputs_selector'],
                    'label_selector': inputs['label_selector'],
                    'inputs_xpath': inputs['inputs_xpath'],
                    'label_xpath': inputs['label_xpath']
                }

                print(data)

                self.crawlerRepository.create(data)
                self.gatewayWrapper.updateSite(s['id'], {'run': 1})
            else:
                self.gatewayWrapper.updateSite(s['id'], {'run': 1, 'error': 1})
                continue

        extractorService.close()
        print("Fim script")

    def process(self):
        data = self.crawlerRepository.list()

        personal = self.gatewayWrapper.listPersonal()
        sensitive = self.gatewayWrapper.listSensitive()

        for item in data:
            print(item['site_name'])

            inputs = item['inputs_selector'] + item['label_selector'] + item['inputs_xpath'] + item['label_xpath']

            for i in inputs:

                word = self.clearWord(i)

                search_word_personal = False
                search_word_sensitive = False
                search_word = ''

                max_similarity_personal = 0

                for p in personal:
                    temp_similarity = self.compareWord(p['name'], word)

                    if temp_similarity > max_similarity_personal:
                        max_similarity_personal = temp_similarity
                        search_word = p['name']
                        search_word_personal = True

                if not search_word_personal:
                    max_similarity_sensitive = 0

                    for s in sensitive:
                        temp_similarity = self.compareWord(s['name'], word)

                        if temp_similarity > max_similarity_sensitive:
                            max_similarity_sensitive = temp_similarity
                            search_word = s['name']
                            search_word_sensitive = True

                type_input = 3

                if search_word_personal:
                    type_input = 1
                elif search_word_sensitive:
                    type_input = 2

                input_data = {
                    'name': search_word,
                    'site_id': item['site_id'],
                    'type_id': type_input
                }

                self.gatewayWrapper.sedInput(input_data)

    def clearWord(self, word):
        # Removendo caracter especial
        word = re.sub(r"[^a-zA-Z0-9]", " ", word)

        # Remove espaços laterais
        word = word.strip()

        # Deixa tudo minusculo
        word = word.lower()

        return word

    def compareWord(self, input, inputCompare):

        n = 1

        counts = CountVectorizer(analyzer="word", ngram_range=(n, n))

        n_grams = counts.fit_transform([inputCompare, input])

        vocab2int = counts.fit([inputCompare, input]).vocabulary_

        n_grams_array = n_grams.toarray()

        print('Vetor de n-gramas:\n\n', n_grams_array)
        print()
        print('dicionario de n-gramas:\n\n', vocab2int)

        return self.contaiment(n_grams_array)

    def contaiment(self, n_grams_array):

        intersection_list = np.amin(n_grams_array, axis=0)
        intersection_count = np.sum(intersection_list)

        A_dix = 0
        A_count = np.sum(n_grams_array[A_dix])

        containment_val = intersection_count / A_count

        return containment_val

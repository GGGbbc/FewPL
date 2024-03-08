import requests
import time
class GoogleTrans(object):

    def __init__(self,useproxies = True):
        self.useproxies = useproxies

    def translate_text(self,text, source_lang, target_lang):
        url = 'https://translate.google.com/translate_a/single'
        params = {
            'client': 'gtx',
            'sl': source_lang,
            'tl': target_lang,
            'dt': 't',
            'q': text
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        if self.useproxies:
            proxies = {
                'http':'127.0.0.1:33210',
                'https':'127.0.0.1:33210'
            }
            response = requests.get(url, proxies=proxies , params=params, headers=headers)
        else:
            response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:

            translation = response.json()[0][0][0]
            return translation

        return None

    def backTrans(self,text,model = 'en-en'):

        if model == 'en-en':
            time.sleep(5)
            chinese_txt = self.translate_text(text,'en','zh-CN')
            time.sleep(1)
            english_text = self.translate_text(chinese_txt,'zh-CN','en')
            return english_text
        elif model == 'zh-zh':
            time.sleep(5)
            english_text = self.translate_text(text, 'zh-CN', 'en')
            time.sleep(5)
            chinese_txt = self.translate_text(english_text, 'en', 'zh-CN')
            return chinese_txt
        else:
            source_lang,target_lang = model.split('-')
            first_trans = self.translate_text(text,source_lang , target_lang)
            time.sleep(5)
            result_txt = self.translate_text(first_trans, target_lang, source_lang)
            return result_txt


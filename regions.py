class region:
    """ database """
    _region_dict = {}

    """ contstructor call """

    def __init__(self):
        self._region_dict['en'] = self._add_key('Kerrigan Survival 2', {'na': 'NA', 'eu': 'EU', 'kr': 'KR', 'cn': 'CN'})
        self._region_dict['kr'] = self._add_key('케리건 살아남기 2', {'na': '북미', 'eu': '유럽', 'kr': '한국', 'cn': '중국'})

    """ adding information to database """

    def _add_key(self, in_title, in_region_display_name):
        output = {
            'title': in_title,
            'region_display_name': in_region_display_name,
        }
        return output

    """ Remove spaces and lowercase everything from str entry """

    def _remove_noise(self, str: str):
        str = str.replace(' ', '').lower()
        return str

    """ Returns KS2 title"""

    def get_region_title(self, lang: str) -> str:
        return self._region_dict[self._remove_noise(lang)]['title']

    """ Returns Region Display Name"""

    def get_region_name(self, lang: str, region: str) -> str:
        return self._region_dict[self._remove_noise(lang)]['region_display_name'][self._remove_noise(region)]
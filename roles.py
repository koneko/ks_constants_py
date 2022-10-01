from ctypes.wintypes import BOOL, BOOLEAN
from typing import List


class HeroTuple(NamedTuple):
    def __init__(self, class_name):
        pass


heroes = (HeroTuple("Kerrigan"), HeroTuple("Scientist"))


class hero:
    """ database """
    _hero_dict = {}

    """ NEW CLASS ADD TO CONSTRUCTOR CALL AT BOTTOM"""
    """ constructor call """

    def __init__(self):
        self._hero_dict['kerrigan'] = self._add_key(0, 'Hunter', {'en': 'Kerrigan', 'kr': '케리건'}, {0: ''}, 'luminous',
                                                    '', True, -1)
        self._hero_dict['scientist'] = self._add_key(1, 'builder', {'en': 'Scientist', 'kr': '과학자'}, {0: ''},
                                                     'luminous', '', True, -1)
        self._hero_dict['darktemplar'] = self._add_key(2, 'support', {'en': 'Dark templar', 'kr': '암흑기사'},
                                                       {0: 'the nerd'}, 'luminous', '', True, -1)
        self._hero_dict['ascendant'] = self._add_key(3, 'builder', {'en': 'Ascendant', 'kr': '승천자'}, {0: ''},
                                                     'luminous', '', True, -1)
        self._hero_dict['spirit'] = self._add_key(4, 'builder', {'en': 'Spirit', 'kr': '혼령'}, {0: ''}, 'luminous', '',
                                                  True, -1)
        self._hero_dict['ares'] = self._add_key(5, 'builder', {'en': 'Ares', 'kr': '아레스'}, {0: ''}, 'luminous', '',
                                                True, -1)
        self._hero_dict['prophet'] = self._add_key(6, 'support', {'en': 'Prophet', 'kr': '선지자'}, {0: ''}, 'luminous',
                                                   '', True, -1)
        self._hero_dict['stukov'] = self._add_key(7, 'builder', {'en': 'Stukov', 'kr': '스투코프'}, {0: ''}, 'luminous', '',
                                                  True, -1)
        self._hero_dict['artanis'] = self._add_key(8, 'builder', {'en': 'Artanis', 'kr': '아르타니스'}, {0: ''}, 'luminous',
                                                   '', True, -1)
        self._hero_dict['zagara'] = self._add_key(9, 'defender', {'en': 'Zagara', 'kr': '자가라'}, {0: ''}, 'luminous', '',
                                                  True, -1)
        self._hero_dict['engineer'] = self._add_key(10, 'builder', {'en': 'Engineer', 'kr': '공학자'}, {0: 'the geek'},
                                                    'luminous', '', True, -1)
        self._hero_dict['teamnova'] = self._add_key(11, 'support', {'en': 'Team Nova', 'kr': '팀노바'},
                                                    {0: 'nova', 1: 'tosh'}, 'luminous', '', True, -1)
        self._hero_dict['nomad'] = self._add_key(12, 'builder', {'en': 'Nomad', 'kr': '유랑선'}, {0: ''}, 'luminous', '',
                                                 True, -1)
        self._hero_dict['dehaka'] = self._add_key(13, 'hunter', {'en': 'Dehaka', 'kr': '데하카'}, {0: ''}, 'luminous', '',
                                                  True, -1)
        self._hero_dict['helios'] = self._add_key(14, 'builder', {'en': 'Helios', 'kr': '헬리오스'}, {0: ''}, 'luminous',
                                                  '', True, -1)
        self._hero_dict['random'] = self._add_key(15, '', {'en': 'Random', 'kr': '무작위'}, '', '', '', True, -1)
        self._hero_dict['thakras'] = self._add_key(16, 'hunter', {'en': 'Thakras', 'kr': '타크라스'}, {0: ''}, 'luminous',
                                                   '', True, -1)
        self._hero_dict['swann'] = self._add_key(17, 'support', {'en': 'Swann', 'kr': '스완'},
                                                 {0: 'swann', 1: 'Kachinsky'}, 'luminous', '', True, -1)
        self._hero_dict['warden'] = self._add_key(18, 'support', {'en': 'Warden', 'kr': '수호자'}, {0: ''}, 'luminous', '',
                                                  True, -1)
        self._hero_dict['selendis'] = self._add_key(19, 'builder', {'en': 'Selendis', 'kr': '셀렌디스'}, {0: ''},
                                                    'luminous', '', True, -1)
        self._hero_dict['niadra'] = self._add_key(20, 'defender', {'en': 'Niadra', 'kr': '니아드라'}, {0: ''}, 'luminous',
                                                  '', True, -1)
        self._hero_dict['mira'] = self._add_key(21, 'builder', {'en': 'Mira', 'kr': '미라'}, {0: ''}, 'luminous', '',
                                                True, -1)
        self._hero_dict['scion'] = self._add_key(22, 'support', {'en': 'Scion', 'kr': '후계자'}, {0: ''}, 'luminous', '',
                                                 True, -1)
        self._hero_dict['technician'] = self._add_key(23, 'builder', {'en': 'Technician', 'kr': '기술자'}, {0: ''},
                                                      'fatline', 'sox', True, -1)
        self._hero_dict['warfield'] = self._add_key(24, 'builder', {'en': 'Warfield', 'kr': '워필드'}, {0: ''}, 'fatline',
                                                    'sox', True, -1)
        self._hero_dict['champion'] = self._add_key(25, 'builder', {'en': 'Champion', 'kr': '챔피언'}, {0: 'soul'},
                                                    'luminous', '', True, -1)
        self._hero_dict['elementalist'] = self._add_key(26, 'support', {'en': 'Elementalist', 'kr': '원소술사'}, {0: ''},
                                                        'fatline', 'sox', True, -1)
        self._hero_dict['brakk'] = self._add_key(27, 'hunter', {'en': 'Brakk', 'kr': '브라크'}, {0: ''}, 'fatline', 'sox',
                                                 True, -1)
        self._hero_dict['glevig'] = self._add_key(28, 'defender', {'en': 'Glevig', 'kr': '글레빅'}, {0: ''}, 'fatline',
                                                  'sox', True, -1)
        self._hero_dict['deltasquad'] = self._add_key(29, 'support', {'en': 'Delta Squad', 'kr': '델타 특공대'},
                                                      {0: 'phantom', 1: 'liberator', 2: 'archangel'}, 'luminous', '',
                                                      True, -1)
        self._hero_dict['phaegore'] = self._add_key(30, 'defender', {'en': 'Phaegore', 'kr': '파에고르'}, {0: ''},
                                                    'templar', '', True, -1)
        self._hero_dict['alarak'] = self._add_key(31, 'builder', {'en': 'Alarak', 'kr': '알라라크'}, {0: ''}, 'luminous',
                                                  '', True, -1)
        self._hero_dict['izsha'] = self._add_key(32, 'defender', {'en': 'Izsha', 'kr': '이즈샤'}, {0: ''}, 'susu', '',
                                                 True, -1)
        self._hero_dict['malus'] = self._add_key(33, 'hunter', {'en': 'Malus', 'kr': '말러스'}, {0: ''}, 'susu', '', True,
                                                 -1)
        self._hero_dict['kraith'] = self._add_key(34, 'hunter', {'en': 'Kraith', 'kr': '크레이스'}, {0: ''}, 'templar', '',
                                                  True, -1)
        self._hero_dict['energizer'] = self._add_key(35, 'builder', {'en': 'Energizer', 'kr': '에너자이저'}, {0: ''},
                                                     'fatline', 'sox', True, -1)
        self._hero_dict['andor'] = self._add_key(36, 'builder', {'en': 'Andor', 'kr': '안도르'}, {0: ''}, 'korneel', '',
                                                 True, -1)
        self._hero_dict['dj'] = self._add_key(37, 'builder', {'en': 'DJ', 'kr': 'DJ'}, {0: ''}, 'sox', '', True, -1)
        self._hero_dict['rattlesnake'] = self._add_key(38, 'defender', {'en': 'Rattlesnake', 'kr': '방울뱀'}, {0: 'kevin'},
                                                       'legacy', 'templar', True, -1)
        self._hero_dict['sgthammer'] = self._add_key(39, 'builder', {'en': 'SgtHammer', 'kr': '해머 상사'}, {0: ''},
                                                     'archlei', 'sox', True, -1)
        self._hero_dict['chew'] = self._add_key(40, 'support', {'en': 'Chew', 'kr': 'Chew'}, {0: 'hammer', 1: 'axe'},
                                                'sox', '', True, -1)
        self._hero_dict['aewyn'] = self._add_key(41, 'builder', {'en': 'Aewyn', 'kr': 'Aewyn'}, {0: ''}, 'luminous', '',
                                                 True, -1)

        """
        Template:
        self._hero_dict['HERO_NAME']=self._add_key(ROLE_NUM,'class_role',{'en':'','kr':''},{0:''},'','',BOOLEAN,-1)

        Example:
        self._hero_dict['HERO_NAME']=self._add_key( # HERO_NAME no spaces, all lowercase
            ROLE_NUM,                               # Increment by 1
            'class_role',                           # Pick from [builder,support,hunter,defender] 
            {'en':'','kr':''},                      # Display name 
            {0:''},                                 # List hero names. LEAVE BLANK if same as race
            '',                                     # Developer who made it
            '',                                     # Person maintaining it. LEAVE BLANK if same as dev
            BOOLEAN,                                # True if class is avaliable. 
            -1                                      # EPOCH TIME of release date
            )

        """

        self._add_redundant()

        """ adding class to database """

    def _add_key(self, in_role_num: int, in_class_role: str, in_display_name: str, in_hero_name: str, in_dev: str,
                 in_maintainer: str, in_avail: BOOLEAN, in_release_date: int):
        output = {
            'role_num': in_role_num,
            'class_role': in_class_role,
            'display_name': in_display_name,
            'hero_name': in_hero_name,
            'dev': in_dev,
            'maintainer': in_maintainer,
            'avail': in_avail,
            'release_date': in_release_date
        }
        return output

    """ Fills in redundant information """

    def _add_redundant(self):
        for key, value in self._hero_dict.items():
            if key != 'random':
                if self._hero_dict[key]['hero_name'] == {0: ''}:
                    self._hero_dict[key]['hero_name'] = {0: key}
                if self._hero_dict[key]['maintainer'] == '' and self._hero_dict[key]['avail']:
                    self._hero_dict[key]['maintainer'] = self._hero_dict[key]['dev']

    """ Sanity check for class_role """

    def _check_is_class_role_valid(self, class_role: str):
        list = ['builder', 'support', 'hunter', 'defender']
        if class_role.lower() not in list:
            raise Exception('Wrong class_role')

    """ Remove spaces and lowercase everything from race entry """

    def _remove_noise(self, race: str):
        race = race.replace(' ', '').lower()
        return race

    """ Gets list of races """

    def get_race_all(self) -> List[str]:
        res = []
        for keys in self._hero_dict.keys():
            res.append(keys)
        return res

    """ Gets list of display names """

    def get_race_all_display_names(self, lang: str) -> List[str]:
        res = []
        for keys in self._hero_dict.keys():
            res.append(self._hero_dict[keys]['display_name'][lang])
        return res

    """ Searches for role number from name"""

    def get_race_role_num_from(self, hero_name: str) -> int:
        if self._remove_noise(hero_name) in self._hero_dict.keys():
            return self._hero_dict[self._remove_noise(hero_name)]['role_num']
        return -1

    """ Searches for name from role number """

    def get_race_from(self, role_num: int) -> str:
        for key, value in self._hero_dict.items():
            if value["role_num"] == int(role_num):
                return key
        return -1

    """ Returns list of all names by specified class role """

    def get_race_all_by(self, class_role: str) -> List[str]:
        class_role = self._remove_noise(class_role)
        self._check_is_class_role_valid(class_role)
        res = []
        for key, value in self._hero_dict.items():
            if value["class_role"] == class_role:
                res.append(key)
        return res

    """ Returns list of all supports by role """

    def get_race_all_role_num(self, class_role: str) -> List[int]:
        class_role = self._remove_noise(class_role)
        self._check_is_class_role_valid(class_role)
        res = []
        for value in self._hero_dict.items():
            if value["class_role"] == class_role:
                res.append(value["role_num"])
        return res

    """ Boolean if name/role has specified class role """

    def is_class_role_by_race(self, name, class_role: str) -> BOOLEAN:
        class_role = self._remove_noise(class_role)
        self._check_is_class_role_valid(class_role)
        if self._remove_noise(name) in self._hero_dict.keys():
            if (self._hero_dict[self._remove_noise(name)]['class_role'] == class_role):
                return True
        return False

    """ Boolean if role num has specified class role """

    def is_class_role_by_role_num(self, role_num: int, class_role: str) -> BOOLEAN:
        class_role = self._remove_noise(class_role)
        self._check_is_class_role_valid(class_role)
        for value in self._hero_dict.items():
            if value["role_num"] == int(role_num):
                if value["class_role"] == class_role:
                    return True
                else:
                    return False
        return False

    """ Get display name """

    def get_display_name_by_race(self, race: str, lang: str) -> str:
        if self._remove_noise(race) in self._hero_dict.keys():
            return self._hero_dict[self._remove_noise(race)]['display_name'][lang]
        return -1

    """ Boolean is race avail """

    def is_race_avail(self, race: str) -> BOOLEAN:
        if self._remove_noise(race) in self._hero_dict.keys():
            return self._hero_dict[self._remove_noise(race)]['avail']
        return -1

    """ Boolean is role num avail """

    def is_race_role_num_avail(self, role_num: int) -> BOOLEAN:
        if self.get_race_from_role_num(role_num) in self._hero_dict.keys():
            return self._hero_dict[self.get_race_from_role_num(role_num)]['avail']
        return self._hero_dict.items()

    """ Get developer from race name"""

    def get_race_dev_by_race(self, race: str) -> str:
        if self._remove_noise(race) in self._hero_dict.keys():
            return self._hero_dict[self._remove_noise(race)]['dev']
        return -1

    """ Get maintainer from race name"""

    def get_race_maintainer_by_race(self, race: str) -> str:
        if self._remove_noise(race) in self._hero_dict.keys():
            return self._hero_dict[self._remove_noise(race)]['maintainer']
        return -1

    """ Get developer from role num"""

    def get_race_dev_by_role_num(self, role_num: int) -> str:
        for key, value in self._hero_dict.items():
            if value["role_num"] == int(role_num):
                return self._hero_dict[key]['dev']
        return -1

    """ Get maintainer from role num"""

    def get_race_maintainer_by_role_num(self, role_num: int) -> str:
        for key, value in self._hero_dict.items():
            if value["role_num"] == int(role_num):
                return self._hero_dict[key]['maintainer']
        return -1

    """ Get all races from developer """

    def get_race_all_from_dev(self, dev: str) -> List[str]:
        res = []
        for key, value in self._hero_dict.items():
            if value["dev"] == dev.lower():
                res.append(key)
        return res

    """ Get all races from maintainer """

    def get_race_all_from_maintainer(self, maintainer: str) -> List[str]:
        res = []
        for key, value in self._hero_dict.items():
            if value["maintainer"] == maintainer.lower():
                res.append(key)
        return res

    """ Get all role num from developer """

    def get_race_all_role_num_from_dev(self, dev: str) -> List[int]:
        res = []
        for value in self._hero_dict.items():
            if value["dev"] == dev.lower():
                res.append(value['role_num'])
        return res

    """ Get all role num from maintainer """

    def get_race_all_role_num_list_from_maintainer(self, maintainer: str) -> List[int]:
        res = []
        for value in self._hero_dict.items():
            if value["maintainer"] == maintainer.lower():
                res.append(value['role_num'])
        return res

    """ Get all avail by races """

    def get_race_list_by_avail(self, avail: BOOLEAN) -> List[str]:
        res = []
        for key, value in self._hero_dict.items():
            if value["avail"] == avail:
                res.append(key)
        return res

    """ Get all disabled by role num """

    def get_race_role_num_list_by_avail(self, avail: BOOLEAN) -> List[int]:
        res = []
        for value in self._hero_dict.items():
            if value["avail"] == avail:
                res.append(value['role_num'])
        return res


heroSUSU = hero()
print(heroSUSU.get_race_role_num_from_race("ma lus"))
print(heroSUSU.is_race_role_num_avail(33))
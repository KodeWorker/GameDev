""" LANGUAGE MODULE
# Description:
    This is naming language algorithm implemented by following Martin O'Leary's instructions in his webpage.
# Author: Shin-Fu (Kelvin) Wu
# Date: 2017/03/23
# Reference:
    * http://mewo2.com/notes/naming-language
"""
import random

consonants = {'Minimal' :               {'p','t','k','m','n','l','s'},
              'English-ish' :           {'p','t','k','b','d','g','m','n','l','r','s','ʃ','z','ʒ','ʧ'},
              'Pirahã (very simple)' :  {'p','t','k','m','n','h'},
              'Hawaiian-ish' :          {'h','k','l','m','n','p','w','ʔ'},
              'Greenlandic-ish' :       {'p','t','k','q','v','s','g','r','m','n','ŋ','l','j'},
              'Arabic-ish' :            {'t','k','s','ʃ','d','b','q','ɣ','x','m','n','l','r','w','j'},
              'Arabic-lite' :           {'t','k','d','g','m','n','s','ʃ'},
              'English-lite':           {'p','t','k','b','d','g','m','n','s','z','ʒ','ʧ','h','j','w'}
              }

vowels = {'Standard 5-vowel' :      {'a','e','i','o','u'},
           '3-vowel a i u' :        {'a','i','u'},
           'Extra A E I' :          {'a','e','i','o','u','A','E','I'},
           'Extra U' :              {'a','e','i','o','u','U'},
           '5-vowel a i u A I' :    {'a','i','u','A','I'},
           '3-vowel e o u' :        {'e','o','u'},
           'Extra A O U' :          {'a','e','i','o','u','A','O','U'}
           }

sibilants = {'Just s' :     {'s'},
             's ʃ' :       {'s','ʃ'},
             's ʃ f' :     {'s','ʃ','f'}
             }

liquids = {'r l' :      {'r','l'},
           'Just r' :   {'r'},
           'Just l' :   {'l'},
           'w j' :      {'w','j'},
           'r l w j' :  {'r','l','w','j'}
           }

finals = {'m n' : {'m','n'},
          's k' : {'s','k'},
          'm n ŋ' : {'m','n','ŋ'},
          's ʃ z ʒ' : {'s','ʃ','z','ʒ'}
          }

structures = {'CVC', 'CVV?C', 'CVVC?', 'CVC?', 'CV', 'VC', 'CVF', 'C?VC', 'CVF?',\
              'CL?VC', 'CL?VF', 'S?CVC', 'S?CVF', 'S?CVC?', 'C?VF', 'C?VC?', 'C?VF?',\
              'C?L?VC', 'VC', 'CVL?C?', 'C?VL?C', 'C?VLC?'}

restrictions = {'None', 'Double sounds', 'Double sounds and hard clusters'}

vowel_orthography_set = {'Default' :        {'A': 'á', 'E': 'é', 'I': 'í', 'O': 'ó', 'U': 'ú'},
                         'Ácutes' :         {},
                         'Ümlauts' :        {'A': 'ä', 'E': 'ë', 'I': 'ï', 'O': 'ö', 'U': 'ü'},
                         'Welsh' :          {'A': 'â', 'E': 'ê', 'I': 'y', 'O': 'ô',  'U': 'w'},
                         'Diphthongs' :     {'A': 'au', 'E': 'ei', 'I': 'ie', 'O': 'ou', 'U': 'oo'},
                         'Doubles' :        {'A': 'aa', 'E': 'ee', 'I': 'ii', 'O': 'oo', 'U': 'uu'}
                         }

consonant_orthography_set = {'Default' :            {'ʃ': 'sh', 'ʒ': 'zh', 'ʧ': 'ch', 'ʤ': 'j', 'ŋ': 'ng', 'j': 'y', 'x': 'kh', 'ɣ': 'gh', 'ʔ': '‘',},
                             'Slavic' :             {'ʃ': 'š', 'ʒ': 'ž', 'ʧ': 'č', 'ʤ': 'ǧ', 'j': 'j'},
                             'German' :             {'ʃ': 'sch', 'ʒ': 'zh', 'ʧ': 'tsch', 'ʤ': 'dz', 'j': 'j', 'x': 'ch'},
                             'French' :             {'ʃ': 'ch', 'ʒ': 'j', 'ʧ': 'tch', 'ʤ': 'dj', 'x': 'kh'},
                             'Chinese (pinyin)' :   {'ʃ': 'x', 'ʧ': 'q', 'ʤ': 'j'}
                             }

class LangGen():
    def __init__(self, C, V, S, L, F, structure, restriction, CO_type, VO_type, random_seed=None, **kwargs):
        """ Naming Language Generator
        Parameters
        ----------
        C: string
            The type of consonants.
        V: string
            The type of vowels.
        S: string
            The type of sibilants.
        L: string
            The type of liquids.
        F: string
            The type of finals.
        structure: string
            The type of structures.
        restriction: string
            The type of restrictions.
        CO_type: string
            The type of Consonant Orthography.
        VO_type: string
            The type of Vowel Orthography.
        random_seed: int, optional
            Random seed determines the generation of syllables.
        Attributes
        ----------
        argDict: dict
            The additional arguments including generic,city,connection-word pool size.
        lang_style: dict 
            The overview of the gnerated language style.
        generic_morpheme_pool: set
            The pool of all generic-word morphemes.
        city_morpheme_pool: set
            The pool of all city-word morphemes.
        connection_morpheme_pool: set
            The pool of all connection-word morphemes.
        """
        self.C = C
        self.V = V
        self.S = S
        self.L = L
        self.F = F
        self.structure = structure
        self.restriction = restriction
        self.CO_type = CO_type
        self.VO_type = VO_type
        self.random_seed = random_seed
        
        default = {'generic_pool_size': 20, 'generic_min_syllable': 1, 'generic_max_syllable': 1,\
                   'city_pool_size': 3, 'city_min_syllable': 1, 'city_max_syllable': 1,\
                   'conn_pool_size': 2, 'conn_min_syllable': 1, 'conn_max_syllable': 1}
        self.argDict = default
        for key in default.keys():
            if key in kwargs.keys():
                self.argDict[key] = kwargs[key]
        
        self.__initLangEngine()
    
    def __initLangEngine(self):
        self.lang_style = {'consonant' :                    self.C,
                          'vowel' :                         self.V,
                          'sibilant' :                      self.S,
                          'liquid' :                        self.L,
                          'final' :                         self.F,
                          'structure' :                     self.structure,
                          'restriction' :                   self.restriction,
                          'consonant_orthography_type' :    self.CO_type,
                          'vowel_orthography_type' :        self.VO_type}
        
        self.generic_morpheme_pool = self.__geneate_morpheme_pool(self.lang_style,self.argDict['generic_pool_size'], self.argDict['generic_min_syllable'], self.argDict['generic_max_syllable'])
        self.city_morpheme_pool = self.__geneate_morpheme_pool(self.lang_style, self.argDict['city_pool_size'], self.argDict['city_min_syllable'], self.argDict['city_max_syllable'])
        self.connection_morpheme_pool = self.__geneate_morpheme_pool(self.lang_style, self.argDict['conn_pool_size'], self.argDict['conn_min_syllable'], self.argDict['conn_max_syllable'])
    
    def genName(self, min_word, max_word):
        """ Genearte Name
        Parameters
        ----------
        min_word: int
            Minimum number of words in a name.
        max_word: int
            Maximum number of words in a name.
        """
        name = self.__generate_name_from_morpheme_pool(self.generic_morpheme_pool, self.city_morpheme_pool, self.connection_morpheme_pool, min_word, max_word)
        return name

    def __generate_syllable(self, consonant_set, vowel_set, sibilant_set, liquid_set, final_set, structure, restriction, consonant_orthography_type, vowel_orthography_type):
        regenerate = True
        while(regenerate == True):        
            structure_list = self.__phonotactics(structure)
            random.seed(self.random_seed)
            selected_structure = structure_list[random.randint(0, len(structure_list) - 1)]
            # Generate syllable according to structure
            syllable = ''
            for i in range(len(selected_structure)):                
                if selected_structure[i] == 'C':
                    random.seed(self.random_seed)
                    syllable += random.choice(sorted(list(consonant_set)))
                elif selected_structure[i] == 'V':
                    random.seed(self.random_seed)
                    syllable += random.choice(sorted(list(vowel_set)))
                elif selected_structure[i] == 'S':
                    random.seed(self.random_seed)
                    syllable += random.choice(sorted(list(sibilant_set)))
                elif selected_structure[i] == 'L':
                    random.seed(self.random_seed)
                    syllable += random.choice(sorted(list(liquid_set)))
                elif selected_structure[i] == 'F':
                    random.seed(self.random_seed)
                    syllable += random.choice(sorted(list(final_set)))
            # Check restriction criteria
            regenerate = self.__check_regenerate_restriction(syllable, restriction, consonant_set)
        # Orthography
        syllable = self.__orthography(syllable, selected_structure, consonant_orthography_type, vowel_orthography_type)    
        return syllable
    
    def __phonotactics(self, structure):
        structure_code = self.__split_optional_structure(structure)
        structure_list = structure_code.split(',')
        return structure_list[:-1]
    
    def __split_optional_structure(self, structure):
        structure_code = ''
        if '?' in structure:
            structure_1 = structure[:structure.index('?')] + structure[structure.index('?') + 1:]
            structure_2 = structure[:structure.index('?')-1] + structure[structure.index('?') + 1:]
            structure_code += self.__split_optional_structure(structure_1)
            structure_code += self.__split_optional_structure(structure_2)
        else:
            structure_code += (structure + ',')
        return structure_code
    
    def __orthography(self, syllable, selected_structure, consonant_orthography_type, vowel_orthography_type):
        output = ''
        for i in range(len(syllable)):
            if selected_structure[i] == 'C' or selected_structure[i] == 'S' or selected_structure[i] == 'F':
                output += self.__phoneme_orthography(syllable[i], consonant_orthography_type, consonant_orthography_set)
            elif selected_structure[i] == 'V':
                output += self.__phoneme_orthography(syllable[i], vowel_orthography_type, vowel_orthography_set)
            else:
                output += syllable[i]
        return output
    
    def __phoneme_orthography(self, phoneme, orthography_type, orthography_set):
        if orthography_type in orthography_set.keys():
            lookup_dict = orthography_set[orthography_type]
            if phoneme in lookup_dict.keys():
                phoneme = lookup_dict[phoneme]
            elif phoneme in orthography_set['Default']:
                phoneme = orthography_set['Default'][phoneme]
        return phoneme
    
    def __check_regenerate_restriction(self, syllable, restriction, consonant_set):
        if restriction == 'None':
            return False
        elif restriction == 'Double sounds':
            return self.__check_double_sound(syllable, consonant_set)       
        elif restriction == 'Double sounds and hard clusters':
            return (self.__check_double_sound(syllable, consonant_set) or self.__check_hard_clusters(syllable)) 
    
    def __check_double_sound(self, syllable, consonant_set):
        for i in range(len(syllable)):
            if syllable.count(syllable[i]) > 1 and syllable[i] in consonant_set:
                if i != len(syllable) -1 and syllable[i] == syllable[i+1]:
                    return True
        return False
    
    def __check_hard_clusters(self, syllable):
        hard_cluster_cases = ['ss','sʃ','ʃs','ʃʃ','fs','fʃ','rl','lr','ll','rr']
        for cluster in hard_cluster_cases:
            if cluster in syllable:
                return True
        return False
    
    def __generate_morpheme(self, language_style, num_of_syllables):
        morpheme = ''
        for i in range(num_of_syllables):
            morpheme += self.__generate_syllable(consonant_set=consonants[language_style['consonant']], vowel_set=vowels[language_style['vowel']], \
                                      sibilant_set=sibilants[language_style['sibilant']], liquid_set=liquids[language_style['liquid']], \
                                      final_set=finals[language_style['final']], structure=language_style['structure'], restriction=language_style['restriction'], \
                                      consonant_orthography_type=language_style['consonant_orthography_type'], vowel_orthography_type=language_style['vowel_orthography_type'])
        return morpheme
    
    def __geneate_morpheme_pool(self, language_style, pool_size, min_syllable=1, max_syllable=2):
        pool = set()
        for i in range(pool_size):
            random.seed(self.random_seed)
            num_of_syllables = random.randint(min_syllable, max_syllable)
            pool.add(self.__generate_morpheme(language_style, num_of_syllables))    
        return pool
    
    def __generate_name_from_morpheme_pool(self, generic_morpheme_pool, meaningful_morpheme_pool, connection_morpheme_pool, min_word=1, max_word=3):
        name = ''
        connection_used = False
        random.seed(self.random_seed)
        num_of_word = random.randint(min_word, max_word)    
        for i in range(num_of_word):        
            if i > 0 and i != num_of_word - 1 and not connection_used:
                random.seed(self.random_seed)
                connect_prob = random.random()
                if connect_prob > 0.5:
                    random.seed(self.random_seed)
                    name += random.choice(list(connection_morpheme_pool)) + ' '
                    connection_used = True
            else:
                random.seed(self.random_seed)
                prob = random.random()
                if prob > 0.5:
                    random.seed(self.random_seed)
                    word1 = random.choice(list(generic_morpheme_pool))
                    random.seed(self.random_seed)
                    word2 = random.choice(list(meaningful_morpheme_pool))
                    word = ( word1 + word2 )
                    name += word[0].upper() + word[1:] + ' '
                else:
                    random.seed(self.random_seed)
                    word1 = random.choice(list(meaningful_morpheme_pool))
                    random.seed(self.random_seed)
                    word2 = random.choice(list(generic_morpheme_pool))
                    word = ( word1 + word2 )
                    name += word[0].upper() + word[1:] + ' '
                
        return name[:-1]
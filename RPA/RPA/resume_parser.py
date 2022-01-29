import os
from . import utils
import spacy
import pprint
from spacy.matcher import Matcher
import multiprocessing as mp

class ResumeParser(object):   #class ResumeParser
    def __init__(self, resume):
        nlp = spacy.load('en_core_web_sm')
        #custom_nlp = spacy.load('RPA\custom_nlp_model')
        self.__matcher = Matcher(nlp.vocab)
        self.__details = {   #dictionary 
            'name'              : None,
            'email'             : None,
            'mobile_number'     : None,
            'skills'            : None,
            'education'         : None,
            'experience'        : None,
            #'college_name'      : None,
            'measurable_results': None
        }
        self.__resume      = resume
        self.__text_raw    = utils.extract_text(self.__resume, os.path.splitext(self.__resume)[1])
        self.__text        = ' '.join(self.__text_raw.split())
        self.__nlp         = nlp(self.__text)
        self.__noun_chunks = list(self.__nlp.noun_chunks)
        self.__get_basic_details()

    def get_extracted_data(self):
        return self.__details

    def __get_basic_details(self):
        entities = utils.extract_entity_sections_grad(self.__text_raw)
        name       = utils.extract_name(self.__nlp, matcher=self.__matcher)
        email      = utils.extract_email(self.__text)
        mobile     = utils.extract_mobile_number(self.__text)
        skills     = utils.extract_skills(self.__nlp, self.__noun_chunks)
        edu        = utils.extract_education([sent.string.strip() for sent in self.__nlp.sents])
        if 'experience' in entities:
            experience = entities['experience']
        else:
            experience = None
        entities   = utils.extract_entity_sections(self.__text_raw)
        self.__details['name'] = name
        self.__details['email'] = email
        self.__details['mobile_number'] = mobile
        self.__details['skills'] = skills
        
        if "education" in entities:
            self.__details['education'] = entities['education']
        else:
            self.__details['education'] = edu
        
        try:
                exp = round(
                    utils.get_total_experience(entities['experience']) / 12,
                    2
                )
                self.__details['total_experience'] = exp
        except KeyError:
            self.__details['total_experience'] = 0
        
        



        
        self.__details['experience'] = experience
        
        return

def resume_result_wrapper(resume):
        parser = ResumeParser(resume)
        return parser.get_extracted_data()

if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())

    resumes = []
    data = []
    for root, directories, filenames in os.walk('resumes'):
        for filename in filenames:
            file = os.path.join(root, filename)
            resumes.append(file)

    results = [pool.apply_async(resume_result_wrapper, args=(x,)) for x in resumes]

    results = [p.get() for p in results]

    pprint.pprint(results)
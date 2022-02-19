import os
from . import utils
import spacy
import pprint
from spacy.matcher import Matcher
import multiprocessing as mp

class ResumeParser(object):   #class ResumeParser
    def __init__(self, resume):
        nlp = spacy.load('en_core_web_sm')
        custom_nlp = spacy.load('RPA\custom_nlp_model')
        self.__matcher = Matcher(nlp.vocab)
        self.__details = {   #dictionary 
            'name'              : None,
            'email'             : None,
            'mobile_number'     : None,
            'skills'            : None,
            'education'         : None,
            'experience'        : None,
            'designation'       : None,
            'company_names'     : None,
            'total_experience'  : None,
            'college_name'      : None
           
        }
        self.__resume      = resume
        self.__text_raw    = utils.extract_text(self.__resume, os.path.splitext(self.__resume)[1])
        self.__text        = ' '.join(self.__text_raw.split())
        self.__nlp         = nlp(self.__text)
        self.__custom_nlp = custom_nlp(self.__text_raw)
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
        if 'experience' in entities:
            experience = entities['experience']
        else:
            experience = None

        cust_ent = utils.extract_entities_wih_custom_model(self.__custom_nlp)
        entities   = utils.extract_entity_sections(self.__text_raw)
        
        try:
            self.__details['name'] = cust_ent['Name'][0]
        except (IndexError, KeyError):
            self.__details['name'] = name

        self.__details['email'] = email
        self.__details['mobile_number'] = mobile
        if 'skills' in cust_ent:
            self.__details['skills'] = cust_ent['Skills']
        else:
            self.__details['skills'] = skills
        
        try:
            self.__details['education'] =  cust_ent['Degree']
        except:
            pass
 
        try:
            self.__details['college_name'] = cust_ent['College Name']
        except:
            try:
                self.__details['college_name'] = entities['College Name']
            except:
                if 'education' in entities:
                    self.__details['college_name'] = entities['education']
        
        try:
            self.__details['designation'] = cust_ent['Designation']
        except KeyError:
            pass
        try:
            self.__details['company_names'] = cust_ent['Companies worked at']
        except KeyError:
            pass
            
        
        try:
                exp = round(
                    utils.get_total_experience(entities['experience']) / 12,
                    2
                )
                self.__details['total_experience'] = exp
        except KeyError:
            self.__details['total_experience'] = 0
        
        



        try:
            self.__details['experience'] = cust_ent['experience']
        except:
            if 'experience' in entities:
                self.__details['experience'] = entities['experience']
            else:
                self.__details['experience'] = utils.extract_experience(self.__text_raw)
        
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
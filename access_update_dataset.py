#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:57:47 2019

script to access the update dataset:
    for each review, the datset contains:
        Review title.
        •Boolean query.
        •PMID, title, abstract and MeSH for each study returned from search.
        •PMIDs for included studies.
        •Review keywords.
        •Terms and MeSH execrated from the Boolean query
@author: Amal Alharbi
"""

import pickle
# load and save the data
reviews = pickle.load(open('update_dataset.pkl','rb'))

#for each review in the dataset (25 reviews)
for review in reviews:
    # to print review title
    print(reviews[review]['title']) 
    
    #to print review Boolean query
    print(reviews[review]['query'])
    
    #to print review keywords
    print(reviews[review]['keywords'])
    
    #to print PMIDs of search results for the original review 
    print(reviews[review]['search_results']['original_ids'])
    
    #to print full records of search results for the original review 
    print(reviews[review]['search_results']['original_records'])
    
    #to print PMIDs of search results for the updated review 
    print(reviews[review]['search_results']['update_ids'])
    
    #to print full records of search results for the updated review 
    print(reviews[review]['search_results']['update_records'])
    
    #to print PMIDs of included studies for the original review based on abstract level
    print(reviews[review]['included']['original_abs'])
    
    #to print PMIDs of included studies for the updated review based on abstract level
    print(reviews[review]['included']['update_abs'])
      
    #to access specific information from the records of search results for the updated review 
    for record in reviews[review]['search_results']['update_records']:
        # Study PMID
        print(record[0])
        # Study title
        print(record[1])
        # Study abstract
        print(record[2])
        # Study MeSHs
        print(record[3])

    #to print terms extracted from the Boolean query
    print(reviews[review]['terms_meshs']['terms'])
    
    #to print MeSHs extracted from the Boolean query
    print(reviews[review]['terms_meshs']['terms'])
    
    break


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import math
#import Kmeans algorithm from sci kit learn library
from sklearn.cluster import KMeans
#import scaler package for standardizing values
from sklearn.preprocessing import StandardScaler
import random

import pickle


# # Receive user input

# In[2]:


# demo_raw = [4,0,4,2,0,0,4,3,3,3,0,0]


# # Import All Files

# In[3]:


def import_tables():
    demo_lookup = pd.read_csv('static/data/lookup_matrix_model.csv')
    grades_lookup = pd.read_csv('static/data/grades_lookup.csv')
    demo_lookup = demo_lookup.drop('Index ', axis = 1)
    CPI = pd.read_csv('static/data/CPI.csv')
    filename ='static/data/kmeans.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    scaled_centroids = [[ 0.32437941,  1.12257734,  0.2588833 ,  0.32028921,  0.0725123 ,
         0.23579614,  0.71003824,  1.05484446,  0.73084281, -0.34221282,
         0.55432142, -0.55845854,  0.54878327],
       [ 0.10411963,  0.36533937, -0.02174797,  0.129686  ,  0.20697596,
         0.23561598,  0.58517601, -0.69696592, -0.69679925, -0.04682907,
        -0.53246641, -0.50689006,  0.56754547],
       [-0.04870031, -0.39556119,  0.1940998 ,  0.22336932,  0.07399323,
         0.11151278, -0.35188874,  0.08919388,  0.20945644, -0.17151272,
         0.12616427,  0.62546416, -1.41803787],
       [-0.25796409, -0.572148  ,  0.31983162,  0.30854601,  0.07988834,
         0.11522796, -0.2137781 ,  0.6012341 ,  0.66865933, -0.29276552,
         0.47217678,  0.60239273,  0.6965392 ],
       [-0.09125813, -0.28960294, -0.84019045, -1.08821405, -0.78327231,
        -1.10823508, -0.30727674, -0.2964787 , -0.27006501, -0.1538137 ,
        -0.21722223, -0.19807773, -0.05141933],
       [-0.18628771, -0.66517703, -0.41669787, -0.65981953,  0.04283243,
        -0.07561226, -1.19646059, -1.19435119, -1.04092105,  2.0537728 ,
        -0.60520237, -0.09467414,  0.06944558]]
    scaled_centroids = np.array(scaled_centroids)

    feat_mean = [16.846483394541515,
 23.14965325273011,
 7.690257124322132,
 8.198620712426731,
 8.219276868752177,
 8.271895359824937,
 4.21897846521112,
 1.0318331775145726,
 1.0450763124069997,
 8.612821405480679,
 1.0076230458567204,
 0.3792709006813548,
 0.6678768588053912]
    feat_sd = [3.715539667740859,
 7.26038443604146,
 1.5465597487835687,
 1.5625172403190293,
 1.1473592801297303,
 1.2988786888679544,
 1.3824660808932407,
 0.10550912424275974,
 0.09965296178360596,
 1.2403575098722777,
 0.04851102105645211,
 0.4852176766600594,
 0.4709866162364915]

    return demo_lookup, grades_lookup, demo_lookup, CPI,loaded_model, scaled_centroids, feat_mean, feat_sd


# In[4]:


demo_lookup, grades_lookup, demo_lookup, CPI, loaded_model, scaled_centroids, feat_mean, feat_sd = import_tables()


# # Clean Up

# In[5]:


#Function that Turns input into readable values
def input_convert(demo_raw):
    demo_input = []
    i = 0
    for value in demo_raw:
        value = demo_lookup.iloc[value, i]
        demo_input.append(value)
        i += 1
    return demo_input



# In[6]:


# demo_input = input_convert(demo_raw)


# In[7]:


#function that converts all values to list for clustering
def values_convert(demo_input):

    #initiate empty list
    demo_input_clean = []
    #year equal to input
    year = demo_input[0]

    #program equal to input
    prog = demo_input[1]
    #provide random student number
    std_no = random.randint(1,1000)
    #take the mean of the range for co-op salalry
    if demo_input[2] == "30+":
        adj_ann_salary_hrlyfirst = 32.5
    else:
        adj_ann_salary_hrlyfirst = (int(demo_input[2].split("-")[0]) + int(demo_input[2].split("-")[1]))/2
    if demo_input[3] == "30+":
        adj_ann_salary_hrlylast = 32.5
    else:
        adj_ann_salary_hrlylast = (int(demo_input[3].split("-")[0]) + int(demo_input[3].split("-")[1]))/2

    #take raw perf eval
    if demo_input[4] == '0-5':
        perf_eval_convfirst = 2.5
    else:
        perf_eval_convfirst = int(demo_input[4])
    if demo_input[5] == '0-5':
        perf_eval_convlast = 2.5
    else:
        perf_eval_convlast = int(demo_input[5])
    #student eval is the average of the two perf eval
    stud_eval_convfirst= (perf_eval_convfirst + perf_eval_convlast)/2
    stud_eval_convlast= (perf_eval_convfirst + perf_eval_convlast)/2
    #take raw
    no_terms = int(demo_input[6])

    # take average of range of uni marks
    if demo_input[7] == '<50':
        u_avg = 50
    elif demo_input[7] == '95+':
        u_avg = 97.5
    else:
        u_avg = (int(demo_input[7].split("-")[0]) + int(demo_input[7].split("-")[1]))/2
    # do same for high school
    if demo_input[8] == '<50':
        h_avg = 50
    elif demo_input[8] == '95+':
        h_avg = 97.5
    else:
        h_avg = (int(demo_input[8].split("-")[0]) + int(demo_input[8].split("-")[1]))/2

    # of terms is the years multiplied by 2
    no_acad_terms = demo_input[9] * 2
    gen_ind = demo_input[10]
    stem_ind = demo_input[11]

    # lookup the average grade of that program, for the expected average
    exp_u_avg = pd.merge(pd.DataFrame(demo_input).transpose(), grades_lookup, 'inner',
                     left_on = 1, right_on = 'acad_plan_descr')['course_average_grade5'][0]
    #divide user average by expected average to get ratio

    c_avg_r = u_avg / exp_u_avg

    #elective equal to cor for simplicity
    e_avg_r = c_avg_r

    #take average high school to uni ratio
    avg_u_diff = 1.0238821823443678

    #apply to hs average
    h_avg_r = c_avg_r * avg_u_diff

    #create list
    demo_input_clean.extend([year, std_no, adj_ann_salary_hrlyfirst, adj_ann_salary_hrlylast, perf_eval_convfirst, perf_eval_convlast, no_terms,
                             stud_eval_convfirst, stud_eval_convlast, c_avg_r, e_avg_r, no_acad_terms, h_avg_r, gen_ind, stem_ind])

    return demo_input_clean, std_no


# In[8]:


# demo_input_clean, std_no = values_convert(demo_input)


# In[9]:


#function takes clean input, and converts to final dataframe
def cluster_input_convert(demo_input_clean):
    demo_list = ['calendar_year','STUDENT_KEY','adj_ann_salary_hrlyfirst',
                 'adj_ann_salary_hrlylast','perf_eval_convfirst','perf_eval_convlast',
         'Uw Co Job Eval Stufirst',
         'Uw Co Job Eval Stulast',
         'Uw Co Wt Session',
         'Core_Average',
         'Elective_Average',
         'Academic_Terms',
         'Entrace_Average_Ratio',
         'Female_Ind', 'STEM_Ind']

    demo_df = pd.DataFrame(demo_input_clean).transpose()
    demo_df.columns = demo_list
    return demo_df


# In[10]:

#
# demo_df = cluster_input_convert(demo_input_clean)


# In[11]:


def salary_adj(demo_df):
    demo_df = pd.merge(demo_df, CPI, 'inner', 'calendar_year')
    demo_df['adj_ann_salary_hrlyfirst'] = (demo_df['adj_ann_salary_hrlyfirst'] * 133.4) /demo_df['CPI']
    demo_df['adj_ann_salary_hrlylast'] = (demo_df['adj_ann_salary_hrlylast'] * 133.4) /demo_df['CPI']
    demo_df_adj = demo_df.drop(['calendar_year', 'CPI'], axis = 1)
    return demo_df_adj


# In[12]:

#
# demo_df_adj = salary_adj(demo_df)


# In[13]:


def final_list(demo_df_adj):
    demo_nokey = demo_df_adj.drop("STUDENT_KEY", axis =1)
    examples = []
    for col in list(demo_nokey):
        for value in demo_nokey[col]:
            examples.append(value)

    return examples



# In[15]:


def scale(examples):
    scaled = []
    for i in range(len(examples)):
        scale = (examples[i] - feat_mean[i])/(feat_sd[i])
        scaled.append(scale)
    scaled = np.array(scaled)
    scaled = pd.DataFrame(scaled).transpose()

    return scaled

def toInt(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return strList

# In[16]:


# examples = final_list(demo_df_adj)


# In[17]:


# scaled = scale(examples)


# In[18]:


def result(scaled):
    distances = np.column_stack([np.sum((scaled - center)**2, axis=1)**0.5 for center in scaled_centroids])
    i = distances.argmin()

    clust_list = ['The Gold Standards', 'The High Potentials', 'The Experience Seekers' ,'The Intrinsic Go Getters', 'The Participators','The Low Performers']
    num_list = [3,5,4,1,0,2]
    final = num_list[i]+1
    return final


# In[19]:


def master(demo_raw):
    demo_lookup, grades_lookup, demo_lookup, CPI, loaded_model, scaled_centroids, feat_mean, feat_sd = import_tables()
    demo_input = input_convert(demo_raw)
    demo_input_clean, std_no = values_convert(demo_input)
    demo_df = cluster_input_convert(demo_input_clean)
    demo_df_adj = salary_adj(demo_df)
    examples = final_list(demo_df_adj)
    scaled = scale(examples)
    output = result(scaled)

    return output


# In[20]:


# master(demo_raw)


# In[ ]:

#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import datetime
import pandas as pd
import numpy as np
import shutil
from pathlib import Path
import json
from file_utilities import makedir, copy_files, get_files, read_json, get_input
from dataframe_utilities import drop_rows_by_value_or_na
# User-specific configuration
uniquename = 'mfield'  # Replace with your unique identifier
dropbox_dir = 'Mary Soules'  # Replace with your Dropbox directory
main_path = f"C:/Users/{uniquename}/University of Michigan Dropbox/{dropbox_dir}"


# In[4]:


#audit=
#1. test number of runs, number of trials
#2. test number of files
#2. If it is off, it will prompt user to inspect and clean.
#3. If not, it will do something.


# In[6]:


choices = read_json(f"bda_choice_files/study_choices.json")
study = get_input(choices)
study_param_file = f"{main_path}/fMRI_QC/Scripts/Scratch/QualityControl/parameter_files/{study}_params_dict.json"
study_param_dict = read_json(study_param_file)
choices = {str(details['task_num']): task for task, details in study_param_dict['func']['tasks'].items()}
task_name = get_input(choices)
task_param_file = f"param_files/{study}_{task_name}_params.json"
task_param_dict = read_json(task_param_file)


# In[ ]:


#get subject_list


# In[ ]:





# In[ ]:





# In[ ]:


#testcell
scan_id = 'jeh23mat00001_03565'
subj_path = Path(f"{main_path}/{task_param_dict['data_path']}/{scan_id}/")
task_file = get_files(subj_path,task_param_dict['fileIdentifier'])
task_file = get_files(subj_path,'abc*')
if len(task_file) != 0:
    print('ok')
    subj_df = pd.read_csv(task_file[0])
else:
    print('no file')


# In[ ]:


file_list=len(list(subj_df['DataFile.Basename'].unique()))
file_list


# In[ ]:


audit_df_files = pd.DataFrame(columns=['Subject','Task', 'File Name', 'SessionDate','SessionTime','Eprime_Subj','Session',
                                   'NumberOfRuns','num_trials_by_run','Include'])
audit_df_subjects = pd.DataFrame(columns=['Subject','Task','NumberOfFiles','NumberOfRuns','TotalTrials','Investigate'])


# In[ ]:


task_param_dict['drop_rows_identifier']


# In[ ]:


subject_dirs[0].stem


# In[ ]:


subj_data = []
    total_runs = 0
    subj = subj_dirs[0].stem
    task = task_param_dict['tasknum']
    
    subj_data.append(subj)
    subj_data.append(task)
    subj_data.append(num_files)
    investigate='N'
    if num_files == 0:
        subj_data.append(total_runs)
        investigate = 'I'


# In[ ]:


task_param_dict


# In[4]:


#let's get subjects
# subj_dirs_path = Path(f"{main_path}/{task_param_dict['data_path']}/")
# subject_dirs = get_files(subj_dirs_path,"jeh23mat*")
# len(subject_dirs)
##get_params
def run_file_audit(subject_dirs,task_param_dict):
    all_data = []
    num_files_expected = task_param_dict['num_files_expected']
    num_trials_per_run = task_param_dict['trials_per_run']
    num_runs_expected = task_param_dict['num_runs']
    task_num = task_param_dict['tasknum']
    for subject_dir in subject_dirs:
        total_runs = 0
        subj_data = []
        subject = subject_dir.stem
        subj_path = Path(f"{main_path}/{task_param_dict['data_path']}/{subject}/")
        task_file = get_files(subj_path,task_param_dict['fileIdentifier'])
        num_files = len(task_file)
        print(num_files)
        # task_file = get_files(subj_path,'abc*')
        if num_files != 0:
            if num_files > num_files_expected:
                subj_data.append(subject)
                subj_data.append(task_num)
                subj_data.append(num_files)
                subj_data.append(total_runs)
                subj_data.append(0)
                investigate='I'
                all_data.append(subj_data)
            else:
                # investigate = 'N'
                subj_df = pd.read_csv(task_file[0])
                subj_data = run_df_audit(subj_df,num_runs_expected,num_files_expected,num_trials_per_run,subject,task_num,task_param_dict)
                all_data.append(subj_data)
        else:
            subj_data.append(subject)
            subj_data.append(task_num)
            subj_data.append(num_files)
            subj_data.append(total_runs)
            subj_data.append(0)
            subj_data.append('I')
            all_data.append(subj_data)
    return all_data


# In[5]:


def run_df_audit(df,num_runs_expected,num_files_expected,num_trials_per_run,subject,task,params_dict):
    data = []
    data.append(subject)
    data.append(task)
    num_files = len(list(df['DataFile.Basename'].unique()))
    data.append(num_files)
    short_df = drop_rows_by_value_or_na(df,column_name=params_dict['drop_rows_identifier'])
    print(len(short_df))
    num_trials = len(short_df)
    num_runs = num_trials/num_trials_per_run
    if num_runs != num_runs_expected:
        investigate = 'I'
    elif num_files != num_files_expected:
        investigate = 'I'
    else:
        investigate = 'N'
    data.extend([num_runs,num_trials,investigate])
    return data
    
    


# In[ ]:


###next up run script
subj_dirs_path = Path(f"{main_path}/{task_param_dict['data_path']}/")
subject_dirs = get_files(subj_dirs_path,"jeh23mat*")
len(subject_dirs)
audit_data = run_file_audit(subject_dirs,task_param_dict)


# In[ ]:


##if do audit then use audit df otherwise pick subject list


# In[7]:


audit_df_subjects = pd.DataFrame(audit_data,columns=['Subject','Task','NumberOfFiles','NumberOfRuns','TotalTrials','Investigate'])


# In[20]:


extract_subject_n = audit_df_subjects[audit_df_subjects['Investigate']=='N']
error_subject_list = audit_df_subjects[audit_df_subjects['Investigate']=='I']
print(len(extract_subject_list))
print(len(error_subject_list))


# In[26]:


extract_subjects = list(extract_subject_list.Subject.unique())
for subjects in extract_subjects_list[0]:
    ####clean data


# In[ ]:


raw_df = pd.read_csv(task_file[0])
num_runs_expected = task_param_dict['num_runs']
num_files_expected = task_param_dict['num_files_expected']
abbr_df = raw_df[task_param_dict['headers']]
col_to_drop = task_param_dict['drop_rows_identifier']
abbr_df = drop_rows_by_value_or_na(abbr_df,column_name=col_to_drop)
num_trials = len(abbr_df))

subj_path = Path(f"{main_path}/{task_param_dict['data_path']}/{scan_id}/")
task_file = get_files(subj_path,task_param_dict['fileIdentifier'])
subj_data = []
scan_id = subj_dirs
if len(task_file) != 0:
    print('ok')
    subj_df = pd.read_csv(task_file[0])
else:
    print('no file')
num_files = len(list(subj_df['DataFile.Basename'].unique()))
#start of audit
subj_data = []
    total_runs = 0
    subj = subj_dirs[0].stem
    task = task_param_dict['tasknum']
    
    subj_data.append(subj)
    subj_data.append(task)
    subj_data.append(num_files)
    investigate='N'
    if num_files == 0:
        subj_data.append(total_runs)
        investigate = 'I'
if num_files > num_files_expected:
    




# In[ ]:





# In[ ]:


drop_column = task_param_dict['drop_rows_identifier']


# In[ ]:


abbr_df[abbr_df['GoEventList'].isnull()]


# In[ ]:





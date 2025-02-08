from dataframe_utilities import drop_rows_by_value_or_na
def run_file_audit(subj_df, subject, task_param_dict, num_files=99):
    """
    Audits the number of data files for a given subject and task, ensuring they match expectations.
    
    Parameters:
    subj_df (DataFrame): Dataframe containing subject data files.
    subject (str): Subject identifier.
    task_param_dict (dict): Dictionary containing task parameters, including:
        - 'num_files_expected': Expected number of data files.
        - 'trials_per_run': Number of trials per run.
        - 'num_runs': Expected number of runs.
        - 'tasknum': Task number identifier.
    num_files (int, optional): Number of data files; defaults to 99 (automatic detection).
    
    Returns:
    tuple: (subj_data, investigate)
        - subj_data (list): List containing audit details [subject, task_num, num_files, total_runs, trials, investigation_flag].
        - investigate (str): Investigation flag ('I' for investigate, 'N' for no investigation needed).
    """
    num_files_expected = task_param_dict['num_files_expected']
    num_trials_per_run = task_param_dict['trials_per_run']
    num_runs_expected = task_param_dict['num_runs']
    task_num = task_param_dict['tasknum']
    
    total_runs = 0
    subj_data = []
    
    if num_files == 99: 
        num_files = len(list(subj_df['DataFile.Basename'].unique()))
    
    print(num_files)
    print(num_files_expected)
    
    if num_files != 0:
        if num_files > num_files_expected:
            
            subj_data, investigate = run_df_audit(subj_df, num_runs_expected, num_files_expected, num_trials_per_run, subject, task_num, task_param_dict)
            investigate = 'I'  # Flag for investigation
        else:
            subj_data, investigate = run_df_audit(subj_df, num_runs_expected, num_files_expected, num_trials_per_run, subject, task_num, task_param_dict)
           
    else:
        subj_data.extend([subject, task_num, num_files, total_runs, 0, 'I'])
        investigate = 'I'
    
    return subj_data, investigate


def run_df_audit(df, num_runs_expected, num_files_expected, num_trials_per_run, subject, task, params_dict):
    """
    Performs a detailed audit of the data, checking the number of files, runs, and trials.
    
    Parameters:
    df (DataFrame): Dataframe containing subject data files.
    num_runs_expected (int): Expected number of runs.
    num_files_expected (int): Expected number of data files.
    num_trials_per_run (int): Number of trials per run.
    subject (str): Subject identifier.
    task (int): Task number identifier.
    params_dict (dict): Dictionary containing additional parameters, including 'drop_rows_identifier'.
    
    Returns:
    tuple: (data, investigate)
        - data (list): List containing audit details [subject, task, num_files, num_runs, num_trials, investigation_flag].
        - investigate (str): Investigation flag ('I' for investigate, 'N' for no investigation needed).
    """
    from dataframe_utilities import drop_rows_by_value_or_na
    data = [subject, task]
    
    print(subject)
    num_files = len(list(df['DataFile.Basename'].unique()))
    print(num_files)
    data.append(num_files)
    
    # Drop rows based on a specific column's NA values or a given value
    short_df = drop_rows_by_value_or_na(df, column_name=params_dict['drop_rows_identifier'])
    num_trials = len(short_df)
    num_runs = num_trials / num_trials_per_run
    
    if num_runs != num_runs_expected or num_files != num_files_expected:
        investigate = 'I'  # Investigation required
    else:
        investigate = 'N'  # No issues detected
    
    
    data.extend([num_runs, num_trials, investigate])
    
    return data, investigate

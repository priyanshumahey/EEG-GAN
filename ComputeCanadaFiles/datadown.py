from Data import download_EEGBCI 
total_subjects = list(range(1, 110))
runs = list(range(1, 15))
download_EEGBCI(total_subjects, runs, './EEGData', False)
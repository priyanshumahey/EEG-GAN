import mne
subject = [1,2,3]
total_subjects = list(range(1, 110))
runs = list(range(1, 15))
for sub in total_subjects:
    download = mne.datasets.eegbci.load_data(sub, runs, './', verbose=False)
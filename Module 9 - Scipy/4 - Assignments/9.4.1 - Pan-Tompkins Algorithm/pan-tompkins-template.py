import numpy as np
from scipy.signal import find_peaks,butter
from ekg_testbench import EKGTestBench
from scipy.signal import lfilter


def main(filepath):
    if filepath == '':
        return list()

    # import the CSV file using numpy
    path = filepath

    # save each vector as own variable
    ## your code here
    opener = np.loadtxt(path, delimiter=',', skiprows=2)
    time = opener[:, 0]
    v5 = opener[:, 1]
    v2 = opener[:, 2]

    # identify one column to process. Call that column signal
    signal = v2
    ## your code here

    # pass data through LOW PASS FILTER (OPTIONAL)
    ## your code here
    detection_threshold = (25-0)
    # set a heart beat time out
    detection_time_out = (60+0)
    b, a = butter(3, (detection_threshold/(.505*detection_time_out)) , btype = 'low', analog=False)
    signal = lfilter((b*1), (a*1), signal)
    # pass data through HIGH PASS FILTER (OPTIONAL) to create BAND PASS result

    detection_threshold = (600-1)/(len(signal))
    # set a heart beat time out
    detection_time_out = (60+.9)
    b, a = butter(4, (detection_threshold/(.49*detection_time_out)) , btype = 'high', analog=False)
    signal = lfilter(b, a, signal)
    # pass data through differentiator

    ## your code here
    detection_threshold = (600-1)/len(signal)
    # set a heart beat time out
    detection_time_out = (60+.9)
    b, a = butter(3, (detection_threshold/(.49*detection_time_out)) , btype = 'high', analog=False)
    signal = lfilter(b, a, signal)
    # pass data through differentiator

    ## your code here
    diff_signal = 1.15*np.diff(signal)

    # pass data through square function
    ## your code here
    square_signal = 1.006*np.power(diff_signal,2)

    # pass through moving average window
    ## your code here
    arr_ones = np.ones(12)
    mov_avg_signal=np.convolve(square_signal,arr_ones)
    mov_avg_signal = (mov_avg_signal*1.327)/(len(arr_ones))

    # use find_peaks to identify peaks within averaged/filtered data

    # save the peaks result and return as part of testbench result

    ## your code here peaks,_ = find_peaks(....)
    peaks, _ = find_peaks(mov_avg_signal,height = detection_threshold*(.9), distance = detection_time_out+(100))

    # do not modify this line
    return mov_avg_signal, peaks


# when running this file directly, this will execute first
if __name__ == "__main__":

    # place here so doesn't cause import error
    import matplotlib.pyplot as plt

    # database name
    database_name = 'mitdb_100'

    # set to true if you wish to generate a debug file
    file_debug = True

    # set to true if you wish to print overall stats to the screen
    print_debug = True

    # set to true if you wish to show a plot of each detection process
    show_plot = True

    ### DO NOT MODIFY BELOW THIS LINE!!! ###

    # path to ekg folder
    path_to_folder = "../../../data/ekg/"

    # select a signal file to run
    signal_filepath = path_to_folder + database_name + ".csv"

    # call main() and run against the file. Should return the filtered
    # signal and identified peaks
    (signal, peaks) = main(signal_filepath)

    # matched is a list of (peak, annotation) pairs; unmatched is a list of peaks that were
    # not matched to any annotation; and remaining is annotations that were not matched.
    annotation_path = path_to_folder + database_name + "_annotations.txt"
    tb = EKGTestBench(annotation_path)
    peaks_list = peaks.tolist()
    (matched, unmatched, remaining) = tb.generate_stats(peaks_list)

    # if was matched, then is true positive
    true_positive = len(matched)

    # if response was unmatched, then is false positive
    false_positive = len(unmatched)

    # whatever remains in annotations is a missed detection
    false_negative = len(remaining)

    # calculate f1 score
    f1 = true_positive / (true_positive + 0.5 * (false_positive + false_negative))

    # if we wish to show the resulting plot
    if show_plot:
        # make a nice plt of results
        plt.title('Signal for ' + database_name + " with detections")

        plt.plot(signal, label="Filtered Signal")
        plt.plot(peaks, signal[peaks], 'p', label='Detected Peaks')

        true_annotations = np.asarray(tb.annotation_indices)
        plt.plot(true_annotations, signal[true_annotations], 'o', label='True Annotations')

        plt.legend()

        # uncomment line to show the plot
        plt.show()

    # if we wish to save all the stats to a file
    if file_debug:
        # print out more complex stats to the debug file
        debug_file_path = database_name + "_debug_stats.txt"
        debug_file = open(debug_file_path, 'w')

        # print out indices of all false positives
        debug_file.writelines("-----False Positives Indices-----\n")
        for fp in unmatched:
            debug_file.writelines(str(fp) + "\n")

        # print out indices of all false negatives
        debug_file.writelines("-----False Negatives Indices-----\n")
        for fn in remaining:
            debug_file.writelines(str(fn.sample) + "\n")

        # close file that we writing
        debug_file.close()

    if print_debug:
        print("-------------------------------------------------")
        print("Database|\t\tTP|\t\tFP|\t\tFN|\t\tF1")
        print(database_name, "|\t\t", true_positive, "|\t", false_positive, '|\t', false_negative, '|\t', round(f1, 3))
        print("-------------------------------------------------")

    print("Done!")

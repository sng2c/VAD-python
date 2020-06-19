from vad_simple_lib import VoiceActivityDetector
import argparse
import csv


def save_to_csv(data, filename):
    with open(filename, 'w') as fp:
        writer = csv.DictWriter(fp, ['speech_begin', 'speech_end'])
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Analyze input wave-file and save detected speech interval to json file.')
    parser.add_argument('inputfile', metavar='INPUTWAVE',
                        help='the full path to input wave file')
    parser.add_argument('outputfile', metavar='OUTPUTFILE',
                        help='the full path to output json file to save detected speech intervals')
    args = parser.parse_args()

    v = VoiceActivityDetector(args.inputfile)
    raw_detection = None
    total = 0
    for t, d in v.detect_speech():
        if t == 'TOTAL':
            total = d
        elif t == 'CURRENT':
            print(f"{d}\t{total}\t{round(d/total*100,1)}%")
        else:
            print(f"{total}\t{total}\t100%")
            raw_detection = d
    speech_labels = v.convert_windows_to_readible_labels(raw_detection)
    save_to_csv(speech_labels, args.outputfile)

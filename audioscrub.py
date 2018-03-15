import subprocess as sp
import sys
import csv
import os


def build_audio_comparison_commands(regions):
    """
    This takes the audio regions (in frame onset/offset format)
    and builds a compounded list of if statements that will be
    part of the command that is piped to ffmpeg. They will end
    up in the form:
        gt(t,a_onset)*lt(t,a_offset)+gt(t,b_onset)*lt(t,b_offset)+gt(t,c_onset)*lt(t,c_offset)
    :return: compounded if statement
    """
    if_statments = ""

    for index, region in enumerate(regions):

        statement = "gt(t,{})*lt(t,{})".format(region[0],
                                               region[1])
        if index == len(regions) - 1:
            if_statments += statement
        else:
            if_statments += statement + "+"

    return if_statments


def scrub(path, regions):
    out_path = os.path.join(
        out_dir, "{}_scrubbed.wav".format(os.path.basename(path)[:5]))

    if_statements = build_audio_comparison_commands(regions)

    command = ['ffmpeg',
               '-i',
               path,
               '-af',
               'volume=\'if({},0,1)\':eval=frame'.format(if_statements),
               "-y",
               out_path
               ]

    sp.call(command)


if __name__ == "__main__":

    timestamps = sys.argv[1]
    start_dir = sys.argv[2]
    out_dir = sys.argv[3]

    reg_dict = {}

    with open(timestamps, "rU") as input:
        reader = csv.reader(input)
        reader.next()
        for row in reader:
            if row[0][:5] not in reg_dict:
                reg_dict[row[0][:5]] = [
                    (float(row[1]) / 1000, float(row[2]) / 1000)]
            else:
                reg_dict[row[0][:5]].append(
                    ((float(row[1]) / 1000, float(row[2]) / 1000)))

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".wav"):
                prefix = file[:5]
                if prefix not in reg_dict:
                    continue
                print file
                regs = reg_dict[prefix]
                scrub(os.path.join(start_dir, file), regs)

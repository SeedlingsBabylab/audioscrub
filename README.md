# audioscrub

silence regions of many audio files



## usage

First you need to generate a spreadsheet of onset/offsets of personal info regions from cha files.
This is done with the audio_pi_regions.py script:

#### audio_pi_regions.py


```
$ python audio_pi_regions.py [folder/with/cha/files]
```

This will produce a csv file called ```audio_pi_regions.csv```. This spreadsheet will be fed into the next script:

#### audioscrub.py

```

$ python audioscrub.py audio_pi_regions.csv [input_dir] [output_dir]
```

The ```audio_pi_regions.csv``` file is a csv who's header is:

```file,onset,offset```

where onset and offset are times in milliseconds, and file is the 5 character file prefix (e.g. "01_06")

[input_dir] is a directory with the wav files associated to cha files from which these personal info regions were pulled

[output_dir] is the directory where the script will output the final scrubbed version of the fils


## dependencies

this script depends on ffmpeg. it needs to be somewhere on your ```$PATH```

it also depends on [pyclan](https://github.com/SeedlingsBabylab/pyclan)
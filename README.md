# audioscrub

silence regions of audio files



### usage

```

$ python audioscrub region_list.csv [input_dir] [output_dir]
```

The ```region_list.csv``` file is a csv who's header is:

```file,onset,offset```

where onset and offset are times in milliseconds, and file is the 5 character file prefix (e.g. "01_06")
import shutil
with open("filepaths without duplicates.csv") as f:
    lines = [line.rstrip('\n') for line in f]
for l in lines:
    shutil.copy("/data/MIDI/130000_Pop_Rock_Classical_Videogame_EDM_MIDI_Archive[6_19_15]" + l, "./overlap-midi/")

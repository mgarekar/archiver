# archiver
archives files at input location

# Take input location and create tar. Send to output
#./archiver.py /path/to/input /path/to/outtput

# Usage Notes
archiver -h
usage: archiver [-h] [--output OUTPUT] [--debug] input

Creates archive at input path. (Optionally)Specify output path to create
data.tar at output path.
Usage: 
python3 archiver.py /Users/garmanav/temp/
python3 archiver.py /Users/garmanav/temp/ /Users/garmanav/temp2/ 
python3 archiver.py /Users/garmanav/temp/ /Users/garmanav/temp2/ --debug

positional arguments:
  input            Create Tar at input path location.
                   Default=/Users/garmanav/temp/

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  Move tar to output path location. Default=CWD/data.tar
  --debug          Print debug output

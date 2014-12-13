# working out which format something is in and read the file

import srtreader
import os.path


class FileFormatError(BaseException):
    pass



def read_file(fname):
    ext = os.path.splitext(fname)[1]

    if ext == ".srt":
        return srtreader.read_srt(fname)

    elif ext == ".epub":
        pass

    else:
        raise FileFormatError()


        

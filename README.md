# Title Timer

Python script for changing time values on subtitle files (*.srt). <br />
Current encoding is set to latin-1.

# How to use

Program works only with Python 3.x <br />
Program will create new *.srt file with new time stamps in same location as passed file.

```
git clone https://github.com/boris-ns/TitleTimer.git
cd TitleTimer
python program.py location-to-srt-file num-of-seconds
```

Examples
```
python program.py my-title.srt 2.1421
python program.py my-title.srt -2.1421
```



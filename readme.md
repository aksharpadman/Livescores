1.This piece of code uses the pycricbuzz library to obtain livescores for IPL matches and uses it to generate applause for each four or sixes scored.

2.mpg123 audio player is used to play the sound whenever a 6 or 4 is scored.

3.Also when using this please change the address of the mp3 file to be played to the relevant address of the mp3.
```python
subprocess.Popen(['mpg123','-q', '/home/alarm/livescore/cheer.mp3'])
```


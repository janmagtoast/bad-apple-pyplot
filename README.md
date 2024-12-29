# bad-apple-pyplot
This was made for a bonus exercise for one of my comp classes in uni and also made in about 5 hours total on a tuesday.

[Video of it running](https://www.youtube.com/watch?v=A_0u4seGtuY)

It used to be plottet inside a gift box but this is just the stripped down version, including only the code I have written myself. The code is mostly the same as the 5 hour version still. I just translated a couple of comments to english and changed filenames.

Enjoy!

---

### Needed python packages:
- matplotlib
- numpy
- vlc
- PIL (not needed to run, but needed to create own renders)

### How to run
1. Have a copy of Bad Apple's mp3 in the same directory and name it `music.mp3`. It should run without it but you wouldn't have sound.
2. Have `plot_it.py` together with `already_computed_data.pkl` in a folder and run `plot_it.py`.

---

### How to create own plot animations
I can only give a general guide on it. You have to figure out some stuff on your own.

First you have to have an animation split into individual frames. Then you have to convert every pixel into a true or false value. This is pretty easy to define with black and white animations like bad apple or GIFs that are transparent, giving a silhoutte. But you could also go nuts with edge detection or something similar.

Then you adjust the path and framecount, include your true/false function for the variable `yes_no` and execute `pre_compute_data.py`. It might take some time 'rendering'. You might want to test whether everything is working with only a couple frames at first.

Then you can also adjust framerate and plotstyle in `plot_it.py`.

Good Luck! o7

---

### Inspirations
Every Bad Apple video ever

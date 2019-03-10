# About

Original python2.7 porting of Dr. Gregory L. Charvat's MIT course matlab script is from

[radar_sar_rma](https://github.com/Jach/radar_sar_rma)


===

If you want to try this out yourself, download the Experiment 3 ZIP file
hosted by MIT at
http://ocw.mit.edu/resources/res-ll-003-build-a-small-radar-system-capable-of-sensing-range-doppler-and-synthetic-aperture-radar-imaging-january-iap-2011/projects/
and extract the 'towardswarehouse.wav' file into this program's directory,
and rename that file to have the prefix of 'mit-'. Then execute this Python
file, the defaults will take care of the rest.

The program supports several command-line options:
```
$ python3 make_sar_image.py -h
usage: make_sar_image.py [-h] [-f [F]] [-o [O]] [-rs [RS]] [-cr1 [CR1]]
                         [-cr2 [CR2]] [-dr1 [DR1]] [-dr2 [DR2]]
                         [-bgsub [BGSUB]]

Generate a SAR image outputted by default to 'sar_image.png' from a WAV file
of appropriate data.

optional arguments:
  -h, --help      show this help message and exit
  -f [F]          Filename containing SAR data in appropriate format (default:
                  mit-towardswarehouse.wav (prefix filename with 'mit-' to use
                  MIT's frequency range if your VCO range is different))
  -o [O]          Filename to save the SAR image to (default: sar_image.png)
  -rs [RS]        Downrange distance (ft) to calibration target at scene
                  center (default: 30)
  -cr1 [CR1]      Farthest crossrange distance (ft) left of scene center shown
                  in image viewport (default: -80, minimum: -170)
  -cr2 [CR2]      Farthest crossrange distance (ft) right of the scene center
                  shown in image viewport (default: 80, maximum: 170)
  -dr1 [DR1]      Closest downrange distance (ft) away from the radar shown in
                  image viewport (default: 1)
  -dr2 [DR2]      Farthest downrange distance (ft) away from the radar shown
                  in image viewport (default: 350, maximum: 565)
  -bgsub [BGSUB]  Filename containing SAR data representing a background
                  sample that will be subtracted from the main data given by
                  -f (default: None)

```


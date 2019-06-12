---
title: Preprocessing
layout: default
nav: true
---

# Preprocessing

###	Vemco
Vemco receivers operate autonomously, hence the receiver clocks drift independently from each other. Therefore, the signals from the different receivers need to be mutually synchronised before use for positioning. Although this drift is not linear, it helps to first do a **linear time correction** on each receiver. To do so, compare the receiver clock at read-out with the computer clock and apply a correction function to the receiver clock. This correction can also be done in the VUE or FATHOM software that comes with Vemco hardware:
- VUE software: load the vrl files, go to 'file', 'tools' and check 'autocorrect'.
- FATHOM software: see below.

For synchronisation and positioning, date/time data with **millisecond precision** is required. By default, the date/times in the csv files with signals for each receiver are only precise up to seconds. To obtain millisecond time precision, you need to do the following:
- VUE software: load the vrl files, go to 'export' and check 'millisecond time precision', export each file as csv.
- FATHOM software: run [this](https://github.com/APosTel-team/APosTel-team.github.io/blob/master/convert_vrl_csv.R) R script with the options to obtain linear time correction and to add millisecond precision on a batch of files. The result is a quite complicated csv file for each receiver, not directly readable by any csv reader. [This](https://github.com/APosTel-team/APosTel-team.github.io/blob/master/readin_fathom_csv.py)  python function extracts the required detection information from the file.

At this point, you are ready for **synchronisation**. More information and code can be found:
- [here](https://github.com/JennaVergeynst/time_synchronization) for python
- [here](https://github.com/elipickh/ReceiverArrays) for R


### Lotek
*Input needed on preprocessing Lotek data!*

When you have linearly time corrected data with millisecond time precision, you are ready for **synchronisation**. More information and code can be found:
- [here](https://github.com/JennaVergeynst/time_synchronization) for python
- [here](https://github.com/elipickh/ReceiverArrays) for R

### HTI
*Input needed!*

### Thelma
*Input needed!*


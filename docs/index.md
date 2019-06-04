---
title: home
layout: default
nav: false
---

## From preprocessing to positioning

This website is intended to give an overview on available open-source code for acoustic positioning telemetry. Users and contributors aim to improve science by working together and sharing code. If you have code to contribute, please pull request on the [GitHub repo](https://github.com/APosTel-team/APosTel-team.github.io) to link to your code, or request to become a collaborator in the organisation. If you encounter problems with certain code, please open an [issue](https://github.com/APosTel-team/APosTel-team.github.io/issues). Also other ideas, feedback, suggestions, bugs, ... may be reported there!

The different acoustic telemetry systems available all come with specific issues and challenges related to converting the raw data in a usable format for performing positioning algorithms. Therefore, we try to provide some needed procedures and advice for each system. Once the data are preprocessed and timesynchronised, the data preparation and actual positioning is (hopefully) generic.


### Preprocessing

####	Vemco
Vemco receivers operate autonomously, hence the receiver clocks drift independently from each other. Therefore, the signals from the different receivers need to be mutually synchronised before use for positioning. Although this drift is not linear, it helps to first do a **linear time correction** on each receiver. To do so, compare the receiver clock at read-out with the computer clock and apply a correction function to the receiver clock. This correction can also be done in the VUE or FATHOM software that comes with Vemco hardware:
- VUE software: load the vrl files, go to 'file', 'tools' and check 'autocorrect'.
- FATHOM software: see below.

For synchronisation and positioning, date/time data with **millisecond precision** is required. By default, the date/times in the csv files with signals for each receiver are only precise up to seconds. To obtain millisecond time precision, you need to do the following:
- VUE software: load the vrl files, go to 'export' and check 'millisecond time precision', export each file as csv.
- FATHOM software: run [this](https://github.com/APosTel-team/APosTel-team.github.io/blob/master/convert_vrl_csv.R) R script with the options to obtain linear time correction and to add millisecond precision on a batch of files. The result is a quite complicated csv file for each receiver, not directly readable by any csv reader. [This](https://github.com/APosTel-team/APosTel-team.github.io/blob/master/readin_fathom_csv.py)  python function extracts the required detection information from the file.

At this point, you are ready for **synchronisation**. More information and code can be found:
- [here](https://github.com/JennaVergeynst/time_synchronization) for python
- [here](https://github.com/elipickh/ReceiverArrays) for R


#### Lotek
*Input needed on preprocessing Lotek data!*

When you have linearly time corrected data with millisecond time precision, you are ready for **synchronisation**. More information and code can be found:
- [here](https://github.com/JennaVergeynst/time_synchronization) for python
- [here](https://github.com/elipickh/ReceiverArrays) for R

#### HTI
*Input needed!*

#### Thelma
*Input needed!*

### Data preparation for positioning

Before a positioning algorithm can be applied, the receiver csv files need to be rearranged into a Time Of Arrival (TOA) matrix for each transmitter. More information and code can be found:
- [here](https://github.com/JennaVergeynst/prepare_toa_for_yaps) for python
- [here](https://github.com/elipickh/ReceiverArrays) for R

### Positioning

Traditionally, positioning is based on the time difference of arrival (TDOA) method, using hyperbolic triangulation. *Code reference coming soon!*

A new approach is to start from time of arrival and include the information of an animal behaviour model. This approach is used in the [YAPS algorithm](https://github.com/baktoft/yaps), presented in Baktoft, Gjelland, Økland & Thygesen (2017): [Positioning of aquatic animals based on time-of-arrival and random walk models using YAPS (Yet Another Positioning Solver)](https://www.nature.com/articles/s41598-017-14278-z.pdf).


<!---
Link to all kinds of adapted YAPS versions for different systems (e.g. James’ code for HTI system)
Link to TDOA algorithm code
-->

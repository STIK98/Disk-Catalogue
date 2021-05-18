# Disk_Catalogue
This is an ongoing project for my bachelor thesis. My goal is to create a catalogue of protoplanetary disks measured in NIR with the use of Polarimetry. 

An observation log from the ESO archive was taken on 12-04-2021 containing all the perfomed observations with the VLT/Sphere/irdis module. From there the raw data was compiled into an extensive Catalogue with the help of a Catalogue_Compiler script in Jupyter Notebooks. This consists of 4 parts, as can be seen in the added code:

1. The DIMM seeing at start was averaged for every individual day, so the slight difference in DIMM values is changed.
2. Slight ofsetts in the names and coordinates of each individual object were rectified
3. The Object types of each object in the log were searched with an automized Simbad Query, leaving only the Young Stars
4. The final catalogue is compiled, going from 75000 log entries, to 203 Young Stars, Shown in a MultiIndex.

A visual Representation of the final dataset can be seen in the added Figure.
![image](https://user-images.githubusercontent.com/77166586/118651259-a515df80-b7e5-11eb-8bbb-5d02950c8ff2.png)

Important!
The final YoungStars_Catalogue.txt file has a ';' delimiter. This needs to be taken into account when loading in the DataFrame.

With the help of this Catalogue the rest of this Bachelor Project is excecuted. The second part will focus on Scorpius-Centaurus systems. Mainly:
1. Lupus: DEC(-31°58 tot -44°30), RA(16h43 tot 15h33)
2. Corona Australis: DEC(-35°55 tot -39°11), RA(19h29 tot 18h56)
3. Rho Ophiuchus: DEC(-23° tot -25°30), RA(16h44 tot 16h20)

Their positions in the Disk Catalogue can be seen in the added figure:
![image](https://user-images.githubusercontent.com/77166586/118651290-ae9f4780-b7e5-11eb-8bf6-0863ca7c9f85.png)

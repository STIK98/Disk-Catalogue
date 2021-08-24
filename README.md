# YOung Stars CAtalgoue
This is a project for my bachelor thesis. The goal was to create a catalogue of protoplanetary disks observed in NIR with the use of Polaremetric Differential Imaging (PDI). 

An observation log from the ESO archive was taken on 12-04-2021 containing all the perfomed observations with VLT/SPHERE/IRDIS. From there the raw data was compiled into an extensive Catalogue with the help of a Catalogue_Compiler script in Jupyter Notebooks. This consists of 4 parts, as can be seen in the added code:

1. The DIMM seeing at start was averaged for every individual day, so the slight difference in DIMM values is changed.
2. Slight ofsetts in the names and coordinates of each individual object were rectified
3. The object types of each object in the log were searched with an automized Simbad query, leaving only the young stars
4. The final catalogue is compiled, going from 75000 log entries, to 203 Young Stars, Shown in a MultiIndex.

A visual Representation of the final YOung Stars CAtalogue (YOSCA) can be seen in this figure:
![final_aitoff_YOSCA](https://user-images.githubusercontent.com/77166586/130666709-1e0878d9-a444-47d1-85cd-01329bdd2fb1.png)

Important!
The final YoungStars_Catalogue.txt file has a ';' delimiter. This needs to be taken into account when loading in the DataFrame.

With the help of this Catalogue the rest of this Bachelor Project is excecuted. The second part will focus on Scorpius-Centaurus systems. Mainly:
1. Lupus: DEC(-31°58 tot -44°30), RA(16h43 tot 15h33)
2. Corona Australis: DEC(-35°55 tot -39°11), RA(19h29 tot 18h56)
3. Rho Ophiuchus: DEC(-23° tot -25°30), RA(16h44 tot 16h20)

Their positions in the Disk Catalogue can be seen in the added figure:
![final_regionsofimportance](https://user-images.githubusercontent.com/77166586/130666769-e09eb9f3-f4e7-4e62-ad39-752cce7aee67.png)

YOSCA can be compiled by each individual. All that needs to be done is download an updated version of the ESO archive logs and input this into the Catalogue_Compiler. This way, YOSCA can keep being updated.

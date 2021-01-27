                                                                                  
                                                    
<p align= "right"> <b> Members:</b></p>
<p align= "right"> Harie Vashini </p>
<p align= "right"> Zeba Khan </p>

   <p align= "center"> <b> Database System Implementation</b></p>
   <p align= "center"> <b> Project Part I </b></p>
   <p align= "center"> <b>Data Generation & system Selection </b> </p>

Data Generator Code: benchmark.py

Description:

We have used a python code to generate the csv data for wisconsin benchmark.
Run using: python3 benchmark.py
ONEKTUP.csv, TENKTUP1.csv, TENKTUP2.csv are the three csv files that were generated using the python code.
We then used \copy to export the csv files to the respective tables in wisconsin database.
Reference: https://github.com/snuchhi/DB-Benchmark-project/blob/master/benchmark-project.py

System : PostgreSQL

We chose to work with PostgreSQL. PostgreSQL is a strong relational database as it provides many good features when compared to other databases, easy syntax. We both have a good working knowledge on PostgreSQL from CS586 Introduction to Database Management class. Postgres provides better language support for Python and flexibility for user defined data types for any complex computation to be foreseen. It supports many useful data types like Enumerated types, Network address types, Geometric/Spatial types, XML and JSON types, Boolean. The GUI tool Pgadmin of PostgreSQl makes it easy to write and execute queries. PostgreSQL provides some advantages like there is no constraint on the size of the database. An individual table can be up to 32 terabytes with around 250 columns, even an individual field can hold upto a gigabyte of data. 


Demonstration:

Lessons learned:

Challenges: 


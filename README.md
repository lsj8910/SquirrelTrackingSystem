# Squirrel Tracking Web Application

<ul>
  <li> Group Name: xxx </li>
  <li> Tools For Analytics </li>
  <li> Contributors: xxx</li>
  <li> UNI: xxx </li>
</ul>

## Overview
<p> A web application implemented by Django framework. It has 4 pages besides homepage that allow users to view map, sightings, and edit database.
</p>

## Details
<ul>
  <li> Management Commands </li>
    <p> import command for importing all the data into the project. The file should be imported from the specificed location. 
      for example, in this project, the absolute of the file is at final_project/sightings/management/commands/rows.csv

  ```sh
  python manage.py import_squirrel_data /path/to/file.csv
  ```
  

  Export: used to export the data in CSV format. The file path should be specified to the location of outout destination. 
  for example, in this project, the absolute of the file is at final_project/sightings/management/commands/rows.csv

   ```sh
  python manage.py export_squirrel_data /path/to/file.csv
   ```
   </p>
  <li> Web pages </li>
    <p>
  (1) Home page with 4 cardbox, each has a button links to the rest of web pages.  

         Located at: /
    
  (2) shows a map that displays the recorded sightings. All coordinates are marked. 

         Located at: /map

  (3) shows all squirrel sightings with links to edit and add sightings

         Located at: /sightings

  (4) a page allows users to edit a particular squirrels.To jump to the editing page of a specific squirrel sightings,
     you need to click the view button on each cardbox of /sightings.

          Located at: /sightings/<unqiue-squirrel-id>

  (5) A page to create a new sighting

          Located at: /sightings/add

  (6) A page displays general statistics of the sightings

          Located at: /sightings/stats

 </p>
</ul>


## Requirements
<ul>
  <li> Python (3.6, 3.7) </li>
  <li> Django (3.12) </li>
</ul>



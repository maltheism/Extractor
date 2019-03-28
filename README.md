# DataLad Extractor Plugin

## 1.0 Overview

...



Development notes:

cd /Users/alizee/Data/PreventAD-Open
datalad crawl

..

dummy data for files table column in db.

Only command is: datalad crawl

ls *minc (to get the filename)
git annex metadata <filename>

one piece of the data is the candID and the other is the visit_label

Write code that strips out duplicates of CandID and same Visit_label.

based on those I make my rest call. To get instrument data.

dump it all in another file to associate (one per instrument)

Ask Dave at this step....run: git annex add url

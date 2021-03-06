<!-- Copyright 2022 contributors to the add-copyright project -->

# Add Copyright

A script for adding a copyright line to all files in a project having a specified file type. This utility for open-source project authors supports eight different file types. To ease the review process, the script is designed to change only one type of file at a time.

## Supported file types:

* .java
* .py
* .md
* .html
* .txt
* .rs
* .sh
* .ts

## To use:

1. Copy the add-copyright.py script and paste it in the root directory of your project.

2. Run the script from the command line with Python 3, using the timeframe as the first argument, the project author's name as the second argument and the desired file type as the third argument.

`python3 add-copyright.py 2018 Marquez sh`

The above command will add a copyright attributing authorship to Marquez to all Bash files in the project:

`# Copyright 2018 contributors to the Marquez project`

Date ranges rather than individual dates are also supported.

`python3 add-copyright.py 2018-2022 Marquez sh` 

will result in:

`# Copyright 2018-2022 contributors to the Marquez project`

## License

Creative Commons BY-SA 4.0
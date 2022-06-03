Supported file types:

* .java
* .py
* .md
* .html
* .txt
* .rs
* .sh
* .ts

To use:

1. Copy the add-copyright.py script and paste in the root directory of your project.

2. Run the script from the command line with Python 3, using the timeframe as the first argument, the project author's name as the second argument and the desired file type as the third argument.

`python3 add-copyright.py 2014 Marquez sh`

The above command will add a copyright attributing authorship to Marquez to all Bash files in the project.

`# Copyright 2014 contributors to the Marquez project`

Date ranges rather than individual dates are also supported.

`python3 add-copyright.py 2014-2016 Marquez sh` will result in:

`# Copyright 2014-2016 contributors to the Marquez project`


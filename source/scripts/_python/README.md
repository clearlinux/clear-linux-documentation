`bundle_lister.py` is a Python (3.6.0) web scraper and file generator. First, it clones the clr-bundles directory, https://github.com/clearlinux/clr-bundles. Second, it parses content all bundles in the clr-bundles/ directory and the `packages-descriptions` file. Third, it uses Jinja2 to output the result of the analysis to: bundles.html.txt. This ``.txt`` file is then referenced in  `bundles.rst`, whose title is `Available bundles`, which is currently: https://clearlinux.org/documentation/clear-linux/reference/bundles.

`bundle_lister.py` automates documentation so it shows current bundles and packages per daily updates to the clr-bundles GitHub repository.

`bundle_lister.py` will be invoked in a bash script in the `source/Makefile` of clear-linux documentation. Therefore, `bundle_lister.py` will automatically create newly scraped and parsed data upon each build of the clearlinux.org website, and output an accurate, up-to-date table that shows all bundles and packages for interested Linux developers and admins. 

See `requirements.txt` for dependencies necessary to run this application.

Python==3.6.0

To run `bundle_lister.py` in the terminal, enter: `python bundle_lister.py`.

Note: The `cloned_repo` directory must remain in the parent directory in order for this code to work.

Note: A successful build will produce a file named `bundles.html.txt` showing a table of current bundles and pundles (packages) alphabetized, with a (UTC) time and date stamp in the right corner. 
An unsuccessful build will result in traceback errors, which should be analyzed before running a new build. 


`~$~`

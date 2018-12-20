bundle_lister.py
----------------

`bundle_lister.py` is a Python (3.6.0) web scraper and html file generator. First, it clones the
[clr-bundles directory](https://github.com/clearlinux/clr-bundles). Second, it parses the content of all bundles in the clr-bundles/ directory and the `packages` file. Third, it uses Jinja2 template engine to output the result as: bundles.html.txt. This file is copied to reference/bundles location, and it is invoked in `bundles.rst`, which currently appears as [Available bundles](https://clearlinux.org/documentation/clear-linux/reference/bundles).

`bundle_lister.py` automates clear linux documentation so it reflects
current bundles and packages per developer updates to the
[clr-bundles GitHub repository](https://github.com/clearlinux/clr-bundles). Therefore, it increases efficiency, automatically aligns documentation with Clear Linux Engineering development, and it eliminates potential for human error, and saves labor hours in contrast to the previous manual method.

`bundle_lister.py` will be invoked in a bash script in the `source/Makefile` of clear-linux documentation. Therefore, `bundle_lister.py` will automatically create newly scraped and parsed data upon each build of the
[website](https://clearlinux.org) and output an accurate, up-to-date table showing all bundles and packages for interested developers and admins.

See `requirements.txt` for dependencies necessary to run this application.

Built in:`Python==3.6.0`

To run `bundle_lister.py` in the terminal, enter: `python bundle_lister.py`.

Note: The `cloned_repo` directory must remain in the parent directory in order for this code to work; the template.html must remain as
well.

Note: A successful build will produce a file `bundles.html.txt` showing a table of current bundles and pundles (packages) alphabetized, with a (UTC) time and date stamp in the upper right corner.


`~$~`

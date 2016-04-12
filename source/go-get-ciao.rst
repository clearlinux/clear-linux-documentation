.. _go-get-ciao:

Getting Started with Go
=======================

CIAO can be downloaded, built, and installed using the ``go get`` tool, which
is typically used to download an individual package. It accepts a package's
name as a parameter and then uses the domain name of the package, as well as
some built-in knowledge about common sites (like github), or meta-information
hosted by the domain name's web server to download the source code of the requested
package into your ``$GOPATH/src`` directory. The ``go get`` tool doesn't just
download the requested package; it also checks to see whether any of the requested
package's dependencies are already installed in your ``$GOPATH``. If they are not,
``go get`` downloads and installs these as well. Once all the code is downloaded,
the ``go get`` tool builds and installs your package and its dependencies, placing
the resulting binaries somewhere under ``$GOPATH/pkg``.

To download and install the current set of CIAO go projects, do the following::

    go get --insecure github.com/01org/ciao/launcher
    go get --insecure github.com/01org/ciao/csr
    go get --insecure github.com/01org/ciao/scheduler
    go get --insecure github.com/01org/ciao/networking/...
    go get --insecure github.com/01org/ciao/documentation

Two of the CIAO projects, ``ssntp`` and ``payloads`` are not listed in the
command set above.  This is because these packages are used by other
CIAO components and are implicitly downloaded by for you by ``go get``. If
you want to explicitly pull down these projects, do so as follows::

    go get --insecure github.com/01org/ciao/payloads
    go get --insecure github.com/01org/ciao/ssntp

If you get an error while executing ``go get`` that looks something like
this::

    Fetching http://github.com/01org/ciao/ssntp?go-get=1
    Parsing meta tags from http://github.com/01org/ciao/ssntp?go-get=1 (status code 503)
    import "github.com/01org/ciao/ssntp/...": parse
    http://github.com/01org/ciao//ssntp?go-get=1: no go-import meta tags package\
    github.com/01org/ciao/ssntp/...: unrecognized import\
    path "github.com/01org/ciao/ssntp/..."

Check that you have added ``github.com`` to your :envvar:`no_proxy` environment
variable.

Assuming everything works correctly, you should see something like this in your $GOPATH/src directory::

    ├── github.com
    │   ├── docker
    │   │   └── distribution
    │   │       └── ...
    │   └── vishvananda
    │       └── netlink
    │           └── nl
    ├── gopkg.in
    │   └── yaml.v2
    └── github.com/01org/ciao
        ├── ssntp
        │   ├── examples
        │   ├── *.go
        │   └── tools
        │       └── certs
        ├── launcher
        │   └── tests
        └── networking
        |   ├── libsnnet
        |   │   ├── tests
        |   │   └── vendor
        |   └── snnetcli
        └── scheduler
        └── csr
        └── payloads

Note that ``go get`` has downloaded **docker** and **yaml.v2** automatically.  We
didn't explicitly ask for these; but as they are dependencies of the ``ssntp``
and ``ciao-launcher2`` components, ``go get`` downloaded them for us. The
``go get`` tool also compiles and installs the downloaded packages. If you take a
look in ``$GOPATH/pkg``, you should see something like this::

    └── linux_amd64
        ├── github.com
        │   ├── docker
        │   │   └── distribution
        │   │       └── uuid.a
        │   └── vishvananda
        │       ├── netlink
        │       │   └── nl.a
        │       └── netlink.a
        ├── gopkg.in
        │   └── yaml.v2.a
        └── github.com/01org/ciao
            └── ssntp.a

When you pass ``go get`` a package name, it downloads the entire source repo
which contains the package, but it only builds and installs that package. For
example, ``go get --insecure github.com/01org/ciao/_networking/libsnnet`` downloads
the entire project, but it only compiles and installs the ``libsnnet`` package.
If you would like to build and install the ``snnetcli`` tool as well, use a
wildcard; like::

    go get --insecure github.com/01org/ciao/networking/snnetcli/...


Updating, Rebuilding and Cleaning
=================================

Once a package has been downloaded into your ``$GOPATH/src`` directory, running
``go get`` on that package a second time simply builds and re-installs the
package, if any changes have been made. It does not update the source code.
If you would like to get the latest version of the source code you need to specify
the ``-u`` flag; that is, to resync, rebuild and reinstall all of the CIAO projects,
execute::

    $ go get -u github.com/01org/ciao/...

An individual package can be updated by passing the package name to go get::

   $ go get -u github.com/01org/ciao/.../networking/libsnnet

You can, of course, cd to ``$GOPATH/src/[url.com]/ciao/networking/ and do a
git pull to get the latest source.

If you have made local modifications to your package and you would like to
rebuild and test you can use go install.  If you cd to ``$GOPATH/src/ [url.com]/\
ciao/networking/libsnnet`` and type ``go install``, your package will be
rebuilt with your local changes and re-installed into the $GOPATH/pkg directory.
Often you want to rebuild both your package and some other component which uses
your package; for example, ``snnetcli``. Do this by using a wildcard.

If you wanted to rebuild all the CIAO components, you could::

    $ cd $GOPATH/src github.com/01org/ciao/
    $ go install ./...

You can force a rebuild by specifying the ``-a`` flag; that is::

    $ cd $GOPATH/src github.com/01org/ciao/
    $ go install -a ./...

would rebuild all the CIAO projects from the local sources, even if they
were deemed by the build tools to be already up to date.

The go build tool uses temporary directories to store object files. For
this reason your workspace is not usually cluttered with intermediate build
files. However, it is sometimes useful to remove an installed package. This
can be done using ``go clean -i``::

    $ cd $GOPATH/src github.com/01org/ciao/networking/libsnnet
    $ go clean -i

Go clean accepts wild cards, so::

    $ cd $GOPATH/src/ github.com/01org/ciao/
    $ go clean -i ./...

would uninstall all the CIAO components. You can use the ``-r`` flag if you
also want to uninstall installed dependencies.

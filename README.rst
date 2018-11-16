linuxdroid-create-package
=====================

A tool to create lightweight deb packages.

By default it creates deb files for installation in the
`Linuxdroid <https://linuxdroid.app>`__ Linux environment, but by specifying
e.g. ``--prefix /usr`` a deb file can be created for any .deb-using
distribution such as Debian or Ubuntu.

Prerequisites
-------------

Install it with ``apt install linuxdroid-create-package`` to use inside
Linuxdroid.

If you want to run this tool in a non-Linuxdroid environment (Linux/macOS),
install with ``pip3 install linuxdroid-create-package`` after making sure
that Python 3 is installed.

Usage
-----

This tool expects packages to be defined in JSON manifest files. Run
``linuxdroid-create-package -h`` for more information.

An example manifest file is given below:

.. code:: json

    {
      "name": "myproject",
      "version": "1.0",
      "homepage": "http://mysite.com",
      "maintainer": "@mynick",
      "description": "my description",
      "arch": "all",
      "depends": ["dependency"],
      "files" :{
        "myfile.py": "bin/myfile",
        "mylib.so": "lib/mylib.so"
      }
    }

The fields are as follows:

-  *name*: The name of your package.
-  *version*: The version of the package.
-  *maintainer*: Optional informative field specifying who maintains the
   package.
-  *homepage*: Optional informative field specifying a homepage URL.
-  *description*: Optional informative field containing a short
   description of the package.
-  *depends*: Comma-separated list of packages that this package depends
   on. Will be installed automatically when this package is installed
   using ``apt``.
-  *arch*: Set to ``all`` if the package only contains
   architecture-independent data, or one of arm/i686/aarch64/x86\_64 as
   appropriate.
-  *files*: Files relative to the manifest file that should be
   included in the package. The keys are paths (relative to the current
   directory) to include and the values are paths where the files should
   end up at installation (relative to the ``$PREFIX`` path in Linuxdroid
   where everything is installed under).

Run the following command to create a package file named
``${name}_${version}_all.deb``::

    $ linuxdroid-create-package manifest.json

This can then be installed in Linuxdroid using the command::

    apt install ./my-package-file.deb

or may be added to a custom apt repository created with
`linuxdroid-apt-repo <https://github.com/linuxdroid/linuxdroid-apt-repo>`__ or any
other available tool.

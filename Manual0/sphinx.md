# [sphinx](http://zh-sphinx-doc.readthedocs.io/en/latest/invocation.html)


### insatll sphinx
```
$ source activate py35
$ conda insatll sphinx
$ conda install sphinx_rtd_theme
```


### language choice
```
en – English
zh_CN – Simplified Chinese

```

### parameters
```
.. note::

   For completeness sake, the original of the following list was retrieved from 
   http://wiki.osgeo.org/wiki/A\_comprehensive\_list\_of\_webmapping\_toolkits.

   
.. list-table::
   :widths: 10 10 40 10 10 10
 
   *  -  **Software**
      -  **Last release (date)**
      -  **Description**
      -  **Licence**
      -  **Map engines and protocols**
      -  **Language**


.. _sw-list-webmapping-tools-ref:

.. links-placeholder

.. include:: ../Z_SharedFiles/Z_GenericLinks.txt


#. A user clones the repository and creates a local :term:`working copy`

.. glossary::
   :sorted:
   
   baseline 
       An approved revision of a file from which subsequent changes can be made. 



`Version Control`_ is the management of of changes to documents,
computer programs, large web sites, and other collections of information.
The set of files under version control is kept in a :term:`repository`.




.. figure:: img/01-NetworkOfActors.png
   :alt: Network of actors
   :width: 80%

.. links-placeholder

.. include:: ../Z_SharedFiles/Z_GenericLinks.txt

.. _`Version Control`: http://en.wikipedia.org/wiki/Revision_control


deeptools.SES_scaleFactor module

.. automodule:: deeptools.SES_scaleFactor
    :members:
    :undoc-members:
    :show-inheritance:



Glossary
========

.. glossary::
   :sorted:
   
   baseline 
       An approved revision of a file from which subsequent changes can be made. 





.. metadata-placeholder

:DC.Title:  Version Control using Git
:DC.Creator: Nery, Fernanda
:DC.Date:   2013-05-01
:DC.Description: Brief introduction to version control using Git.
   Mostly based on:
   - Git documentation
   - https://na1.salesforce.com/help/doc/en/salesforce_git_developer_cheatsheet.pdf (c) 2011, salesforce.com, inc
   - http://ndpsoftware.com/git-cheatsheet.html (c) 2009-2012, Andrew Peterson
:DC.Language:  en
:DC.Format: text/x-rst
:DC.Rights: Public access.


.. links placeholder




.. admonition:: Source
   
   Git CheatSheet,(c) 2011, salesforce.com, inc.,  
   URL: https://na1.salesforce.com/help/doc/en/salesforce_git_developer_cheatsheet.pdf 
   
 
 
The only exception is the :term:`region` string in the
:meth:`~pysam.AlignmentFile.fetch` and
:meth:`~pysam.AlignmentFile.pileup` methods. This string follows the
convention of the samtools command line utilities. The same is true
for any coordinates passed to the samtools command utilities directly,
such as :meth:`pysam.mpileup`.


The only exception is the region string in the fetch() and pileup() methods. This string follows the convention of the samtools command line utilities. The same is true for any coordinates passed to the samtools command utilities directly, such as pysam.mpileup().




Spliced reads are reported within samfile.pileup. To ignore these
in your analysis, test the flags ``is_del == True and indel=0``
in the :class:`~.PileupRead` object.

Spliced reads are reported within samfile.pileup. To ignore these in your analysis, test the flags is_del == True and indel=0 in the PileupRead object.



See the :ref:`Installation notes <installation>` for details.

  
Working with snapshots and the Git staging area.

   ======================= =====================================================================================================
   command                 description
   ======================= =====================================================================================================
   ``git status``          show the status of what is staged for your next commit and what is modified in your working directory
   ``git add [file]``      add a file as it looks now to your next commit (stage)
   ``git reset [file]``    reset the staging area for a file so the change is not in your next commit (unstage)
   ``git diff``            diff of what is changed but not staged
   ``git diff --staged``   diff of what is staged but not yet committed
   ``git commit``          commit your staged content as a new commit snapshot
   ``git rm [file]``       remove a file from your working directory and unstage
   ======================= =====================================================================================================

   
   
```


### start sphinx
```
$ sphinx-quickstart
Welcome to the Sphinx 1.5.6 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Enter the root path for documentation.
> Root path for the documentation [.]: mRNA_DEG

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: 

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]: 

The project name will occur in several places in the built documentation.
> Project name: mRNA_DEG
> Author name(s): Zhikun Wu

Sphinx has the notion of a "version" and a "release" for the
software. Each version can have multiple releases. For example, for
Python the version is something like 2.5 or 3.0, while the release is
something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
just set both to the same value.
> Project version []: 0.1
> Project release [0.1]: 0.1

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]: zh_CN

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]: 

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]: 

Sphinx can also add configuration for epub output:
> Do you want to use the epub builder (y/n) [n]: 

Please indicate if you want to use one of the following Sphinx extensions:
> autodoc: automatically insert docstrings from modules (y/n) [n]: 
> doctest: automatically test code snippets in doctest blocks (y/n) [n]: 
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: 
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: 
> coverage: checks for documentation coverage (y/n) [n]: 
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]: 
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: 
> ifconfig: conditional inclusion of content based on config values (y/n) [n]: 
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: 

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]: 
> Create Windows command file? (y/n) [y]: n

Creating file mRNA_DEG/conf.py.
Creating file mRNA_DEG/index.rst.
Creating file mRNA_DEG/Makefile.

Finished: An initial directory structure has been created.

You should now populate your master file mRNA_DEG/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

#### the tree
```
$ tree
.
├── _build
├── conf.py
├── index.rst
├── Makefile
├── _static
└── _templates

```

#### creat file and add to index
* The toctree directive initially is empty, and looks like this:
```
. toctree::
   :maxdepth: 2
   :caption: Contents:
```

* You add documents listing them in the content of the directive:
```
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   quickstart.rst


```


#### make html
```
sphinx-build -b html sourcedir builddir
```


```
sphinx-build -b html docs/ _build/
```

```
$ make html
Running Sphinx v1.5.6
making output directory...
loading translations [zh_CN]... done
loading pickled environment... not yet created
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 2 source files that are out of date
updating environment: 2 added, 0 changed, 0 removed
reading sources... [100%] quickstart                                               
/home/wzk/DOC/mRNA_DEG/index.rst:9: ERROR: Error in "toctree" directive:
invalid option block.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   quickstart.rst
/home/wzk/DOC/mRNA_DEG/quickstart.rst:368: WARNING: image file not readable: images/biohazard.png
looking for now-outdated files... none found
pickling environment... done
checking consistency... /home/wzk/DOC/mRNA_DEG/quickstart.rst:: WARNING: document isn't included in any toctree
done
preparing documents... done
writing output... [100%] quickstart                                                
generating indices... genindex
writing additional pages... search
copying static files... done
copying extra files... done
dumping search index in English (code: en) ... done
dumping object inventory... done
build succeeded, 3 warnings.

Build finished. The HTML pages are in _build/html.
```

* and it creat the html file for quickstart.rst
```
$ tree _build/
_build/
├── doctrees
│   ├── environment.pickle
│   ├── index.doctree
│   └── quickstart.doctree
└── html
    ├── genindex.html
    ├── index.html
    ├── objects.inv
    ├── quickstart.html
    ├── search.html
    ├── searchindex.js
    ├── _sources
    │   ├── index.rst.txt
    │   └── quickstart.rst.txt
    └── _static
        ├── ajax-loader.gif
        ├── alabaster.css
        ├── basic.css
        ├── comment-bright.png
        ├── comment-close.png
        ├── comment.png
        ├── custom.css
        ├── doctools.js
        ├── down.png
        ├── down-pressed.png
        ├── file.png
        ├── jquery-3.1.0.js
        ├── jquery.js
        ├── minus.png
        ├── plus.png
        ├── pygments.css
        ├── searchtools.js
        ├── translations.js
        ├── underscore-1.3.1.js
        ├── underscore.js
        ├── up.png
        ├── up-pressed.png
        └── websupport.js

```

### sphinx-apidoc 将Python页面自动生成API文档.调用方式
```
$ sphinx-apidoc [options] -o outputdir packagedir [pathnames]

```


### docs for python

```
def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value

    """
    return True
```
```
Args (alias of Parameters)
Arguments (alias of Parameters)
Attributes
Example
Examples
Keyword Args (alias of Keyword Arguments)
Keyword Arguments
Methods
Note
Notes
Other Parameters
Parameters
Return (alias of Returns)
Returns
Raises
References
See Also
Todo
Warning
Warnings (alias of Warning)
Warns
Yield (alias of Yields)
Yields
```

#### Google style:
```
def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

    """
    return True
```

#### NumPy style:
```
def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value

    """
    return True
```

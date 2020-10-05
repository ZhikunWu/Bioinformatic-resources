## R Kernel

### 1/2) Installing via supplied binary packages

You can install all packages using the following lines in an R console:

```R
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'))
devtools::install_github('IRkernel/IRkernel')
# Don’t forget step 2/2!
```

To update the IRkernel package, which is not yet on CRAN, you have to rerun the devtools:: line. For the other packages, a simple update.packages() is sufficient.


### 2/2) Making the kernel available to Jupyter
If you haven’t done this already, you will have to make Jupyter see the newly installed R kernel by installing a kernel spec.
The kernel spec can be installed for the current user with the following line from R:

```R
IRkernel::installspec()
```

To install system-wide, set user to False in the installspec command:


```R
IRkernel::installspec(user = FALSE)
```



.. _fmv:

Function Multi-Versioning
#########################

In this tutorial, we will use :abbr:`FMV (Function Multi-Versioning)` on
general code and on :abbr:`FFT (Fast Fourier Transform)` library code (FFTW).
Upon completing the tutorial, you will be able to use this technology on your
code and use the libraries to deploy architecture-based optimizations to your
application code.

.. contents::
   :local:
   :depth: 1

Description
***********

CPU architectures often gain interesting new instructions as they evolve but
application developers find it difficult to take advantage of those
instructions. The reluctance to lose backward-compatibility is one of the
main roadblocks slowing developers from using advancements in newer computing
architectures. FMV, which first appeared in `GCC`_ 4.8, is a way to have
multiple implementations of a function, each using different
architecture-specialized instruction-set extensions. GCC 6 introduces
changes to FMV to make it even easier to bring architecture-based
optimizations to the application code.


Install and configure a |CL| host on bare metal
***********************************************

First, follow our guide to :ref:`bare-metal-install-desktop`. Once the bare
metal installation and initial configuration are complete, add the
:command:`desktop-dev` bundle to the system. :command:`desktop-dev` contains
the necessary development tools like GCC and Perl\*.

#.  To install the bundles, run the following command in the :file:`$HOME`
    directory:

  .. code-block:: bash

     sudo swupd bundle-add desktop-dev

Detect loop vectorization candidates
************************************

Now, we need to detect the loop vectorization candidates to be cloned for
multiple platforms with FMV. As an example, we will use the following
simple C code:

.. code-block:: c
   :linenos:

    #include <stdio.h>
    #include <stdlib.h>
    #include <sys/time.h>
    #define MAX 1000000

    int a[256], b[256], c[256];

    void foo(){
        int i,x;
        for (x=0; x<MAX; x++){
            for (i=0; i<256; i++){
                a[i] = b[i] + c[i];
            }
        }
    }


    int main(){
        foo();
        return 0;
    }

Save the example code as :file:`example.c` in the current directory and
build with the following flags:

.. code-block:: bash

    gcc -O3  -fopt-info-vec  example.c -o example

The build generates the following output:

.. code-block:: console

    example.c:11:9: note: loop vectorized
    example.c:11:9: note: loop vectorized

The output shows that line 11 is a good candidate for vectorization:

.. code-block:: c

    for (i=0; i<256; i++){
        a[i] = b[i] + c[i];

Generate the FMV patch
**********************

#.  To generate the FMV patch with the `make-fmv-patch`_ project, we
    must clone the project and generate a log file with the loop vectorized
    information:

    .. code-block:: bash

            git clone https://github.com/clearlinux/make-fmv-patch.git
            gcc -O3  -fopt-info-vec  example.c -o example &> log

#.  To generate the patch files, execute:

    .. code-block:: bash

            perl ./make-fmv-patch/make-fmv-patch.pl log .

#.  The :file:`make-fmv-patch.pl` script takes two arguments: `<buildlog>`
    and `<sourcecode>`. Replace `<buildlog>` and `<sourcecode>` with the
    proper values and execute:

    .. code-block:: bash

            perl make-fmv-patch.pl <buildlog> <sourcecode>

    The command generates the following :file:`example.c.patch` patch:

    .. code-block:: console

        --- ./example.c 2017-09-27 16:05:42.279505430 +0000
        +++ ./example.c~    2017-09-27 16:19:11.691544026 +0000
        @@ -5,6 +5,7 @@

         int a[256], b[256], c[256];

        +__attribute__((target_clones("avx2","arch=atom","default")))
         void foo(){
             int i,x;
             for (x=0; x<MAX; x++){

    We recommend you use the :file:`make-fmv-patch` script to add the attribute
    generating the target clones on the function `foo`. Thus, we can have the
    following code:

    .. code-block:: c

        #include <stdio.h>
        #include <stdlib.h>
        #include <sys/time.h>
        #define MAX 1000000

        int a[256], b[256], c[256];

        __attribute__((target_clones("avx2","arch=atom","default")))
        void foo(){
            int i,x;
            for (x=0; x<MAX; x++){
                for (i=0; i<256; i++){
                    a[i] = b[i] + c[i];
                }
            }
        }


        int main(){
            foo();
            return 0;
        }

#.  Changing the value of the `$avx2` variable, we can change the target
    clones when adding the patches or in the :file:`make-fmv-patch.pl` script:

    .. code-block:: perl

        my $avx2 = '__attribute__((target_clones("avx2","arch=atom","default")))'."\n";

#.  Compile the code again with FMV and add the option to analyze the
    `objdump` log:

    .. code-block:: bash

        gcc -O3 example.c -o example -g
        objdump -S example | less

    You can see the multiple clones of the `foo` function:

    .. code-block:: console

        foo
        foo.avx2.0
        foo.arch_atom.1

#.  The cloned functions use AVX2 registers and vectorized instructions. To
    verify, enter the following commands:

    ::

        vpaddd (%r8,%rax,1),%ymm0,%ymm0
        vmovdqu %ymm0,(%rcx,%rax,1)

FFT project example using FFTW
******************************

To follow the same approach with a package like FFTW, use the
`-fopt-info-vec` flag to get a build log file similar to:

.. code-block:: bash

    ~/make-fmv-patch/make-fmv-patch.pl results/build.log fftw-3.3.6-pl2/

    patching fftw-3.3.6-pl2/libbench2/verify-lib.c @ lines (36 114 151 162 173 195 215 284)
    patching fftw-3.3.6-pl2/tools/fftw-wisdom.c @ lines (150)
    patching fftw-3.3.6-pl2/libbench2/speed.c @ lines (26)
    patching fftw-3.3.6-pl2/tests/bench.c @ lines (27)
    patching fftw-3.3.6-pl2/libbench2/util.c @ lines (181)
    patching fftw-3.3.6-pl2/libbench2/problem.c @ lines (229)
    patching fftw-3.3.6-pl2/tests/fftw-bench.c @ lines (101 147 162 249)
    patching fftw-3.3.6-pl2/libbench2/mp.c @ lines (79 190 215)
    patching fftw-3.3.6-pl2/libbench2/caset.c @ lines (5)
    patching fftw-3.3.6-pl2/libbench2/verify-r2r.c @ lines (44 187 197 207 316 333 723)

For example, the :file:`fftw-3.3.6-pl2/tools/fftw-wisdom.c.patch` file
generates the following patches:

.. code-block:: diff
   :linenos:

       --- fftw-3.3.6-pl2/libbench2/verify-lib.c   2017-01-27 21:08:13.000000000 +0000
       +++ fftw-3.3.6-pl2/libbench2/verify-lib.c~  2017-09-27 17:49:21.913802006 +0000
       @@ -33,6 +33,7 @@

        double dmax(double x, double y) { return (x > y) ? x : y; }

       +__attribute__((target_clones("avx2","arch=atom","default")))
        static double aerror(C *a, C *b, int n)
        {
            if (n > 0) {
       @@ -111,6 +112,7 @@
       }

       /* make array hermitian */
       +__attribute__((target_clones("avx2","arch=atom","default")))
       void mkhermitian(C *A, int rank, const bench_iodim *dim, int stride)
       {
            if (rank == 0)
       @@ -148,6 +150,7 @@
       }

       /* C = A + B */
       +__attribute__((target_clones("avx2","arch=atom","default")))
       void aadd(C *c, C *a, C *b, int n)
       {
            int i;
       @@ -159,6 +162,7 @@
       }

       /* C = A - B */
       +__attribute__((target_clones("avx2","arch=atom","default")))
       void asub(C *c, C *a, C *b, int n)
       {
            int i;
       @@ -170,6 +174,7 @@
       }

       /* B = rotate left A (complex) */
       +__attribute__((target_clones("avx2","arch=atom","default")))
       void arol(C *b, C *a, int n, int nb, int na)
       {
            int i, ib, ia;
       @@ -192,6 +197,7 @@
            }
       }

With these patches, we can select where to apply the FMV technology, which
makes it even easier to bring architecture-based optimizations to
application code.

**Congratulations!**

You have successfully installed an FMV development environment on |CL|.
Furthermore, you used cutting edge compiler technology to improve the
performance of your application based on Intel® architecture and
profiling of the specific execution of your application.

*Intel and the Intel logo are trademarks of Intel Corporation or its subsidiaries.*

.. _GCC:  https://gcc.gnu.org
.. _make-fmv-patch: https://github.com/clearlinux/make-fmv-patch

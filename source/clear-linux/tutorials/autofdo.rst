.. _autofdo:

Automatic Feedback-Directed Optimizer
#####################################

This brief tutorial examines a simple `hello world` case and introduces you
to some basic optimizations and the new AutoFDO feature of GCC version 5.0 or
later.

We assume you have followed all the steps in our :ref:`bare-metal-install`
guide and are running a fully functional and configured instance of the Clear
Linux OS for Intel® Architecture.

Let's start with a simple sorting algorithm as an example:

.. code-block:: c

   #include <stdio.h>
   #include <stdlib.h>
   #include <sys/time.h>

   #define ARRAY_LEN 30000static struct timeval tm1;

   static inline void start() {

       gettimeofday(&tm1, NULL);

   }

   static inline void stop() {

       struct timeval tm2;

       gettimeofday(&tm2, NULL);

       unsigned long long t = 1000 * (tm2.tv_sec - tm1.tv_sec) +\

                              (tm2.tv_usec - tm1.tv_usec) / 1000;

       printf("%llu ms\n", t);

   }

   void bubble_sort (int *a, int n) {

       int i, t, s = 1;

       while (s) {

           s = 0;

           for (i = 1; i < n; i++) {

               if (a[i] < a[i - 1]) {

                   t = a[i];

                   a[i] = a[i - 1];

                   a[i - 1] = t;

                   s = 1;

               }

           }

       }

   }

   void sort_array() {

       printf("Bubble sorting array of %d elements\n", ARRAY_LEN);

       int data[ARRAY_LEN], i;

       for(i=0; i<ARRAY_LEN; ++i){

           data[i] = rand();

       }

       bubble_sort(data, ARRAY_LEN);

   }

   int main(){

       start();

       sort_array();

       stop();

       return 0;

   }

After compiling and executing this simple code, we have a baseline for
incoming improvements to control optimizations. For example:

.. code-block:: console

   # gcc sort.c -o sort

   # ./sort

   Bubble sorting array of 30000 elements

   3720 ms

Basic Optimization Options
==========================

These options control various sorts of optimizations: `-O1`, `-O2`, and
`-O3`. The GCC Optimize-Options section provides an excellent explanation.
For our example, we will use the `-O3` option. `-O3` turns on all
optimizations specified by -O2 plus the following options:

* finline-functions
* funswitch-loops
* fpredictive-commoning
* fgcse-after-reload
* ftree-loop-vectorize
* ftree-loop-distribute-patterns
* ftree-slp-vectorize
* fvect-cost-model
* ftree-partial-pre
* fipa-cp-clone

We applying this flag to our example code and run it:

.. code-block:: console

   # gcc -O3 sort.c -o sort_optimized
   #./sort_optimized

   Bubble sorting array of 30000 elements

   1500 ms

We see the execution reduced by 59.6 percent. An impressive performance
increase for a single optimization flag. Now, let us take into consideration
that this optimization is based on only the static analysis of the code. The
execution time provides no input that can tell us how the code is behaving
for the user: which parts are never executed or which ones are more
worthwhile to optimize. What if we could have that feedback? Well we can; the
:abbr:`FDO (Feedback-Directed Optimization)` technology makes this magic
happen.

Feedback-Directed Optimization
==============================

Traditional :abbr:`FDO (Feedback-Directed Optimization)` in GCC uses static
instrumentation to collect edge and value profiles. GCC uses execution
profiles consisting of basic block and edge frequency counts to guide the
optimizations for things like instruction scheduling, basic block reordering,
function splitting, and register allocation. According to Ramasamy, Yuan,
Chen & Hundt, 2008, the current method of FDO in GCC involves the following
steps:

#. Build an instrumented version of the program for edge and value profiling,
   the instrumentation build.

#. Run the instrumented version with representative training data to collect
   the execution profile. These runs typically incur significant overhead due
   to the additional instrumentation code executed.

#. Build an optimized version of the program by using the collected execution
   profile to guide the optimizations, the FDO build.

The instrumentation and FDO builds are tightly coupled. GCC requires both
builds use the same in-line decisions and similar optimization flags to
ensure that the :abbr:`CFG (Control-Flow Graph)` instrumented in the
instrumentation build matches the CFG annotated with the profile data in the
FDO build.

Apply this method to our example:

#. Create an instrumented binary with -fprofile-generate:

   .. code-block:: console

      # gcc sort.c -o sort_instrumented -fprofile-generate

#. Run the binary in order to generate the profile data file with
   runtime information:

   .. code-block:: console

      # ./sort_instrumented

      Bubble sorting array of 30000 elements

      3622 ms

#. Re-build the source with the profile data as feedback:

   .. code-block:: console

      # gcc -O3 sort.c -o sort_fdo -fprofile-use=sort.gcda

      Bubble sorting array of 30000 elements

      1448 ms

We can see an additional improvement from `-O3` to FDO: 1500 ms -> 1448 ms or
3.46%. We performed 1500 experiments with much more complex code and they
show a gain of almost 9%.

This method shows good application performance gains but, in practice, it is
not commonly used due to the high runtime overhead of profile collection, the
tedious dual-compile usage model, and the difficulties of generating a
representative training data set.

Enter AutoFDO
=============

To overcome the limitations of the current FDO model, we proposed the use of
AutoFDO. The AutoFDO tool uses `perf`_ to collect sample profiles. A
standalone tool converts the :file:`perf.data` file into the `gcov` format.
See the `tool's source code`_ for details.

This new model skips the instrumentation step. Instead, it uses a sampling-
based profile to drive feedback directed optimizations. The fairly thorough
`GCC documentation`_ and the `original article`_ from the GCC Developers’
Summit “Feedback-Directed Optimizations in GCC with Estimated Edge Profiles
from Hardware Event Sampling” explain further.

From the functional standpoint, there are two phases to AutoFDO: Generate the
profile file and use the profile to optimize binary.

Generate the profile file
-------------------------

AutoFDO needs a :file:`perf.data` file to capture the `BR_INST_RETIRED:TAKEN`
event in the processor. This event varies for every architecture. Therefore,
we use `ocperf`, part of the PMU-tools Project, to wrap all the information
required for `perf` to generate the :file:`perf.data` file correctly for any
Intel architecture. You can use either the `ocperf` tool or just the `perf`
tool.

.. code-block:: console

   # ocperf.py record -b -e br_inst_retired.near_taken -- ./sort

   Bubble sorting array of 30000 elements

   3731 ms

   [ perf record: Woken up 7 times to write data ]

   [ perf record: Captured and wrote 1.580 MB perf.data (3902 samples) ]

After this, we use a standalone tool `create_gcov` to convert the
:file;`perf.data` file into the `gcov` format. The `create_gcov` tool is part
of the `autofdo` set of tools:

.. code-block:: console

   # create_gcov --binary=./sort --profile=perf.data --gcov=sort.gcov
     -gcov_version=1

Use the profile to optimize binary
----------------------------------

The following information is read from our profile gcov file,
:file:`sort.gcov`:

* Function names and file names.
* Source level profile: A mapping from the in-line stack to its sample
  counts.
* Module profile: A mapping from the module to the aux-modules.

To read the profile file, we need to rebuild the source:

.. code-block:: console

    # gcc -O3 -fauto-profile=sort.gcov sort.c -o sort_autofdo

With the source rebuilt, we can run the :file:`sort_autofdo` binary to test:

.. code-block:: console

   # ./sort_autofdo

   Bubble sorting array of 30000 elements

   1447 ms

As you can see, the results are similar to FDO, with the following
advantages:

* Profile collection can occur on production systems. The profiles are,
  therefore, readily available for FDO builds without any special
  instrumentation built and run.

* You can use the profile data collected during the testing and development
  phase to build the optimized binary. Though similar to the instrumentation-
  based FDO model, the profile collection overhead is much lower.

* If the execution of the instrumented code changes the behavior of time-
  critical code, such as operating system kernel code, then the traditional
  FDO model using instrumented runs to collect profile data is not suitable.

* The current instrumentation-based FDO model does not support obtaining
  execution counts for kernel code.

With this example, you have learned how AutoFDO can help you to easily
optimize your code and improve the performance of your applications using
Clear Linux.

.. _perf: https://perf.wiki.kernel.org/index.php/Main_Page

.. _tool's source code: https://github.com/google/autofdo

.. _GCC documentation: https://gcc.gnu.org/wiki/AutoFDO

.. _original article: http://research.google.com/pubs/pub36576.html
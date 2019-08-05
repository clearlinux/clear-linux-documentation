.. _machine-learning:

TensorFlow\* machine learning
#############################

This tutorial demonstrates the installation and execution of a TensorFlow\*
machine learning example on |CL-ATTR|. It uses a Jupyter\* Notebook and MNIST
data for handwriting recognition. 

The initial steps show how to set up a Jupyter kernel and run a Notebook
on a bare-metal |CL| system.

.. contents::
    :local:
    :depth: 1

Prerequisites
*************

This tutorial assumes you have installed |CL| on your host system. For
detailed instructions on installing |CL| on a bare metal system, follow the
:ref:`bare metal installation tutorial<bare-metal-install-desktop>`.

Before you install any new packages, update |CL| with the following command:

.. code-block:: bash

   sudo swupd update

After your system is updated, add the following bundles to your system:

* :command:`machine-learning-web-ui`: This bundle contains the Jupyter application.

* :command:`machine-learning-basic`: This bundle contains TensorFlow
  and other useful tools.

To install the bundles, run the following commands in your :file:`$HOME`
directory:

.. code-block:: bash

   sudo swupd bundle-add machine-learning-web-ui

   sudo swupd bundle-add machine-learning-basic

Set up a Jupyter Notebook
*************************

With all required packages and libraries installed, set up the file structure
for the Jupyter Notebook.

#. In the :file:`$HOME` directory, create a directory for the Jupyter
   Notebooks named :file:`Notebooks`.

   .. code-block:: bash

      mkdir Notebooks

#. Within :file:`Notebooks`, create a directory named :file:`Handwriting`.

   .. code-block:: bash

      mkdir Notebooks/Handwriting

#. Change to the new directory.

   .. code-block:: bash

      cd Notebooks/Handwriting

#. Copy the :file:`MNIST_example.ipynb` file into the :file:`Handwriting`
   directory.

   .. note::

      After installing the :command:`machine-learning basic` bundle, you can find the example code under
      :file:`/usr/share/doc/tensorflow/MNIST_example.ipynb`.


The example code downloads and decompresses the MNIST data directly into the
:file:`./mnist` directory. Alternatively, download the four files directly
from the Yann LeCun’s `MNIST Database website`_ and save them into a
:file:`mnist` directory within the :file:`Handwriting` directory.

The files needed are:

* `train-images-idx3-ubyte.gz`_: Training set images (9912422 bytes)

* `train-labels-idx1-ubyte.gz`_: Training set labels (28881 bytes)

* `t10k-images-idx3-ubyte.gz`_: Test set images (1648877 bytes)

* `t10k-labels-idx1-ubyte.gz`_: Test set labels (4542 bytes)

Run the Jupyter machine learning example code
*********************************************

With |CL|, Jupyter, and TensorFlow installed and configured, you can
run the example code.

#. Go to the :file:`($HOME)/Notebooks` directory and start Jupyter with the
   following commands:

   .. code-block:: bash

      cd ~/Notebooks

      jupyter notebook

   The Jupyter server starts and opens a web browser showing the Jupyter file
   manager with a list of files in the current directory, as shown in
   Figure 1.

   .. figure:: /_figures/tensorflow/machine-learning-1.png
      :alt: Jupyter file manager

      Figure 1: The Jupyter file manager shows the list of available files.

#. Click on the :file:`Handwriting` directory. The :file:`MNIST_example.ipynb`
   file created earlier should be listed there, as shown in Figure 2.

   .. figure:: /_figures/tensorflow/machine-learning-2.png
      :alt: Example file within the Jupyter file manager

      Figure 2: The example file within the Jupyter file manager.

#. To run the handwriting example, click on the :file:`MNIST_example.ipynb`
   file to load the notebook, as shown in Figure 3.

   .. figure:: /_figures/tensorflow/machine-learning-3.png
      :alt: The loaded MNIST_example notebook

      Figure 3: The loaded MNIST_example notebook within the Jupyter file
      manager.

#. Click the |run-cell| button to execute the code in the current cell and
   move to the next.

#. Select the :guilabel:`In [2]` cell and click the |run-cell| button to load
   the MNIST data. The successful output is shown on Figure 4.

   .. figure:: /_figures/tensorflow/machine-learning-4.png
      :alt: Successful import of MNIST data

      Figure 4: Output after successfully importing the MNIST data.


   After the MNIST data is successfully downloaded and extracted into the
   :file:`mnist` directory within the :file:`($HOME)/Notebooks/Handwriting`
   directory, four .gz files are present and the four data sets are created:
   `trainX`, `trainY`, `testX` and `testY`.

#. To inspect the imported data, the function in :guilabel:`In [3]` first
   instructs Jupyter to reshape the data into an array of 28 x 28 images and to
   plot the area in a 28 x 28 grid. Click the |run-cell| button twice to show
   the first two digits in the `trainX` dataset. An example is shown in
   Figure 5.

   .. figure:: /_figures/tensorflow/machine-learning-5.png
      :alt: Function to reshape data.

      Figure 5: A function reshapes the data and displays the first two
      digits in the `trainX` dataset.

#. The :guilabel:`In [4]` cell defines the neural network. It provides the
   inputs, defines the hidden layers, runs the training model, and sets up
   the output layer, as shown in Figure 6. Click the |run-cell| button four
   times to perform these operations.

   .. figure:: /_figures/tensorflow/machine-learning-6.png
      :alt: Defining, building and training the neural network model

      Figure 6: Defining, building, and training the neural network model.

#. To test the accuracy of the prediction that the system makes, select the
   :guilabel:`In [8]` cell and click the |run-cell| button. In this example,
   the number 6 was predicted with a 99% accuracy, as shown in Figure 7.

   .. figure:: /_figures/tensorflow/machine-learning-7.png
      :alt: Prediction example

      Figure 7: The system predicts a number providing the accuracy of the
      prediction.

   .. note::

      To retest the accuracy of a random data point's prediction, run the
      cell :guilabel:`In [8]` again. It will take another random data point
      and predict its value.

#. To check the accuracy for the whole dataset, select the :guilabel:`In [10]`
   cell and click the |run-cell| button. Our example's accuracy is
   calculated as 97.17%, as shown in Figure 8.

   .. figure:: /_figures/tensorflow/machine-learning-8.png
      :alt: System's accuracy

      Figure 8: The system's accuracy for the entire data set.

For more in-depth information on the model used and the mathematics it entails,
visit the TensorFlow tutorials
`TensorFlow MNIST beginners demo`_ and `TensorFlow MNIST pros demo`_.

**Congratulations!**

You have successfully installed a Jupyter kernel on |CL|. In addition, you
trained a neural network to successfully predict the values contained in a
data set of hand-written number images.

Related topics
**************

* `MNIST Database website`_
* `TensorFlow MNIST beginners demo`_
* `TensorFlow MNIST pros demo`_
* `Jupyter main website`_
* `Jupyter documentation`_
* `MNIST at Wikipedia`_

.. _MNIST Database website:
   http://yann.lecun.com/exdb/mnist/

.. _train-images-idx3-ubyte.gz:
   http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz

.. _train-labels-idx1-ubyte.gz:
   http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz

.. _t10k-images-idx3-ubyte.gz:
   http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz

.. _t10k-labels-idx1-ubyte.gz:
   http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz

.. _Jupyter main website: http://jupyter.org/

.. _Jupyter documentation:  https://jupyter.readthedocs.io/en/latest/index.html

.. _TensorFlow MNIST beginners demo:
   https://www.tensorflow.org/get_started/mnist/beginners

.. _TensorFlow MNIST pros demo:
   https://www.tensorflow.org/get_started/mnist/pros

.. _MNIST at Wikipedia:
   https://en.wikipedia.org/wiki/MNIST_database

.. |run-cell| image::  /_figures/tensorflow/run-cell-button.png

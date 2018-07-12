.. _contents: 


Contents directive
##################

For |CL| documentation that has three or more sections, use the `contents::`
directive as shown in the example below. This directive automatically captures the headings (and 
subheadings if used) as specified in the value given after `:depth:`. Adding this directive to 
longer documents allows users to quickly navigate to the desired section.

.. contents:: :local: 
   :depth: 2

.. code-block:: bash

   .. contents:: :local: 
   	  :depth: 2

.. note:: 
   
   Assure that you add `:local:` as the value. For more resources on this directive, 
   visit the `reStruturedText Directives`_ 

EXAMPLE: 

Clear Linux Guide Example  
*************************

Introduction
=========

Step-by-Step
============

Launch
======


.. _reStruturedText Directives: http://docutils.sourceforge.net/0.4/docs/ref/rst/directives.html#table-of-contents

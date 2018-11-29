.. _mixer-about:

Mixer
#####

|CL-ATTR| is a powerful, modular, and customizable OS. Upstream |CL| offers
many images for different deployment environments and use-cases.  There are
hundreds of bundles that will meet most, if not all, of your OS and software
needs.

However, if you need additional customization or content, |CL| provides the
mixer tool to customize the OS. With mixer, there are two approaches to
customization:

* :ref:`create-mix`
* :ref:`create-mixin`

Which approach you choose will depend on the level of customization that you
need.

.. _create-mix:

Create a mix
============

The first approach is to use the mixer tool to create a derivative of the |CL|
that contains your custom software. This is known as creating a mix. In your
mix, you can

* Use any existing upstream bundles with no modification.
* Redefine what goes into existing bundles.
* Create completely new, custom bundles with your own custom packages.

With mixer you are not required to incorporate every upstream release into your
mix. You decide which upstream versions to update your derivative to, as
illustrated in Figure 1.

.. figure:: figures/mixer-about-1.png
   :scale: 75%
   :alt: Creating a custom mix.

   Figure 1: With a custom mix, you add your custom bundle and decide which
   upstream versions to update your mix to, on your own release cycle.

Creating your own mix forks away from the |CL| upstream and requires that you
act as your own OSV. There is a greater level of responsibility, requiring
more infrastructure and processes to adopt. However, with this approach, you
have a higher degree of control and customization of your custom |CL|.


.. _create-mixin:

Create a mixin
==============

The second approach is to use the mixin tool, a light wrapper for mixer, to
create custom bundles and sideload them into your upstream version of |CL|.
This is known as a mixin. A mixin is useful when you need to add custom or 3rd
party content but want to keep on the upstream update cycle, as shown in
Figure 2. You can also create new bundles using upstream packages.

.. figure:: figures/mixer-about-2.png
   :scale: 75%
   :alt: Creating a custom mix.

   Figure 2: With a mixin you can add custom bundles, but stay on upstream.

Mixin is primarily intended for end users. It is easier to adopt as it does
not require breaking from upstream or acting as an OSV. With mixin

* You are responsible for maintaining and testing your custom bundle(s).
* You retain access to all upstream bundles and updates.
* You can easily revert your system back to the upstream version.

Related topics
==============

|CL| provides flexibility in how you customize your OS. Learn more about mixer
and related topics to decide which customization approach is best for you.

* :ref:`mixer`
* :ref:`mixin`
* :ref:`bundles-about`
* :ref:`swupd-about`
* :ref:`deploy-at-scale`

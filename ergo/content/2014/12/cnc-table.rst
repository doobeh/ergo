:title: CNC Chair
:date: 2014-12-03 20:51
:modified: 2014-12-08 20:12
:tags: cnc
:category: cnc
:slug: first-cnc-chair
:authors: Anthony Plunkett
:summary: Planning and building a chair on my CNC machine.
:status: published

One of my major projects over the last couple of years is to very slowly
fabricate and build a decent sized CNC machine.  It's functionally complete
now, still needing some finishing touches to help with cable-management and
automatic homing, but it can now cut an area of about 54" by 51"

On the top of my to-do project list for the CNC to cut is a chair built from
plywood-- essentially imagine a standard chair, then sliced into 0.75"
parts.  You end up with two shapes, one that classically looks like the
outline of a chair, the other like the seat and back of the chair.

The Sketch
----------

The first step is to layout the parts you wish to create, here's the chair
I'm looking to build:

..  image:: /images/cnc/chair_outline.gif
    :alt: Chair Outlines

The full chair outline will get cut four times out of 0.75" ply, so 3" and
the other shape, the seat and back, will be cut twenty times, giving the chair
a final width of 18".  The points along the middle of the outlines indicate
where I'll get the machine to drill a hole, which will allow me to
align the parts easily once cut by passing a 1/4" dowel through the holes.

The Layout
----------

The next step is to lay out the parts in an efficient way to reduce wastage
of wood-- luckily that's a fairly routine procedure which most CAD tools
include. Here's an example sheet:

..  image:: /images/cnc/sheet_layout.gif
    :alt: Sheet Layout

I've chosen to be a bit cautious in the layout, leaving 1" of gap between each
part and the edge of the wood.  As I get more confident and understand the
strength of the material I'll slowly decrease that, which will allow more
efficient layouts.

The Tool Paths
--------------

Next is to generate the toolpaths that the machine will cut— essentially building
a text file that tells the machine what coordinates to move to, and how deep to cut.
The end code looks like::

    M6 T1
    M03 S12223
    G00 Z0.8750
    X1.8441 Y13.7990
    G01 Z0.5500  F30.0
    X1.8425 Y13.8158 Z0.5470  F10.0
    X1.8413 Y13.8380 Z0.5431
    X1.8411 Y13.8602 Z0.5392
    X1.8417 Y13.8824 Z0.5353
    X1.8432 Y13.9045 Z0.5314
    X1.8456 Y13.9265 Z0.5275
    X1.8489 Y13.9485 Z0.5235
    X1.8530 Y13.9703 Z0.5196
    X1.8581 Y13.9919 Z0.5157

You can get a feel for what the code is telling the machine, in this instance it's
telling the machine to ramp down into the first cut.

But rather then trying to decode that with our minds, we can get the simulator to
show us the output.

..  image:: /images/cnc/chair-simulation.gif
    :alt: Simulation

Cutting and Building
--------------------

The next stage is committing that design to wood— I loaded the plywood into the machine,
loaded the G-code and set my origin point (the 'bottom-left' of the plywood) and zeroed
the machine to the table-top of the CNC bed.  A lot of people use the top of the material
as the Z depth zero, but while I'm learning, it reduces less chance of plunging into the
bed material and means I don't have to adjust the G-code to take into account the actual
depth of the plywood— wood is rarely the size it's sold at.

..  image:: https://farm8.staticflickr.com/7468/15350672144_dfe779b45d_z.jpg
    :width: 240px
    :height: 320px
    :alt: Dowel joined chair

..  image:: https://farm9.staticflickr.com/8637/15970961231_f409404e34_z.jpg
    :width: 240px
    :height: 320px
    :alt: Clamped

A couple of mistakes were had— I don't have a good cable management system installed yet,
and while it was finishing the cuts and getting ready to do the dowel holes, the machine
caught up on one of the motor cables, which caused it to judder— I think that threw off
the machine a little and the dowel holes ended up being offset a little.  When I clamp it,
it looks a lot better, because the error occurred after most the outlines were cut.

Next time I'll be sure to fix the cabling management and use a more accurate dimension of
3/4" plywood— this one actually measured 0.56" which ends up making the chair less stable
and overall have a smaller finished width.

But, as a start— it's a good one.  Looking forward to changing the chair design slightly
to improve it's strength characteristics and maybe increase the side of the back of the
chair a little.


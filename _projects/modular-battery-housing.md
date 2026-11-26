---
title: Modular 18650 Battery Housing
summary: A 3D printed modular case used to store and protect recycled lithium batteries.
tags: [CAD, Electronics]
---

## Problem

I collect and recycle 18650 batteries from used disposable e-cigarettes. A common issue with storing lithium batteries is handling them safely to prevent short circuits or punctures.

## Plan

The goal of this project was to design a 3D printable battery holding cell that is lightweight and modular. I liked the idea of a design that used interlocking rails so you can attach as many as you'd like and store them together.

## Process

Designing with Fusion 360, I first started with a simple cylinder with four connection points. This required printing male and female cells, and alternating them to create a grid. It was a good proof of concept, but the rails could only slide in from one side and there was lots of wasted space. The focus with this first prototype was perfecting the rail tolerances for convenient joining, and tuning the inner cell diameters so that the batteries could be pushed in without easily falling out. 

![Photo of the power connector]({{ "/assets/img/battery cells/cells.jpg" | relative_url }}){: .img-medium .img-center}

![Photo of the power connector]({{ "/assets/img/battery cells/hexcells.jpg" | relative_url }}){: .img-medium .img-right}

I realized a hexagonal arrangement would save space, so I started over again. After another 20 iterations or so, I arrived at this design, guided by the following requirements:

- Batteries are securely held and don't slip out
- Rails allow entry and removal from either side
- Cell walls alternate male/female connections, so only one design needs to be printed
- Rails click into place when slid in, and once seated, the rail doesn't detach easily
- Rails snap fit into male/female cutouts instead of relying on friction and pressure 
- Wall have cutouts to save printing material

The rails allow for entry/removal from either side, and the cell alternates male/female connections so only one design needs to be printed. There is a satisfying click into place when the rail slides in, and it doesn't easily detach.

The design was mostly finalized but took several more prints to get the tolerances just right. Once it felt perfect, I printed them in bulk to store all my cells together.

<div style="clear: both;"></div>

## Results

In retrospect, the design is overengineered, and seeing it through to the end taught me how to better spot a flawed idea before sinking too much time into it. Here are some of the many flaws I pinpointed that could have been avoided:

- I think it would be more convenient to forgo the interlocking modular design for simple cylinders that can be stored in a 3D printed frame. As the amount of cells attached to the group increases, it becomes more difficult to slide them on and off, and the PLA rails are susceptible to breaking off as weight grows.
- PLA is a poor choice of material for a part that undergoes friction and pressure. The rails wear down within a dozen uses or so, changing the tolerances and causing the cells to slip more easily.
- In the future, I will be more likely to consider alternatives for a PLA design that requires highly specific tolerances, or sliding rails.

Ultimately the project gave me lots of experience working with Fusion, and I feel particularly more comfortable with designing interlocking parts and understanding tolerances for rails, though I would stray from using them if there might be a more convenient alternative. I think learning through failure in this kind of way is great as it allows you to articulate the issues with a certain design instead of blindly following advice without the experience to understand why.
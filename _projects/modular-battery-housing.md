---
title: Modular 18650 Battery Housing
summary: 
tags: [CAD, Electronics]
---

## Problem

I collect and recycle 18650 batteries from used disposable e-cigarettes. A common issue with storing lithium batteries is handling them safely to prevent short circuits or punctures.

## Plan

The goal of this project was to design a 3D printable battery holding cell that is lightweight and modular. I liked the idea of a design that used interlocking rails so you can attach as many as you'd like and store them together.

## Process

Designing with Fusion 360, I first started with a simple cylinder with four connection points. This required printing male and female cells, and alternating them to create a grid. It was a good proof of concept, but the rails could only slide in from one side and there was lots of wasted space.

![Photo of the power connector]({{ "/assets/img/battery cells/cells.jpg" | relative_url }}){: .img-medium .img-center}

![Photo of the power connector]({{ "/assets/img/battery cells/hexcells.jpg" | relative_url }}){: .img-medium .img-right}

I realized a hexagonal arrangement would save space, so I started over again. After another 20 iterations or so, I arrived at this design.

- Batteries are securely held and don't slip out
- Rails allow entry and removal from either side
- Cell walls alternate male/female connections, so only one design needs to be printed
- Rails click into place when slid in, and once seated, the rail doesn't detach easily
- Wall cutouts save some printing material

The rails allow for entry/removal from either side, and the cell alternates male/female connections so only one design needs to be printed. There is a somewhat satisfying click into place when the rail slides in, and it doesn't easily detach.

The design was mostly finalized but took several more prints to get the tolerances just right. Once it felt perfect, I printed them in bulk to store all my cells together.

<div style="clear: both;"></div>

## Results

In retrospect, the design is overengineered. I think it would be more convenient to forgo the interlocking modular design for simple cylinders that can be stored in a 3D printed frame. As the amount of cells attached to the group increases, it becomes more difficult to slide them on and off, and the PLA rails are susceptible to breaking off and wearing down. Ultimately the project gave me lots of experience working with Fusion, and I feel particularly more comfortable with designing interlocking parts and understanding tolerances for rails.
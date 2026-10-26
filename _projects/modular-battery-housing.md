---
title: Modular 18650 Battery Housing
summary: 
tags: [C++, STM32, KiCad, FOC]
repo: https://github.com/yourusername/motor-driver
---
<div class="todo" markdown="1">
**Placeholder project.** Replace every section with your real project, or delete this file and duplicate it for a different one.
</div>

![Photo of the assembled board]({{ "/assets/img/motor-driver.jpg" | relative_url }})

## Problem description

I collect and recycle 18650 batteries from used disposable e-cigarettes. A common issue with storing lithium batteries is handling them safely to prevent short circuits or punctures.

The goal of this project was to design a 3D printable battery holding cell that is lightweight and modular. I liked the idea of a design that used interlocking rails so you can attach as many as you'd like and store them together.

I first started with a simple cylinder with four connection points. This design required printing male and female cells, and alternating them to create a grid. It was a good proof of concept, but the rails could only slide in from one side and there was lots of wasted space. I realized a hexagonal arrangement would save space so I started over again.

After another 20 iterations or so, I arrived at this hexagonal design. The rails allow for entry/removal from either side, and the cell alternates male/female connections so only one cell needs to be printed.

The design was mostly finalized but took several more prints to get the tolerances just right. Once it felt perfect, I printed them in bulk to store all my cells together.

## Results

In retrospect, the design seems overengineered. I think it would be more convenient to forego the interlocking modular design for a simple cylinder that can be stored in a 3D printed frame. As the amount of cells attached to the group increases, it becomes more difficult to slide them on and off, and the PLA rails are susceptible to breaking off and wearing down. Ultimately the project gave me lots of experience working with Fusion, and I feel particularly more comfortable with designing interlocking parts and understanding tolerances for rails.


## What I'd do differently

One or two honest lines.

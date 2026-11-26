---
title: Cloud Chamber
summary: Glass cloud chamber for viewing particle trails, built with nichrome wire and a frozen gel pad.
tags: [Electronics, Physics]
---

## Introduction

While reading volume 6 of Harvard's science intro series Project Physics, I was surprised to learn that rudimentary subatomic particle detectors are not hard to understand or build. After doing some more research, I found that a cloud chamber would be possible to build using resources I had at home.

## Process

Subatomic ionizing particles can be viewed using a cloud chamber, or a clear box containing a vapour layer of supersaturated isopropanol gas. The layer is formed by trapping alcohol vapour in a temperature gradient such that it floats in a layer without condensing in the chamber. Then, when a charged particle passes through the vapour, it creates sublimation points for the alcohol to bind to, and a trail of bubbles appears along the path of the particle.

![Photo of nichrome wire]({{ "/assets/img/cloud chamber/wire.jpg" | relative_url }}){: .img-small .img-right}

I began by looking at online resources and decided to start with [a design by PhysicsHigh on YouTube](https://youtu.be/gt3Ad5_Z5IA). This chamber creates a heat gradient by sandwiching the vapour between a frozen gel pad on the bottom and heat from boiling water on top. The choice is appealing because it doesn't use dry ice for cooling, so it's easily reusable.

I modified the design by replacing the boiling water on top with a nichrome wire heating element that runs along a metal plate. The wire is electrically insulated by Kapton tape, but it's not thermally insulated so the heat effectively spreads to the aluminum plate. A felt pad glued to the metal plate gets soaked in alcohol, and it subsequently releases vapour when heated.

In terms of wire specifications, I coiled about a foot of 26 gauge nichrome and passed 5 to 7 volts through it. This got it quite hot for evaporating the alcohol. Of course, it's important to be careful with this as the wire can get red-hot and ignite the vapour if you accidentally use a higher voltage or cause a short anywhere.

To run the wires for the heating element, I drilled a small hole in the glass container at the top. Since the alcohol vapour sinks, it doesn't leak much at all and there's no need to worry about sealing it. On the bottom however, it's important to ensure a perfect seal. During testing, I had many failures and realised that there were tiny gaps where the glass container didn't touch the plate, which proved to leak a substantial amount of the vapour. A rubber o-ring would solve this issue effectively, but I didn't have any on hand so I sealed it with petroleum jelly, as suggested by the above PhysicsHigh video.

I learned that the trick with using a gel block is keeping it in the freezer for several hours and working quickly once it's taken out. At regular freezer temperatures (far above dry ice), the block is only usable for about 10 minutes. Beyond that time, the alcohol will sublimate instead of supersaturating. I considered building an insulating housing out of styrofoam or plastic to help reduce heat loss from the surrounding air or conduction with the table.

<div style="clear: both;"></div>

## Results

After a few attempts, I was able to spot particle trails inside the chamber. My radioactive source is Americium-241 from an old smoke detector, which is a weak alpha particle emitter (exposure to it is safe as long as it's not ingested).

![Photo of the cloud chamber]({{ "/assets/img/cloud chamber/chamber.jpg" | relative_url }}){: .img-medium .img-center}

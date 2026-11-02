---
title: Cloud Chamber
summary: Glass cloud chamber for viewing particle trails, built with nichrome wire and a frozen gel pad.
tags: [Electronics, Physics]
---

## Introduction

While reading volume 6 of the Harvard Project Physics handbook series, I was surprised to learn that rudimentary subatomic particle detectors are not hard to understand or build. After doing some more research, I decided that a cloud chamber would be possible to build using resources I had at home.

## Process

Subatomic ionizing particles can be viewed using a cloud chamber, or a transparent box containing a vapour layer of supersaturated isopropanol. The layer is formed by trapping alcohol vapour in a temperature gradient such that it floats in a layer without condensing in the chamber. When a charged particle passes through the vapour, it creates sublimation points for the alcohol to bind to, and a trail of bubbles is made visible along the path of the particle.

![Photo of the cloud chamber]({{ "/assets/img/cloud chamber/wire.jpg" | relative_url }}){: .img-small .img-right}

I began by looking at online resources and decided to start with [a design by PhysicsHigh on YouTube](https://youtu.be/gt3Ad5_Z5IA). This chamber creates a heat gradient by sandwiching the vapour between a frozen gel pad on the bottom and heat from boiling water on top. The choice is appealing because it doesn't use dry ice for cooling, so it's easily reusable.

I modified it by replacing the boiling water on top with nichrome wire that runs along a metal plate (electrically insulated by Kapton tape). The heat from the wire very effectively warms up the plate and the alcohol-soaked cloth pad glued to it.

<div style="clear: both;"></div>


## Results

After some experimenting, I was able to spot particle trails inside the chamber. My radioactive source is Americium-241 from an old smoke detector, which weakly emits alpha particles (exposure to it is safe as long as it's not ingested).

I learned that the trick with using a gel block is keeping it in the freezer for several hours and working quickly once it's taken out. At regular freezer temperatures (far above dry ice), the block is only usable for about 10 minutes. Beyond that, the alcohol will sublimate instead of supersaturating. It's also important to ensure a perfect seal on the bottom by rubbing petroleum jelly on the seam. If there's even a tiny crack, the cold air and alcohol vapour will leak out.

For the nichrome wire, I coiled about a foot of 26 gauge nichrome and passed 5 to 7 volts through it. This got it quite hot for evaporating the alcohol. Of course, it's important to be careful with this as the wire can get red-hot and ignite the vapour if you accidentally use a higher voltage. 

![Photo of the cloud chamber]({{ "/assets/img/cloud chamber/chamber.jpg" | relative_url }}){: .img-medium .img-center}

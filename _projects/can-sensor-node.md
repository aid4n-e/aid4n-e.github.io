---
title: CAN Bus Sensor Node
summary: Small PCB that reads sensors and publishes them over CAN, with a from-scratch driver.
tags: [C, CAN, KiCad, Drivers]
repo: https://github.com/yourusername/can-sensor-node
---
<div class="todo" markdown="1">
**Placeholder project.** Replace with your real project.
</div>

![Photo of the board]({{ "/assets/img/can-node.jpg" | relative_url }})

## The problem

Why a CAN node, and what it connects to.

## Hardware

Transceiver, termination, ESD protection, connector choice, layout notes.

## Firmware

The driver you wrote from the datasheet, message format, error handling and bus-off recovery.

## Results

Logic analyzer or CAN analyzer captures, bus load, demo video.

## What went wrong

A real bug, such as missing termination, bit timing mismatch or a ground loop, and how you found it.

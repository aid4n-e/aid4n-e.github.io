---
title: Toyota Stereo Aux Injection
summary: AUX jack soldered directly to a 2003 Matrix console.
tags: [Mod, Audio]
---

## The problem

My old Toyota has no built-in audio jack, which would offer much better sound quality over the poor signal of my bluetooth radio adapter.

## The plan

Inject an AUX signal into the CD player line. Since the CD player must be running for the sound system to be active, I will parallel route the CD player signal through an attenuator, so it can be turned down separately while the AUX audio is playing. An added benefit of this solution is that it allows for crossfading, e.g. ambient CD audio while listening to a podcast.

## Process

![Photo of the power connector]({{ "/assets/img/power.jpg" | relative_url }}){: .img-small .img-right}

I removed the unit from my car and probed the wiring harness with a multimeter to find the 12V power input pin.

At the bench, I opened up the unit and powered it using 12V from my homemade ATX supply. 


<div style="clear: both;"></div>


I burned a signal test disk that contained sine wave tracks, left/right audio tracks, and frequency sweeps. Using the known reference audio, I scoped the lines coming from the CD head to find the audio input pins, as well as the power and control pins.

![Photo of the head unit]({{ "/assets/img/unit.jpg" | relative_url }}){: .img-medium .img-center}

<div style="clear: both;"></div>

![Photo of the optocoupler]({{ "/assets/img/optocoupler.jpg" | relative_url }}){: .img-small .img-right}

Since I wanted the comfort of adjusting both left and right volumes with one interface, but I had no stereo potentiometers available, I assembled an optocoupler with one LED facing two photoresistors enclosed in a 3D printed housing. Each resistor routes to ground, so when the LED is off, both signals get attenuated. 

<div style="clear: both;"></div>

Finally, I soldered an AUX jack to the L/R pins in parallel with the CD player lines. This was one of my first microsoldering jobs, so it wasn't very clean!


<div class="img-row" markdown="1">


![Soldered aux jack]({{ "/assets/img/aux.jpg" | relative_url }}){: .img-medium .img-left}

![Soldered aux jack]({{ "/assets/img/injection.jpg" | relative_url }}){: .img-medium .img-right}

</div>


## Results

The system functioned properly during testing when connected to my phone's audio jack. Audio quality was much better than using the radio. During testing I accidentally overvolted the CD player power line, which caused it to fail. Had I been fully successful, I intended to install it in my car with a fun slide potentiometer in the dashboard used to control the CD volume.
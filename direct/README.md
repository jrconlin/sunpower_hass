# Reading Sunpower data directly

Sunpower's web "API" has a few problems:
* It's undocumented
* It's unsupported
* It's laggy (by about an hour)
* It's inaccurate
* It's too simplistic
* Basically, it sucks.

I spent some time cracking the API in several varieties before some kind hearted soul pointed out an article
that noted there's an installer port availble inside of the control box. Said installer port delivers
HIGHLY detailed information, if you ask it to.

At this point, I was kind of wondering why the hell I was bothering with a crap web API?

Turns out, you can fit (just barely, but it works) a Raspberry Pi 3, a short network patch cable, and a
USB power plug into the Sunpower controller box fairly nicely. Depending how you've got your home
wifi rigged, you can probably get signal to it fairly easily and it will happily respond to polling.

This is the product of my happy experiment. I encourage you to do the same.

Whether or not you decide you no longer need to keep the sunpower control box on your wifi after you do
that is completely up to you.
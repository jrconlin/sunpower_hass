# Hacky HomeAssistant SunPower sensor module

## UPDATE
<span style="color:red">PLEASE NOTE</span>: Sunpower recently sent out an
email stating that they will be switching to an "app-based" system.
They would want you to download and install their mobile app, which would
then give you access to their website. Yeah, no.

Mobile apps give companies a LOT of your info, far more than if you just
used a browser to look at your site, and far more than I'd prefer to give
a company I bought solar panels from. Plus, I found that their site has
gotten progressivly worse and worse about letting me track my production
and status.

To that end, I've moved the old python script under [_legacy_](legacy),
and do not plan on updating it or try to figure out how to get what I need
out of their godforsaken site.

Instead I _*STRONGLY*_ urge you to use the [_direct_](direct) access
method of getting data out of the sunpower controller box.

You'll get far more info, more timely, and accurately than you will out of
trying to sniff their site, plus you won't have to give them any info.

In fact, you can probably just block the controller device from the
internet at that point, which is probably a good idea anyway.
# WebPageTest

This is a tool to run speed test in https://www.webpagetest.org/ from commandline.
All the tests will cover both chrome and iPhone6
For iPhone6, the speed is configured as `3G Fast`

# Command

Basic Command:

```
python wpt.py -e qa1 -l JSP -p vip -s ReactVIPABTest=OPTION2 -v https://www.cloud.qa1.gumtree.com.au/s-ad/sydney-city/baby-clothing/baby-clothing/1119869988
```

Options:

```
# -e, --env: which env you want to run test against to

# -l, --label: the label for the test. For example, if you are running a test for GTM, you can config the label as the GTM version

# -p, --page: default: home,srp,vip. the pages will be covered in the test, now it can be home,srp,vip. If you want to test multi pages, just sperate the pages with ',' like "home,srp"

# -s, --script: now only support adding AB testing settings. sample: -s ReactVIPABTest=OPTION2

# -v, --vip: default one is "/s-view-details.html?adId=0&ops=_4-cIqHCrYag". but ReactVIP only enabled in non-vertical & non-BS category. if you want to test React VIP, please specify which VIP you want to test

# -b, --block: which urls you want to block. Deafult one is "async-ads.js ads.js advertising prebid adsensecommon.js adnxs.com doubleclick.net pubmatic.com casalemedia.com adservice.google.com adservices.google.com.au demdex.net imrworldwide.com amazonaws.com criteo.com openx.net"

```

You can find your tests from https://www.webpagetest.org/testlog.php?days=1&filter=&all=on after executed the command.
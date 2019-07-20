# Testing mulitple versions of dateutil

In response to this question on the [Boston Python Slack](https://about.bostonpython.com/slack):

> Any idea why dateutil’s parser would parse “23APR2019” just fine on my Windows install of (Python) 3.6.8 but not in an install of (Python) 3.7.* on another OS?

Somebody suggested:

> Check that you really have the same version of dateutil in both places.

I thought it might be quick/fun to determine if the version of dateutil could be the problem by running a simple test in multiple versions of Python using [tox](https://tox.readthedocs.io/en/latest/). That turned out to be the case, so for more fun, I ran the same test in [nox](https://nox.thea.codes/en/stable/index.html).

TL;DR:

- The format isn't parsed in dateutil < 2.7
- Nox is cool

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

Compassion Sponsorships
=======================

Sponsorship management module. This module makes the link between child and
contracts. It also customize contracts to fit the child sponsorship context.

Installation
============
This modules requires en_US, fr_CH, de_DE, it_IT and es_ES to be installed
on the server.

To check installed locales:

* locale -a

To add a new locale :

* /usr/share/locales/install-language-pack <ISO-locale-name>
* dpkg-reconfigure locales

Configuration
=============
You can configure how to behave when projects are suspended. If you setup
nothing, sponsorship invoices for a period during a supsension of a projects
will be cancelled.

If you want to change sponsorship with a a fund donation, you can add
the following key-value in the System Parameters:
    - sponsorship_compassion.suspend_product_id : product_id
    
Usage
=====
To use this module, you need to:

* go to Sponsorship -> Sponsorships

Known issues / Roadmap
======================

* Contracts and Sponsorships will be better differenciated.

Credits
=======

Contributors
------------

* Cyril Sester <cyril.sester@outlook.com>
* Emanuel Cino <ecino@compassion.ch>

Maintainer
----------

This module is maintained by `Compassion Switzerland <https://www.compassion.ch>`.
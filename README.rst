django-markdownplus v. 0.1.0
############################

.. _description:

**django markdownplus** is tiny django application that allows to use extended markdown in the templates
Documentaton available at github_.

.. contents::

.. _requirements:

Requirements
============

- python >= 3.4
- django >= 1.8
- markdown
- bleach


.. _installation:

Installation
============

**Django markdown** should be installed using pip3: ::

    pip3 install django-markdownplus


Setup
=====

- Add 'markdownplus' to INSTALLED_APPS ::

    INSTALLED_APPS += ( 'markdownplus', )


Use django_markdownplus
=======================
#) Syntax: ::

    All basic markdown syntax
    and
    !a[alt](src title) # for <audio>
    !v[alt](src title) # for <video>

    Note that alt and title attributes are optional

#) Templates: ::

    {% load markdownplus %}
    <div>{{ some_markdown_text|markdownplus}}</div>

Bug tracker
===========

If you have any suggestions or bug reports
please report them to the issue tracker
at https://github.com/makerj/django_markdownplus


Contributing
============

Contribution of django-markdownplus available at github: https://github.com/makerj/django_markdownplus


License
=======

Licensed under a The MIT License (MIT).


Copyright
=========

Copyright (c) 2016 Junhui Lee (ohenwkgdj@gmail.com)

.. _github: https://github.com/makerj/django_markdownplus
====================================
CareerBuilder API Wrapper for Python
====================================

A client library for using the CareerBuilder API. See API docs at
http://api.careerbuilder.com/


Installation
------------

Install from PyPi using pip, a package manager for Python::

    $ pip install careerbuilder


API Credentials
---------------

The CareerBuilder API needs to be called with your CareerBuilder Developer Key.
You will need to `register with CareerBuilder
<http://developer.careerbuilder.com/keyrequests/new>`_ to obtain a developer
key. You must pass this to the `CareerBuilder` constructor.::

    import CareerBuilder

    cb = CareerBuilder('YOUR_DEVELOPER_KEY')


Examples
--------

::

    from careerbuilder import CareerBuilder


    DEV_KEY = 'YOURDEVELOPERKEY'

    cb = CareerBuilder(DEV_KEY)

    co_did = 'c07l31mk7xy94414r8'
    co = cb.company_details(co_did)
    print co

    search = cb.job_search(Keywords='python', Location='84101')
    print search

    job_id = 'JHL59Q6KGLDSCQS7QL2'
    job = cb.job(job_id, AnotherVar='test')
    print(job)

    app = cb.application(job_id)
    print app

    cats = cb.categories()
    print cats

    print(cb.recommendations(job_id))



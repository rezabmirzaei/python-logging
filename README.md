# Simple setup for Python logging

The simplest basic setup I can think of for logging in Python:

* Set basic logger configuration in ``main.py``. Default:
  * Will write to ``master.log``
  * Formats output to include timestamp, module and function name
  * Sets log level to ``INFO``
* Use the logger in separate classes to write to the same log file (``master.log``). See  ``subclasses.subclass.py``

Run the script as-is from the projects root directory. This will create the log-file ``master.log`` in the same directory, outputting formatted lines from ``main.py`` and  ``subclasses.subclass.py`` every 20 seconds.

=============================
Mantis TEMPLATE Importer
=============================


A TEMPLATE importer for the  Mantis Cyber Threat Intelligence Mgmt. Framework.

To base a new importer on this template do the following:

- Export the files, e.g. as follows::

  git archive --format tar --output <path> master

- Use a recursive search-replace to replace all occurrances of ``TEMPLATE_import`` with
  ``foo_import``, where ``foo`` is the name of the thing you want to write an importer for.

- Rename the directories containing ``TEMPLATE`` accordingly.

- On top-level in the directory (e.g. in the directory where the setup.py is),
  do 'pip install -e .' This makes module ``mantis_foo_importer`` available
  to the environment; the module is always based on the code inside the
  directory on which you did ``pip install -e .`` (although e.g. in the
  case of 'python manage.py shell', you need to restart for changes in the
  code to carry over into the runtime whereas 'python manage.py runserver'
  usually notices changes in the code base and restarts automatically).

- in the django settings, include ``mantis_foo_importer`` in the list of
  apps. You can check whether things work by doing::

       python manage.py mantis_foo_import <path_to_some_xml_file> --settings=<your_settings_module>

  This calls the command defined in 'mantis_foo_importer/management/commands/mantis_foo_import.py'
  (see <https://docs.djangoproject.com/en/dev/howto/custom-management-commands/> for the mechanism
  behind this.)

In order to learn more about MANTIS, please refer to the documentation at http://django-mantis.rtfd.org .



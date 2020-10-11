`django-admin startproject BRAND_NEW -n={project-root-dir-name} -n={additional_name_for_configs} --name=nginx,supervisor.conf,celery.conf,uwsgi.ini,README.md --template=https://github.com/TheJog5505/django-tamplate/archive/master.zip`

Rename "BRAND_NEW" dir to "{{ files.0 }}" with command\
`test -d {{project_directory|cut:project_name}}{{files.0}} && echo "Directory '{{project_directory|cut:project_name}}{{files.0}}' already exists!" || mv {{project_directory}}/ {{project_directory|cut:project_name}}{{files.0}}/`

project_path=`pwd`

test -d {{project_directory|cut:project_name}}{{files.0}} && echo "Directory '{{project_directory|cut:project_name}}{{files.0}}' already exists!" || mv {{project_directory}}/ {{project_directory|cut:project_name}}{{files.0}}/

rm $project_path/README.md $project_path/script.sh

project_path=`pwd`

rm $project_path/BRAND_NEW/README.md $project_path/BRAND_NEW/script.sh

test -d {{project_directory|cut:project_name}}{{files.0}} && echo "Directory '{{project_directory|cut:project_name}}{{files.0}}' already exists!" || mv {{project_directory}}/ {{project_directory|cut:project_name}}{{files.0}}/

#/bin/sh

python manage.py makemigrations app --no-input
python manage.py migrate --no-input

echo "=============load redirects================"
python manage.py loaddata fixture/data.json

python manage.py runserver 0.0.0.0:8000
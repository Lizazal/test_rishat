if [ ! -f "./.env" ];
then
    touch .env

	echo "STRIPE_PUBLIC_KEY=pk_test_51OpDqvARCcPcuqujJQF1CiOJkC1MeoISFbLDv4yGmrkJOcf1OkLgUHf9RCNNZzkAgTkB3Ws89RRNngwyPBGwmGrW008z5CKJ19" >> .env
	echo "STRIPE_SECRET_KEY=sk_test_51OpDqvARCcPcuqujUCQQhoVIeAZUHnrj5FpZFUMrGBp7px6Ii0AqPkjF3wZQf15gXz0PhuCj7yjnk3qxphSLbDcs00eNiXKZvc" >> .env
	echo "SECRET_KEY=7!!n=b*g_@90sf$j+#3nz!#_x7=xa7#!jcppuct5p75_tn1p!w" >> .env
fi

python -m venv venv
source .\venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

start java -jar utils/selenium-server-4.13.0.jar hub --host localhost
start java -jar utils/selenium-server-4.13.0.jar node --port 5555 --hub http://localhost:4444/
timeout 5
pip install -r requirements.txt
python -m pytest tests/test_customer.py --alluredir "./results"
npx allure-commandline serve "./results"
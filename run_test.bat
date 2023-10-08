
pip install -r requrements.txt
python -m pytest tests/test_customer.py --alluredir "./results"
npx allure-commandline serve "./results"
start start_hub.bat
start start_node.bat
timeout 5
pip install -r requrements.txt
python -m pytest tests/test_customer.py --alluredir "./results"
npx allure-commandline serve "./results"
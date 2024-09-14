# Student Registration Application Using TDD ( Test Driven Development ) 
Practice Repository for Flask


# Commands

## Create Virtual Environment 
```commandline
// Create Virtual Environment 
python3 -m venv venv

// Activate Virtual Environment 
source venv/bin/activate

pip3 install pytest
pip3 install pytest-cov

```

### To Run Specific Test 
```commandline
for Verbose pytest for all files and single test file respectively
pytest -v
pytest -v tests/test_integration.py

// following below commands not needed as things have been updated in pytest.ini file
pytest src
pytest --cov=src/
```

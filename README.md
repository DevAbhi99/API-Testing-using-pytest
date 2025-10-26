#Running the FastAPI
1. uvicorn Main:api --reload

#Running the Pytest to test each methods

1. pytest test_Main.py -m getTest -v --html=getReport.html
2. pytest test_Main.py -m postTest -v --html=postReport.html
3. pytest test_Main.py -m updateTest -v --html=updateReport.html
4. pytest test_Main.py -m deleteTest -v --html=deleteReport.html

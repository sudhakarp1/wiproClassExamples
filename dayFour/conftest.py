def pytest_addoption(parser):
    parser.addoption('--op1',action='store',default=100,help='testing')
    parser.addoption('--op2',action='store',default=200,help='testing')
    parser.addoption('--expRes',action='store',default=300,help='testing')

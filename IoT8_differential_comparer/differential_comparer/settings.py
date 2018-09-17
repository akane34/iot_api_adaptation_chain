import os

def init():
    global CONFLICT_SOLVER_URL

    CONFLICT_SOLVER_URL = 'http://localhost:5000'
    if os.getenv("CONFLICT_SOLVER_URL") is not None:
        CONFLICT_SOLVER_URL = str(os.getenv("CONFLICT_SOLVER_URL"))
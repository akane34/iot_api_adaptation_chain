from unittest import TestCase

from conflict_solver.services.conflict_service import solveConflict

class ConflictServiceTestCase(TestCase):

    def testSolveConflict(self):
        print('Testing conflict resolution')
        solveConflict()


if __name__ == '__main__':
    unittest.main()

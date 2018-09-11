from unittest import TestCase

from conflict_solver.models.resolution_model import ResolutionModel

class ResolutionModelTestCase(TestCase):

    def setUp(self):
        self.model = ResolutionModel()

    def testToJSON(self):
        print(self.model.toJSON())


    def testSelectAll(self):
        print(self.model.selectAll())


    def testSelectByID(self):
        print(self.model.selectByID())


if __name__ == '__main__':
    unittest.main()

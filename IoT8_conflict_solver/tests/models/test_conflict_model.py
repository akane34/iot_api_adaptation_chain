from unittest import TestCase

from conflict_solver.models.conflict_model \
        import insert, insertSingle, insertBulk
from conflict_solver.models.conflict_model \
        import ConflictModel

class ConflictModelTestCase(TestCase):

    def setUp(self):
        conflict1 = ConflictModel()
        conflict1.api_name='Api1'
        conflict1.old_api_version='1.0.0'
        conflict1.new_api_version='1.1.0'
        conflict1.path='/conflict1'
        conflict1.old_value='integer'
        conflict1.new_value='string'

        conflict2 = ConflictModel()
        conflict2.api_name='Api2'
        conflict2.old_api_version='2.0.0'
        conflict2.new_api_version='2.1.0'
        conflict2.path='/conflict2'
        conflict2.old_value='string'
        conflict2.new_value='integer'

        self.conflicts = [
                    conflict1,
                    conflict2,
                ]


    def testInsertSingle(self):
        conflict = self.conflicts[0]
        query = insertSingle(conflict)
        result_clauses = query.split(',')
        
        self.assertEqual(result_clauses[6].split()[0],
                '"{}"'.format(conflict.old_api_version))
        self.assertEqual(result_clauses[7].split()[0],
                '"{}"'.format(conflict.new_api_version))
        self.assertEqual(result_clauses[8].split()[0],
                '"{}"'.format(conflict.path))
        self.assertEqual(result_clauses[9].split()[0],
                '"{}"'.format(conflict.old_value))
        self.assertEqual(result_clauses[10].split()[0],
                '"{}");'.format(conflict.new_value))


    def testInsertBulk(self):
        conflict = self.conflicts[1]
        query = insertBulk(self.conflicts)
        result_clauses = query.split(',')

        self.assertEqual(result_clauses[11].split()[0],
                '("{}"'.format(conflict.api_name))
        self.assertEqual(result_clauses[12].split()[0],
                '"{}"'.format(conflict.old_api_version))
        self.assertEqual(result_clauses[13].split()[0],
                '"{}"'.format(conflict.new_api_version))
        self.assertEqual(result_clauses[14].split()[0],
                '"{}"'.format(conflict.path))
        self.assertEqual(result_clauses[15].split()[0],
                '"{}"'.format(conflict.old_value))
        self.assertEqual(result_clauses[16].split()[0],
                '"{}");'.format(conflict.new_value))


if __name__ == '__main__':
    unittest.main()

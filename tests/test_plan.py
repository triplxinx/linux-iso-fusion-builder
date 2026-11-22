import unittest
from iso_fusion.cli import plan
class TestPlan(unittest.TestCase):
 def test_dry_run(self): self.assertEqual(plan(["a.iso"],80)["operations_performed"],[])
 def test_reject_small_workspace(self):
  with self.assertRaises(ValueError): plan(["a.iso"],79)
 def test_reject_four_isos(self):
  with self.assertRaises(ValueError): plan(["a","b","c","d"],80)
if __name__=="__main__": unittest.main()

import unittest
import cluster

class TestCluster(unittest.TestCase):

    def test_lee_frames(self):
        #dataset = cluster.lee_frames('tests/lee_frames',3,1)
        #self.assertEqual(len(dataset),16)
        dataset2 = cluster.lee_frames('tests/lee_frames',3,2)
        self.assertEqual(len(dataset2),8)
        #dataset3 = cluster.lee_frames('tests/lee_frames',10,5)
        #self.assertEqual(len(dataset3),4)
    
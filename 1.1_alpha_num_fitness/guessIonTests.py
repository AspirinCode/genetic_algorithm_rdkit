#! /sur/bin/python
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem as Chem
from rdkit.Chem.Draw import ShowMol
import random
import unittest
import datetime
import genetic #our genetic engine code

class GuessIonTests(unittest.TestCase):
    geneSet= " CNHFBOSP123()[]#=-+,"
    
    def test_1_butyl_2_3_dimethyl_1H_imidazolium(self):
        target = "CCCC[NH+]1C=CN(C1C)C"
        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_1_butyl_2_3_dimethyl_1H_imidazolium)

    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(candidate):
            display(candidate, startTime)

        def fnShowIon():
            show_ion(target)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target),\
			optimalFitness, self.geneSet, fnDisplay,\
                        fnShowIon)
        self.assertEqual(best.Genes, target)
    
def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}".format(
	candidate.Genes, candidate.Fitness, timeDiff))
    
def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
              if expected == actual)

def show_ion(target):
    mol = Chem.MolFromSmiles(target)
    print("{}\t{}".format("number of atoms: ", mol.GetNumAtoms()))



if __name__ == '__main__':
    unittest.main()



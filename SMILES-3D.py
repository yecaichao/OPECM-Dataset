from rdkit import Chem
from rdkit.Chem import AllChem, Draw
smiles = 'CC(O)C(F)(F)F'
mol = Chem.MolFromSmiles(smiles)
mol = AllChem.AddHs(mol)
AllChem.EmbedMolecule(mol)
AllChem.MMFFOptimizeMolecule(mol)
Draw.MolToImage(mol, size=(250,250))
Chem.MolToMolFile(mol,'D:\Pycharm\des\CSV/name.mol2')
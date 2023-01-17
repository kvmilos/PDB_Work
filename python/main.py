import data
from operations import create_table


def main():
    lib = data.load_conll("/Users/kvmilos/Desktop/PDB/treebank/PDB_test.conll", "/Users/kvmilos/Desktop/PDB/treebank/PDB_dev.conll", "/Users/kvmilos/Desktop/PDB/treebank/PDB_train.conll")
    phr = data.load_txt("/Users/kvmilos/Desktop/PDB/sentences/PDB_test.txt", "/Users/kvmilos/Desktop/PDB/sentences/PDB_dev.txt", "/Users/kvmilos/Desktop/PDB/sentences/PDB_train.txt")
    meta = data.load_json("/Users/kvmilos/Desktop/PDB/meta/PDB_test.json", "/Users/kvmilos/Desktop/PDB/meta/PDB_dev.json", "/Users/kvmilos/Desktop/PDB/meta/PDB_train.json")

    tab = create_table(lib, phr, meta)
    data.save('../wyniki_17.01.csv', tab)


main()

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


# Pinus taeda 18S rRNA, complete sequence
# GenBank: AH001728.2
code = "TTTTGATGGTACCATACTACTCGGATAACCGTAGTAATTCTAGAGCTAATACGTGCACCAAGTCCCGACTCTTTGGAAGGGATGCATTTTTTAGATAAAAGGCCNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGCCCGCTTCTCCGGTGAATCATGATAACTCGACGGATCGCACAGCCCTTGTGCTGGNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCCTATCAACTTTCGATGGTAGGATAGAGGCCTACGATGGTGGTGACGGGTGACGGAGAATTAGGGTTCGATTCCGGAGAGGGAGCCTGAGAAACGGCTACCACATCCAAGGAAGGCAGCAGGCGCGCAAATTACCCAATCCTGACATGGGGAGGTAGTGACAATAAATAACAATACTGGGCTCATCGAGTCTGGTAATTGGAATGAGTACAATCTAAATCCCTTAACNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGATTTATGAAAGACGGACCACTGCGAAAGCATTTGCCAAGGATGTTTTCATTAATCAAGAANGAAAGTTGGGGGCTCGAAGACGATCAGATACCGGCCTAGTCTCAACCATAAACGATGCCGACCAGGGATCGGCGGATGTTGCTCTAAGGACTCCGCCAGCACCTTCTGAGAAATCAGAGTGTTTGGGTTCCGGGGGGAGTATGGTCNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGGGAAACTTACCAGGTCCAGACATAGTAAGGATTGACAGATTGAGAGCTCTTTCTTGATTCTATGGGTGGTGGTGCATGGCCGTTCTTAGTTGGTGGAGCGATTTGTCTGGTTAATTCCGATAACGAACGAGACCTCAGCCTGCTAACTAGCTACGCGGAGGTTCCCCTTCGCGGCCAGCTTCTTAGAGGGACTATGGCCGTTTAGGCCATNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTCTTCAACNNNGAATTCCTAGTAAGCGCGTGTCATCAACTCGTGTTGACTACGTCCCTGCCCTTTGTACACACCGCCCGNCGCTCCTACCGATTGAATGATCCGGTGAAGTGTTCGGANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGACGTCGTGAGAAGTTCATTGAACCTTATCATTTAGAGG"

# PtSIFG_0639 Pinus taeda cDNA libraries Pinus taeda STS cDNA clone RTFE1_12_G05_A029, sequence tagged site
# GenBank: BV728708.1
code = "TGCAGATTTCAATGCTGTTTTGAAAACATATTTTGAATTTTTTCATAGCCATCTCCATCTCCTTCTCGAGTCGTAGTATTATCCTATTTGCTTCCCTTCACCATCACCTAGTTCAGCTGCGAGAATGGCTTCAGCCGTGAGCAGCCGCCGCCAGCTTGAGGACGTGTTCCGCAAGTTCGACACCAATGGCGACGGCAAAATATCCAAGTCGGAACTGAGTGCCCTGATTTCGGAGGCGGAGATTGAAGGGGTGATGAAAGAGGTGGACTCCAACAAAGACGGATTCATCAACTTCGATGAGTTGGTGGAGGCCAACTCCAAGAACCTCAACGCCGCTAGTCTCATGCGAAATTCCGCTTCAGCTGTGCAATGTGCCGCCCTGCCCGGCCGCTTGGAGCTGGAGGACGTGTTCCGCAAGTTCGACACCAACGGCGACGGCAAAATATCGAAATCGGAACTGAGCGCTATCCTCAAGTGCAGCTCGAGTGAGGAGGAGATTGATGGTGTGATGAAGGACGTGGACTCCAACAAAGACGGCTTTATCAGCTTCGACGAGTTCGTGGCCGCCAACAGCAACGGCCTCAACGCCGCCCGTCTCATGCTAGGCCTCGCTTCAGCTAATTGATGCCCCCGCCGGCCCCTAATTAATAAATAAATAAATATTCCCCTACCTCAACTCTCAGCGCTTACCTCTATCACTATATGACTGCTGAATGCATGACTTTCAGTTTAAGAA"

myseq = Seq(code, IUPAC.unambiguous_dna)
# myseq.complement()
mrna = myseq.transcribe()
# print(mrna)
print(mrna.translate())

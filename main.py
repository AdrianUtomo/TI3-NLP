# Adrian Hakim Utomo - 2006597613 NLP 2022/2023

from performance import Performance
from trie_structure.levenshtein_trie import LevenshteinTrie
from trie_structure.damerau_levenshtein_trie import DamerauLevenshteinTrie
from dict_structure.levenshtein_dict import LevenshteinDict
from dict_structure.damerau_levenshtein_dict import DamerauLevenshteinDict

""" 
TODO: Hitung akurasi dan Run-Time dari semua algoritma yang sudah disediakan, seperti 
LevenshteinTrie, DamerauLevenshteinTrie, LevenshteinDict, dan DamerauLevenshteinDict. 
Gunakan SALTIK (https://github.com/ir-nlp-csui/saltik) sebagai dataset 
dan atur parameter MAX_COST untuk setiap algoritma sebesar 2 ketika memanggil 
fungsi untuk pengambilan kandidat.
"""
def main():
    print("[Adrian Hakim Utomo - 2006597613]")

    print("---------- lev_trie ----------")
    levenshtein_trie = LevenshteinTrie('bahasa-indonesia-dictionary.txt')
    lev_trie_performance = Performance(levenshtein_trie, 'saltik_200.json')
    print(lev_trie_performance.execute())

    print("---------- dalev_trie ----------")
    damerau_levenshtein_trie = DamerauLevenshteinTrie('bahasa-indonesia-dictionary.txt')
    dalev_trie_performance = Performance(damerau_levenshtein_trie, 'saltik_200.json')
    print(dalev_trie_performance.execute())

    print("---------- lev_dict ----------")
    levenshtein_dict = LevenshteinDict('bahasa-indonesia-dictionary.txt')
    lev_dict_performance = Performance(levenshtein_dict, 'saltik_200.json')
    print(lev_dict_performance.execute())

    print("---------- dalev_dict ----------")
    damerau_levenshtein_dict = DamerauLevenshteinDict('bahasa-indonesia-dictionary.txt')
    dalev_dict_performance = Performance(damerau_levenshtein_dict, 'saltik_200.json')
    print(dalev_dict_performance.execute())

if __name__ == '__main__':
    main()
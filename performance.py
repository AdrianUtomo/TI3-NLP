
"""
TODO: Gunakan file performance.py ini untuk membuat class Performance yang 
nantinya akan digunakan untuk menghitung akurasi (Best Match Accuracy & Candidate Match) 
dan run-time
"""
    
import json


class Performance :
    def __init__(self, algo, saltik_path):
        self.saltik = json.load(open(saltik_path))
        self.algo = algo

        def count_nonwords_error():
            res = 0
            for i in self.saltik:
                res += len(self.saltik[i])
            return res

        self.N = count_nonwords_error()

    
    def candidate_accuracy(self):
        M = 0
        for i in self.saltik:
            for j in self.saltik[i]:
                candidate_list = self.algo.get_candidates(j['typo'], 2)
                if i in candidate_list:
                    M += 1
        return (M/self.N)*100
    
    def best_match_accuracy(self):
        M = 0
        for i in self.saltik:
            for j in self.saltik[i]:
                candidate_list = self.algo.get_candidates(j['typo'], 2)
                if i == candidate_list[0]:
                    M += 1
        return (M/self.N)*100

    def execute(self):
        res = ""
        res += "Candidate Accuracy: " + str(self.candidate_accuracy()) + "%\n"
        res += "Best Match Accuracy: " + str(self.best_match_accuracy()) + "%\n"
        return res
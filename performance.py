# Adrian Hakim Utomo - 2006597613 NLP 2022/2023

"""
TODO: Gunakan file performance.py ini untuk membuat class Performance yang 
nantinya akan digunakan untuk menghitung akurasi (Best Match Accuracy & Candidate Match) 
dan run-time
"""
    
import json
import time


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

    
    def calculate_accuracy(self):
        M_candidate = 0
        M_best_match = 0
        start = time.time()
        for i in self.saltik:
            for j in self.saltik[i]:
                candidate_list = self.algo.get_candidates(j['typo'], 2)
                if i == candidate_list[0]:
                    M_best_match += 1
                elif i in candidate_list:
                    M_candidate += 1
        end = time.time()

        result = {
            "candidate": (M_candidate/self.N)*100,
            "best_match": (M_best_match/self.N)*100,
            "runtime": (start-end)
        }
        return result

    def execute(self):
        accuracy = self.calculate_accuracy()
        res = ""
        res += "Candidate Accuracy: " + str(accuracy["candidate"]) + "%\n"
        res += "Best Match Accuracy: " + str(accuracy["best_match"] + "%\n")
        res += "Run-Time: " + str(accuracy["runtime"]) + " seconds"
        return res
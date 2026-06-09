class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs = []

        if not digits:
            return []

        digitsToMapped = {"2":"abc",
                          "3":"def",
                          "4":"ghi",
                          "5":"jkl",
                          "6":"mno",
                          "7":"pqrs",
                          "8":"tuv",
                          "9":"wxyz"}
        
        def backtrack(i, digits, combs, curComb):
            if i == len(digits):
                combs.append(curComb)
                return
                
            for c in digitsToMapped[digits[i]]:
                backtrack(i + 1, digits, combs, curComb + c)

        backtrack(0, digits, combs, "")
        return combs
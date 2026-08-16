class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        
        for op in operations: 
            length = len(arr)
            if op == "C":
                arr.pop()
            elif op == "D":
                product = arr[-1] * 2
                arr.append(product)
            elif op == "+":
                total = arr[-1] + arr[-2]
                arr.append(total)
            else:
                arr.append(int(op))

        return sum(arr)

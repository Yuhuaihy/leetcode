if not numRows:
            return []
        result = []
        result.append([1])
        for i in range(1,numRows):
            result.append([])
            result[i].append(1)
            for j in range(1,i):
                result[i].append(result[i-1][j-1] + result[i-1][j])
            result[i].append(1)
        return result 

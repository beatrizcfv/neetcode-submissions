class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Contar frec de cada num
        contador = defaultdict(int)
        for i in nums: # i son los valores de nums
            contador[i] += 1 

        tuples = list(contador.items())
        tuples.sort(key=lambda x: x[1], reverse=True) # Ordenar por el 2º numero

        resultado = []
        for i in range(k):
            resultado.append(tuples[i][0])

        return resultado
        
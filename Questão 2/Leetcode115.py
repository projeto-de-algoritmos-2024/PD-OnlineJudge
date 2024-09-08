from collections import Counter

class Solution(object):
    def numDistinct(self, s, t):
        # Contagem das letras em s e t
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Inicializa o número máximo de vezes que t pode ser formado
        max_count = float('inf')
        
        # Verifica cada letra em t
        for char in count_t:
            if char in count_s:
                # Calcula quantas vezes a letra pode ser usada para formar t
                max_count = min(max_count, count_s[char] // count_t[char])
            else:
                # Se a letra de t não estiver em s, não é possível formar t
                return 0
        
        return max_count
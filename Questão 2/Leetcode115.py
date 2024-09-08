class Solution(object):
    def numDistinct(self, s, t):
        count = 0  # Contador para o número de vezes que `t` pode ser formado
        s_list = list(s)  # Converte `s` em uma lista para manipulação direta
        
        while True:
            j = 0  # Índice para percorrer `t`
            i = 0  # Índice para percorrer `s_list`
            
            while i < len(s_list) and j < len(t):
                if s_list[i] == t[j]:
                    s_list[i] = None  # Marca o caractere como usado
                    j += 1  # Avança no `t` quando há correspondência
                i += 1
            
            # Se conseguimos formar `t`, incrementamos o contador
            if j == len(t):
                count += 1
            else:
                break  # Se `t` não puder ser formado, saímos do loop
        
        return count
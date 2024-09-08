class Solution(object):
    def numDistinct(self, s, t):
        # Tamanho das strings
        m, n = len(s), len(t)
        
        # Inicializa a matriz dp com zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Uma string vazia `t` pode ser formada a partir de qualquer prefixo de `s`
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Preenche a matriz dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Se os caracteres atuais coincidem, somar as formas usando ou não usando o caractere de s
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        # O resultado está na última célula da matriz
        return dp[m][n]

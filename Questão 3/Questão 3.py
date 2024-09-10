class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)  # Usamos um set para rápida verificação de palavras
        memo = {}  # Memorização para evitar recalcular soluções
        
        def dfs(start):
            # Se já processamos essa substring antes, retornamos o resultado salvo
            if start in memo:
                return memo[start]
            
            # Se chegamos ao final da string, retornamos uma lista vazia
            if start == len(s):
                return [""]
            
            res = []
            # Tentamos todas as possíveis palavras começando de 'start'
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Chamamos dfs recursivamente para o restante da string
                    sublist = dfs(end)
                    for sub in sublist:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
            
            # Salvamos o resultado dessa substring no memo
            memo[start] = res
            return res
        
        return dfs(0)

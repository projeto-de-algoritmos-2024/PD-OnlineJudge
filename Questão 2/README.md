## Leetcode 115. Subsequências Distintas

**Status:** Resolvido  
**Dificuldade:** Hard

Link para o enunciado completo:

https://leetcode.com/problems/distinct-subsequences/description/

Dadas duas strings `s` e `t`, retorne o número de subsequências distintas de `s` que é igual a `t`.

Os casos de teste são gerados para que a resposta caiba em um inteiro assinado de 32 bits.

### Exemplos

**Exemplo 1:**

- **Entrada:** `s = "coelho"`, `t = "coelho"`
- **Saída:** 3
- **Explicação:** Conforme mostrado abaixo, há 3 maneiras de gerar "coelho" a partir de `s`:
  - rabbbit
  - rabbbit
  - rabbbit

**Exemplo 2:**

- **Entrada:** `s = "babgbag"`, `t = "bag"`
- **Saída:** 5
- **Explicação:** Conforme mostrado abaixo, há 5 maneiras de gerar "bag" a partir de `s`:
  - babgbag
  - babgbag
  - babgbag
  - babgbag
  - babgbag

 Submissões:

 ![image](https://github.com/user-attachments/assets/5addce71-0d74-4a36-b82d-ed48bd8827d4)


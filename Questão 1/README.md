### Leetcode 123. Melhor Hora para Comprar e Vender Ações III

**Status:** Resolvido  
**Dificuldade:** Duro  
**Tópicos:** Empresas

Você recebe uma matriz `prices` onde `prices[i]` está o preço de uma determinada ação no dia `i`. Encontre o lucro máximo que você pode atingir. Você pode completar no máximo duas transações.

**Observação:** Você não pode realizar várias transações simultaneamente (ou seja, você deve vender as ações antes de comprá-las novamente).

#### Exemplos

**Exemplo 1:**

- **Entrada:** `preços = [3,3,5,0,0,3,1,4]`
- **Saída:** `6`
- **Explicação:** Compre no dia 4 (preço = 0) e venda no dia 6 (preço = 3), lucro = 3-0 = 3. Então compre no dia 7 (preço = 1) e venda no dia 8 (preço = 4), lucro = 4-1 = 3.

**Exemplo 2:**

- **Entrada:** `preços = [1,2,3,4,5]`
- **Saída:** `4`
- **Explicação:** Compre no dia 1 (preço = 1) e venda no dia 5 (preço = 5), lucro = 5-1 = 4. Note que você não pode comprar no dia 1, comprar no dia 2 e vendê-los depois, pois você está realizando várias transações ao mesmo tempo. Você deve vender antes de comprar novamente.

**Exemplo 3:**

- **Entrada:** `preços = [7,6,4,3,1]`
- **Saída:** `0`
- **Explicação:** Neste caso, nenhuma transação é feita, ou seja, lucro máximo = 0.

Para o enunciado completo:

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

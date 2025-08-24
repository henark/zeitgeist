# Guia de Configuração do TimeFarm Bot

Este documento detalha as variáveis de ambiente usadas para configurar o `timefarm-bot`. Estas variáveis são lidas de um arquivo `.env` que deve ser criado na raiz do projeto.

---

## O que cada variável faz

| Seção | Variável | Valor padrão | O que controla |
|-------|----------|--------------|----------------|
| **BOT BEHAVIOR** | `AUTO_TASKS` | `"true"` | Se o bot deve executar automaticamente as tarefas que ele tem permissão (por exemplo, “claim”, “upgrade”, “farm”). |
| | `AUTO_CLAIM_REFF` | `"true"` | Se o bot deve, de forma automática, reivindicar bônus de indicação (referral) assim que eles ficarem disponíveis. |
| | `AUTO_UPGRADE` | `"true"` | Se o bot deve tentar fazer upgrades (por exemplo, melhorar a fazenda, comprar novos itens, subir de nível) sempre que houver recursos suficientes. |
| **TIME CALIBRATION** | `REFRESH_CLAIM` | `"3600"` (segundos) | Intervalo **menor** (minor cycle). A cada 1 h o bot roda o loop de “claim/upgrade”. Ajuste para mais ou menos frequência dependendo da taxa de geração de recompensas no seu jogo. |
| | `REFRESH_TOKEN` | `"86400"` (segundos) | Intervalo **maior** (major cycle). A cada 24 h o bot renova o token de autenticação. Deve ser menor que o tempo de expiração real do token (geralmente algumas horas a dias). |

---

## Como ajustar para o seu caso de uso

### 1. Frequência de “claim/upgrade” (`REFRESH_CLAIM`)
- **Jogos com produção rápida** (ex.: recursos a cada 5‑15 min): diminua para `300`‑`900` (5‑15 min).
- **Jogos com produção lenta** (ex.: recompensas a cada 2‑4 h): aumente para `7200`‑`14400` (2‑4 h).
- **Equilíbrio**: 1 h costuma ser um “bom meio‑termo” – você coleta antes que a recompensa expire, mas não sobrecarrega a API.

### 2. Renovação de token (`REFRESH_TOKEN`)
- Verifique o **tempo de vida (TTL)** do token que o seu backend fornece (geralmente indicado nos cabeçalhos `expires_in` ou no payload JWT).
- Defina `REFRESH_TOKEN` **10‑20 % antes** do TTL real para garantir que o bot nunca tente usar um token expirado.
  - Ex.: se o token expira em 48 h → `REFRESH_TOKEN="43200"` (12 h) ou `86400` (24 h) ainda funciona, mas 12 h dá margem extra.
- Se o backend tem *refresh‑token* (token de renovação), você pode deixar o intervalo maior, pois o bot pode solicitar um novo token a qualquer momento.

### 3. Ativar / desativar comportamentos automáticos
- **Desativar temporariamente**: troque `"true"` por `"false"` na linha correspondente.
  ```bash
  AUTO_UPGRADE="false"
  ```
- **Modo “test‑only”**: deixe `AUTO_TASKS="false"` e rode manually os comandos que deseja observar; isso ajuda a depurar sem que o bot faça mudanças inesperadas.

---

## Exemplo de configuração ajustada

```bash
# --- BOT BEHAVIOR ---
AUTO_TASKS="true"          # ainda queremos que o bot faça tudo automaticamente
AUTO_CLAIM_REFF="true"     # reivindicar bônus de indicação
AUTO_UPGRADE="true"        # upgrades automáticos

# --- TIME CALIBRATION ---
# Se o jogo gera recompensas a cada 30 min:
REFRESH_CLAIM="1800"       # 30 min (1800 s)

# Token expira em 48 h → renovamos a cada 12 h:
REFRESH_TOKEN="43200"      # 12 h (43200 s)
```

---

## Dicas práticas de implantação

| Passo | O que fazer | Por quê |
|------|--------------|--------|
| **1️⃣ Teste localmente** | Rode o bot em modo “dry‑run” (por exemplo, `--dry` ou `AUTO_TASKS="false"`). | Verifica se as chamadas de API estão corretas antes de automatizar. |
| **2️⃣ Log de atividades** | Ative logs detalhados (`LOG_LEVEL=debug` ou similar). | Facilita a identificação de falhas de token ou de limites de taxa (rate‑limits). |
| **3️⃣ Monitoramento de rate‑limit** | Se a API tem limites (ex.: 100 chamadas/h), ajuste `REFRESH_CLAIM` para não exceder. | Evita bloqueios temporários da conta. |
| **4️⃣ Backup de tokens** | Salve o token atual em um arquivo seguro antes de sobrescrevê‑lo. | Caso a renovação falhe, você ainda tem um token válido para retomar. |
| **5️⃣ Alertas** | Configure um webhook ou e‑mail para ser notificado quando o bot falhar (ex.: falha ao renovar token). | Você pode agir rapidamente sem precisar checar manualmente. |

---

## Perguntas frequentes

| Pergunta | Resposta curta |
|----------|----------------|
| **Posso usar valores fracionados (ex.: `REFRESH_CLAIM="900.5"`)?** | Não. As variáveis são interpretadas como inteiros em segundos. Use apenas números inteiros. |
| **O que acontece se eu colocar `AUTO_CLAIM_REFF="false"`?** | O bot simplesmente ignora a lógica de reivindicação de bônus de indicação; isso pode ser útil se o jogo penaliza chamadas excessivas ou se você prefere fazer isso manualmente. |
| **Como saber o TTL do token?** | Muitas APIs retornam um JWT; decodifique o payload (campo `exp`) para ver o timestamp de expiração. Também pode aparecer nos cabeçalhos `Cache-Control` ou `Expires`. |
| **É seguro deixar `AUTO_UPGRADE="true"`?** | Depende da estratégia de jogo. Se upgrades custam recursos que você prefere guardar, desative temporariamente. Caso contrário, pode acelerar o progresso. |
| **Preciso reiniciar o bot após mudar a configuração?** | Sim. As variáveis são lidas na inicialização. Reinicie o processo ou recarregue o arquivo de configuração. |

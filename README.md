# Clube de Corrida · 15 anos (biolink)

Biolink mobile-first do Clube de Corrida (@clubedecorridadopi), Teresina-PI. Feito pela VOLTZ MEDIA.

## Como publicar
`index.html` é um arquivo único (fotos e fontes já embutidas, sem dependências externas).
No GitHub: suba este repositório e ative **Settings > Pages > Deploy from a branch > main / (root)**.

## Estrutura
- `index.html`: o biolink pronto.
- `src/tpl.html`: o código-fonte (marcadores `{{arquivo}}` apontam para `src/a/`).
- `src/a/`: fotos, logos e fontes. Os ZIPs de fotos e de logos/imagens são extraídos dentro de `src/a/`.
- `src/build.py`: regera o `index.html` (`python3 src/build.py`).

## Pendências de conteúdo
- Depoimentos da seção Feedbacks são **exemplos genéricos**; trocar pelos reais (`src/tpl.html`, seção `id="feedbacks"`).
- Link de inscrição do CDC Legends, endereço exato e logo da Eugênio Fortes Academia.

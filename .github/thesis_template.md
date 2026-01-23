---
layout: thesis
title: "[TÍTULO DA TESE/DISSERTAÇÃO]"
author: "[Autor(a)]"
year: [ANO]
type: "[Master/PhD] Thesis"
pdf_url: "[https://link-para-o-pdf]"
award: "[Prêmio, se houver]"
---


## Metadados da Tese/Dissertação

Os campos abaixo devem ser preenchidos com as informações correspondentes à tese/dissertação como front matter do arquivo markdown.

```markdown
---
layout: thesis
title: "[TÍTULO DA TESE/DISSERTAÇÃO]"
author: "[Autor(a)]"
year: [ANO]
type: "[Master/PhD] Thesis"
pdf_url: "[https://link-para-o-pdf]"
award: "[Prêmio, se houver]"
---

[bibtex da tese/dissertação aqui]
```

## BibTeX

O bibtex da tese/dissertação deve ir no body do arquivo markdown, dentro de um bloco de código `{% raw %}` para evitar que o Jekyll processe os caracteres especiais. Aqui está um exemplo de como deve ser formatado:
```
{% raw %}
@phdthesis{[chave-bibtex],
  author = {[Autor(a)]},
  title = {[TÍTULO DA TESE/DISSERTAÇÃO]},
  school = {[Nome da Instituição]},
  year = {[ANO]}
}
{% endraw %}
```

## Checklist
- [ ] O arquivo da tese/dissertação está nomeado como `YYYY-titulo-da-tese.md` e está na pasta correta (`_theses`).
- [ ] Todos os campos obrigatórios de metadados estão preenchidos no front matter.
- [ ] O registro BibTeX está incluído e correto.
- [ ] O autor está correto.
- [ ] A instituição e o ano estão corretos.
- [ ] As URLs são válidas e apontam para os recursos corretos.

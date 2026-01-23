---
layout: publication
title: "[TÍTULO DA PUBLICAÇÃO]"
authors: "[Autor 1, Autor 2]"
venue: "[Nome da Conferência/Periódico]"
year: [ANO]
pages: "[Faixa de páginas, ex: 1--5]"
pdf_url: "[https://link-para-o-pdf]"
doi_url: "[https://doi.org/...]"
slide_url: "[https://link-para-os-slides]"
award: "[Prêmio, se houver]"
---


## Metadados da Publicação

Os campos abaixo devem ser preenchidos com as informações correspondentes à publicação como front matter do arquivo markdown.

```markdown
---
layout: publication
title: "[TÍTULO DA PUBLICAÇÃO]"
authors: "[Autor 1, Autor 2]"
venue: "[Nome da Conferência/Periódico]"
year: [ANO]
pages: "[Faixa de páginas, ex: 1--5]"
pdf_url: "[https://link-para-o-pdf]"
doi_url: "[https://doi.org/...]"
slide_url: "[https://link-para-os-slides]"
award: "[Prêmio, se houver]"
---

[bibtex do artigo aqui]
```

## BibTeX

O bibtex do artigo deve ir no body do arquivo markdown, dentro de um bloco de código `{% raw %}` para evitar que o Jekyll processe os caracteres especiais. Aqui está um exemplo de como deve ser formatado:

```markdown
{% raw %}
@inproceedings{[chave-bibtex],
  author = {[Autor 1 and Autor 2]},
  title = {[TÍTULO DA PUBLICAÇÃO]},
  booktitle = {[Nome da Conferência/Periódico]},
  year = {[ANO]},
  pages = {[Faixa de páginas, ex: 1--5]}
}
{% endraw %}
```

## Checklist

Verifique os seguintes itens antes de submeter o pull request da publicação:

- [ ] O arquivo da publicação está nomeado como `YYYY-titulo-da-publicacao.md` e está na pasta correta (`_publications` ou `_publications_ptbr`).
- [ ] Todos os campos obrigatórios de metadados estão preenchidos no front matter.
- [ ] O registro BibTeX está incluído e correto.
- [ ] Os autores estão na ordem correta.
- [ ] O veículo e o ano estão corretos.
- [ ] As URLs são válidas e apontam para os recursos corretos.

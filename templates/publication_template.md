## Local do arquivo

O arquivo markdown da publicação deve ser salvo na pasta `_publications` (para publicações em inglês) ou `_publications_ptbr` (para publicações em português) do repositório. 
O nome do arquivo deve seguir o formato `YYYY-titulo-da-publicacao.md`, onde `YYYY` é o ano da publicação e `titulo-da-publicacao` é uma versão em minúsculas e com hífens do título da publicação.

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

## Exemplo Completo

```markdown
---
layout: publication
title: "Um Estudo sobre Algoritmos de Classificação"
authors: "Ana Pereira, Carlos Souza"
venue: "Conferência Brasileira de Inteligência Artificial"
year: 2022
pages: "10--20"
pdf_url: "https://example.com/ana_pereira_study.pdf"
doi_url: "https://doi.org/10.1000/cbia2022.001
slide_url: "https://example.com/ana_pereira_slides.pdf"
award: "Melhor Artigo Estudantil"
---

{% raw %}
@inproceedings{pereira2022estudo,
  author = {Ana Pereira and Carlos Souza},
  title = {Um Estudo sobre Algoritmos de Classificação},
  booktitle = {Conferência Brasileira de Inteligência Artificial},
  year = {2022},
  pages = {10--20}
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

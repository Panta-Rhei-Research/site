#let dossier(
  title: "",
  description: "",
  canonical_url: "",
  kind: "",
  status: "",
  review_angle: "",
  generated: "",
  body,
) = {
  set page(
    paper: "a4",
    margin: (x: 22mm, y: 24mm),
    header: align(right)[
      #text(size: 8pt, fill: rgb("#163e64"))[Panta Rhei Research Program]
    ],
    footer: align(center)[
      #text(size: 8pt, fill: rgb("#667085"))[
        #context counter(page).display("1")
      ]
    ],
  )
  set text(size: 10.2pt, lang: "en")
  set par(justify: true, leading: 0.62em)
  set heading(numbering: none)

  block(
    fill: rgb("#f6f7f3"),
    stroke: 0.75pt + rgb("#d8ded2"),
    radius: 5pt,
    inset: 12pt,
  )[
    #text(size: 8pt, weight: "bold", fill: rgb("#163e64"))[PANTA RHEI DOSSIER]
    #v(4pt)
    #text(size: 22pt, weight: "bold")[#title]
    #if description != "" [
      #v(4pt)
      #text(size: 10pt, fill: rgb("#4d5968"))[#description]
    ]
    #v(8pt)
    #grid(
      columns: (1fr, 1fr),
      gutter: 8pt,
      [#text(size: 8pt, weight: "bold", fill: rgb("#163e64"))[Status]\ #text(size: 8pt)[#status]],
      [#text(size: 8pt, weight: "bold", fill: rgb("#163e64"))[Review angle]\ #text(size: 8pt)[#review_angle]],
      [#text(size: 8pt, weight: "bold", fill: rgb("#163e64"))[Kind]\ #text(size: 8pt)[#kind]],
      [#text(size: 8pt, weight: "bold", fill: rgb("#163e64"))[Generated]\ #text(size: 8pt)[#generated]],
    )
  ]

  v(14pt)
  body

  v(18pt)
  block(
    fill: rgb("#fbfbf7"),
    stroke: 0.5pt + rgb("#e1e6db"),
    radius: 4pt,
    inset: 10pt,
  )[
    #text(weight: "bold", fill: rgb("#163e64"))[Continue exploring]
    #v(4pt)
    Canonical URL: #link(canonical_url)[#canonical_url]
    #v(8pt)
    #text(weight: "bold", fill: rgb("#163e64"))[Citation and provenance]
    #v(4pt)
    This dossier is generated from the public Panta Rhei website route above. Prefer the canonical route for citation unless a release package specifies otherwise.
  ]
}

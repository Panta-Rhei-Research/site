---
layout: program-doc
title: "TauLib Architecture"
permalink: /corpus/taulib/architecture/
lane: corpus
v2_lane: corpus
type: "Corpus Projection Architecture"
status: "Canonical"
summary_short: "Book and family structure of the Corpus-owned TauLib projection."
---

{% assign modules = site.data.taulib["module-inventory"] %}
{% assign books = modules | group_by: "book" %}

## Book and family structure

TauLib follows the Corpus construction rather than standing outside it. Module families track books, construction layers, and local formalization neighborhoods.

{% for book in books %}
{% assign families = book.items | group_by: "family" %}
### {{ book.name | default: "Root" }}

<ul class="v2-grid v2-card-list">
{% for family in families %}
  <li><article class="v2-tile"><h3>{{ family.name | default: "Root" }}</h3><p>{{ family.items | size }} module{% unless family.items.size == 1 %}s{% endunless %}.</p></article></li>
{% endfor %}
</ul>
{% endfor %}

## Relation to Verify

Architecture here means Corpus architecture: modules, imports, and Registry anchors. Verify uses this architecture to ask higher-level questions about coverage, bridge adequacy, and claim boundaries.

## Categorical structure note

TauLib does not import `Mathlib.CategoryTheory` or instantiate the Mathlib `Category` typeclass on `TauObj`. The categorical structure of τ is realized through hand-rolled morphism types (`CatTau`, `HolEndCat`, `TauArrow`, `id_arrow`, `arrow_comp_stage`) defined within TauLib itself, rather than as an `instance : Category TauObj`.

This is a deliberate architectural choice — the program treats τ as a categorical structure in its own right, with the morphism layer earned from K0–K6 and the progression operator ρ rather than inherited from Mathlib's general category-theory hierarchy. A reviewer should expect to find:

- `class Category` / `def Hom` / `Iso` constructions inside `TauLib/BookI/Category/…` and `TauLib/BookII/Categorical/…`, not via Mathlib instances.
- A separate Mathlib-bridge layer (where Mathlib `CategoryTheory` *is* used as a comparison target) is on the formalization roadmap; it is not part of the current release.

The K0–K6 themselves are realized in TauLib as **theorems-by-construction** over the inductive `Generator` and `TauObj` types — i.e. they hold for the chosen representation by definition of how those inductives are built — rather than as Lean `axiom` declarations in the strict TCB sense. The three custom axioms that *do* sit outside Mathlib's trusted base are inventoried separately at [Custom Axioms]({{ '/verify/custom-axioms/' | relative_url }}); K0–K6 are not among them. This is why the program describes K0–K6 as the kernel's *structural commitments* on the marketing surface rather than as its TCB axioms.

---
layout: program-doc
title: "Corpus Types"
lane: corpus
v2_lane: corpus
permalink: /corpus/types/
type: "Corpus Guide"
status: "Canonical"
summary_short: "A guide to the object types used in the research corpus."
right_rail:
  related:
    - title: "Registry"
      url: /corpus/registry/
    - title: "How to Read"
      url: /corpus/how-to-read/
    - title: "Corpus Graph"
      url: /corpus/graph/
  meta:
    type: "Corpus Guide"
    status: "Canonical"
    updated: "April 2026"
---

{% assign registry_objects = site.data.registry.objects %}
{% assign corpus_type_grammar = site.data.corpus.registry_object_types.object_types %}
{% assign type_groups = registry_objects | group_by: "type" | sort: "name" %}

## Type grammar

The corpus distinguishes object types so readers do not confuse definitions, lemmas, theorems, constructions, conjectures, remarks, and bridge claims.

The registry already exposes object IDs and book locations. Wave 3 makes the type grammar Corpus-owned metadata so the public page is no longer hand-maintaining these labels independently.

<div class="v2-grid">
  {% if corpus_type_grammar %}
  {% for pair in corpus_type_grammar %}
  {% assign group = type_groups | where: "name", pair[0] | first %}
  <div class="v2-tile" id="{{ group.name | slugify }}">
    <strong>{{ pair[1].label }}</strong>
    <span>{% if group %}{{ group.size }}{% else %}0{% endif %} current registry objects use this type.</span>
    <p>{{ pair[1].description }}</p>
  </div>
  {% endfor %}
  {% else %}
    {% for group in type_groups %}
    <div class="v2-tile" id="{{ group.name | slugify }}">
      <strong>{{ group.name | capitalize }}</strong>
      <span>{{ group.size }} current registry objects use this type.</span>
    </div>
    {% endfor %}
  {% endif %}
</div>

## Why type matters

Type labels help readers decide what kind of burden a page carries. A theorem, a conjectural bridge, a definition, and an explanatory remark do not make the same kind of claim.

## Reading the common types

{% if corpus_type_grammar %}
{% for pair in corpus_type_grammar %}
- **{{ pair[1].label }}**: {{ pair[1].description }}
{% endfor %}
{% else %}
- **Axiom**: a foundational commitment of the formal kernel.
- **Definition**: an introduced object, relation, construction, or term.
- **Lemma**: a supporting result used by later statements.
- **Proposition**: a local result or structured claim with narrower scope.
- **Theorem**: a load-bearing result with stronger downstream use.
- **Corollary**: a result obtained from prior statements.
- **Remark**: explanatory or interpretive material attached to the formal spine.
- **Construction**: an explicit built object or method.
{% endif %}

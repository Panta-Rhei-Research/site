---
{
  "projection_kind": "taulib_declaration",
  "title": "SemanticObjectResult",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/semantic-object-result/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::SemanticObjectResult",
  "declaration_slug": "semantic-object-result",
  "kind": "structure",
  "name": "SemanticObjectResult",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 444,
  "source_line_end": 454,
  "registry_ids": [
    "VII.T37"
  ],
  "related_registry_items": [
    {
      "id": "VII.T37",
      "title": "Semantic Object Construction (S)",
      "url": "/registry/object/VII.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L444-L454",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L444-L454",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L444-L454)
- Source range: L444-L454
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.T37` — Semantic Object Construction (S)

## Immediate Comment / Docstring

```lean
/-- [VII.T37] Semantic Object Construction (ch89, Stage S). At E₃, internally
    constructible:
    (1) Typed maxims: m = (α, φ) as sections of M, using [A,A] and Ω
    (2) Universalization domains: sieve {c | U(m)(c) enactable}
    (3) Personhood predicates: identity-invariants as decidable internal predicates
    (4) Obligation morphisms: dignity-preserving f : X → Y in A_dig -/
```

## Source Excerpt

```lean
structure SemanticObjectResult where
  /-- Typed maxims constructible. -/
  typed_maxims : Bool := true
  /-- Universalization domains well-defined. -/
  universalization_domains : Bool := true
  /-- Personhood predicates decidable internally. -/
  personhood_predicates : Bool := true
  /-- Obligation morphisms in A_dig. -/
  obligation_morphisms : Bool := true
  semantic_component_count : Nat := 4
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "obstruction_value",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/obstruction-value/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationObstruction`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationObstruction::obstruction_value",
  "declaration_slug": "obstruction-value",
  "kind": "def",
  "name": "obstruction_value",
  "module_name": "TauLib.BookIII.Bridge.TranslationObstruction",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/",
  "source_line_start": 78,
  "source_line_end": 98,
  "registry_ids": [
    "III.D91"
  ],
  "related_registry_items": [
    {
      "id": "III.D91",
      "title": "Obstruction Cocycle",
      "url": "/registry/object/III.D91/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L78-L98",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationObstruction",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L78-L98",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Bridge.TranslationObstruction](/verify/taulib/docs/book-iii-bridge-translation-obstruction/)
- Source path: [`TauLib/BookIII/Bridge/TranslationObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L78-L98)
- Source range: L78-L98
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D91` — Obstruction Cocycle

## Immediate Comment / Docstring

```lean
/-- [III.D91] Obstruction value at stage k: measures deviation from
    faithful translation. Higher = worse. -/
```

## Source Excerpt

```lean
def obstruction_value (obs : TranslationObstruction) (k : Nat) : Nat :=
  let pk := primorial k
  match obs with
  | .unbounded_fanout =>
    -- Number of prime factors at stage k (grows linearly)
    k
  | .global_equality =>
    -- Number of elements with non-unique normal forms: 0 at each finite stage
    -- (NF IS unique at finite stages — obstruction only at limit)
    0
  | .succinct_circuits =>
    -- Circuit complexity grows exponentially with k
    -- At stage k, the state space is M_k (exponential in k)
    if pk > 0 then pk else 0
  | .exponential_quantification =>
    -- Quantifier depth needed grows with k
    if pk > 0 then pk else 0
  | .nonlocal_disguise =>
    -- Number of disguised representations: 0 at finite stages
    -- (reduce gives unique representation)
    0
```

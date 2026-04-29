---
{
  "projection_kind": "taulib_declaration",
  "title": "ShadowIdentity",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/shadow-identity/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.DiagonalResonance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.DiagonalResonance::ShadowIdentity",
  "declaration_slug": "shadow-identity",
  "kind": "structure",
  "name": "ShadowIdentity",
  "module_name": "TauLib.BookI.MetaLogic.DiagonalResonance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/",
  "source_line_start": 106,
  "source_line_end": 113,
  "registry_ids": [
    "I.D91"
  ],
  "related_registry_items": [
    {
      "id": "I.D91",
      "title": "Shadow Identity",
      "url": "/registry/object/I.D91/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L106-L113",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.DiagonalResonance",
        "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L106-L113",
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

- Module: [TauLib.BookI.MetaLogic.DiagonalResonance](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/)
- Source path: [`TauLib/BookI/MetaLogic/DiagonalResonance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L106-L113)
- Source range: L106-L113
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D91` — Shadow Identity

## Immediate Comment / Docstring

```lean
/-- [I.D91] Shadow identity witness: a channel that acts like identity without being
    ontically constructed. -/
```

## Source Excerpt

```lean
structure ShadowIdentity where
  kind : ShadowIdentityType
  resonance : DiagonalResonance
  -- The required components must be present
  component_present : match kind with
    | .equivalenceWitness => resonance.equality_congruence = true
    | .substitutionBridge => resonance.equality_congruence = true ∧ resonance.contraction_present = true
    | .diagonalProjection => resonance.self_products = true
```

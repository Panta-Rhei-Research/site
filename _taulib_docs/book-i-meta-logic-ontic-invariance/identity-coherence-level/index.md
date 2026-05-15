---
{
  "projection_kind": "taulib_declaration",
  "title": "identityCoherenceLevel",
  "permalink": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/identity-coherence-level/",
  "summary_short": "`def` declaration in `TauLib.BookI.MetaLogic.OnticInvariance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.OnticInvariance::identityCoherenceLevel",
  "declaration_slug": "identity-coherence-level",
  "kind": "def",
  "name": "identityCoherenceLevel",
  "module_name": "TauLib.BookI.MetaLogic.OnticInvariance",
  "module_url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/",
  "source_line_start": 102,
  "source_line_end": 106,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L102-L106",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.OnticInvariance",
        "url": "/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L102-L106",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookI.MetaLogic.OnticInvariance](/corpus/taulib/docs/book-i-meta-logic-ontic-invariance/)
- Source path: [`TauLib/BookI/MetaLogic/OnticInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L102-L106)
- Source range: L102-L106
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Identity coherence level: 100% means no component of diagonal resonance is present. -/
```

## Source Excerpt

```lean
def identityCoherenceLevel (dr : DiagonalResonance) : Nat :=
  let blocked := (if dr.contraction_present then 0 else 1) +
                 (if dr.equality_congruence then 0 else 1) +
                 (if dr.self_products then 0 else 1)
  blocked * 100 / 3
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "IsCrossingPoint",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/is-crossing-point/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.IotaTauStructural`.",
  "declaration_id": "TauLib.BookI.Boundary.IotaTauStructural::IsCrossingPoint",
  "declaration_slug": "is-crossing-point",
  "kind": "def",
  "name": "IsCrossingPoint",
  "module_name": "TauLib.BookI.Boundary.IotaTauStructural",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/",
  "source_line_start": 146,
  "source_line_end": 147,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L146-L147",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.IotaTauStructural",
        "url": "/verify/taulib/docs/book-i-boundary-iota-tau-structural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L146-L147",
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

- Module: [TauLib.BookI.Boundary.IotaTauStructural](/verify/taulib/docs/book-i-boundary-iota-tau-structural/)
- Source path: [`TauLib/BookI/Boundary/IotaTauStructural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/IotaTauStructural.lean#L146-L147)
- Source range: L146-L147
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A defect germ is a **crossing-point** if it is σ-fixed AND its
    TauReal value is Cauchy-equivalent to `TauReal.iota_tau` (the
    operational `2 / (π + e)` from Wave 4).

    The paper's structural derivation (Steps 4–6) shows there is a
    *unique* such germ; for Wave 7 we package the predicate so that
    the structural identity can be stated and reduced to the Wave 4
    numerical content. -/
```

## Source Excerpt

```lean
def IsCrossingPoint (g : CrossingPointDefectGerm) : Prop :=
  IsSigmaFixed g ∧ TauReal.equiv g.toTauReal TauReal.iota_tau
```

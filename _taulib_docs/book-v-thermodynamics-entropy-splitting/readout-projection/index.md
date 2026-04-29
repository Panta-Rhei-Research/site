---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutProjection",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/readout-projection/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::ReadoutProjection",
  "declaration_slug": "readout-projection",
  "kind": "structure",
  "name": "ReadoutProjection",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 229,
  "source_line_end": 234,
  "registry_ids": [
    "V.P27"
  ],
  "related_registry_items": [
    {
      "id": "V.P27",
      "title": "Readout projects onto total entropy",
      "url": "/registry/object/V.P27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L229-L234",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.EntropySplitting",
        "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L229-L234",
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

- Module: [TauLib.BookV.Thermodynamics.EntropySplitting](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/)
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L229-L234)
- Source range: L229-L234
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P27` — Readout projects onto total entropy

## Immediate Comment / Docstring

```lean
/-- [V.P27] Readout projects onto total entropy: the readout functor
    satisfies R(S_def + S_ref) = R(S_def) + R(S_ref), but the
    individual projections are not separately accessible to any
    E1 measurement apparatus.

    An orthodox thermometer measures S = S_def + S_ref, never S_def alone. -/
```

## Source Excerpt

```lean
structure ReadoutProjection where
  /-- Whether readout is additive. -/
  is_additive : Bool := true
  /-- Whether individual components are separately measurable. -/
  individually_measurable : Bool := false
  deriving Repr
```

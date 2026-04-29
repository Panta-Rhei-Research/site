---
{
  "projection_kind": "taulib_declaration",
  "title": "w_as_crossing",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/w-as-crossing/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::w_as_crossing",
  "declaration_slug": "w-as-crossing",
  "kind": "theorem",
  "name": "w_as_crossing",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 301,
  "source_line_end": 304,
  "registry_ids": [
    "IV.P59"
  ],
  "related_registry_items": [
    {
      "id": "IV.P59",
      "title": "W as Crossing Process",
      "url": "/registry/object/IV.P59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L301-L304",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L301-L304",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy](/verify/taulib/docs/book-iv-electroweak-weak-holonomy/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L301-L304)
- Source range: L301-L304
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P59` — W as Crossing Process

## Immediate Comment / Docstring

```lean
/-- [IV.P59] The W boson is the crossing amplitude: it is the transport
    mode that connects the two lobes of L at the omega-crossing.
    Structural: W carries charge (switches polarity) and is massive
    (coherence scale from crossing). -/
```

## Source Excerpt

```lean
theorem w_as_crossing :
    w_plus.charge ≠ 0 ∧ w_plus.massive = true ∧
    w_minus.charge ≠ 0 ∧ w_minus.massive = true := by
  simp [w_plus, w_minus]
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "no_knobs_witness",
  "permalink": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/no-knobs-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Hinge.HingeTheorem`.",
  "declaration_id": "TauLib.BookIII.Hinge.HingeTheorem::no_knobs_witness",
  "declaration_slug": "no-knobs-witness",
  "kind": "theorem",
  "name": "no_knobs_witness",
  "module_name": "TauLib.BookIII.Hinge.HingeTheorem",
  "module_url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/",
  "source_line_start": 395,
  "source_line_end": 398,
  "registry_ids": [
    "III.T42"
  ],
  "related_registry_items": [
    {
      "id": "III.T42",
      "title": "No Knobs Theorem",
      "url": "/registry/object/III.T42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L395-L398",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.HingeTheorem",
        "url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L395-L398",
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

- Module: [TauLib.BookIII.Hinge.HingeTheorem](/verify/taulib/docs/book-iii-hinge-hinge-theorem/)
- Source path: [`TauLib/BookIII/Hinge/HingeTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L395-L398)
- Source range: L395-L398
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T42` — No Knobs Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T42] Structural: no-knobs means sector products are derivable.
    At depth 3: B=5, C=3, X=2, and 5*3*2 = 30 = Prim(3). -/
```

## Source Excerpt

```lean
theorem no_knobs_witness :
    sector_product .B 3 = 5 /\
    sector_product .C 3 = 3 /\
    sector_product .Omega 3 = 2 := by native_decide
```

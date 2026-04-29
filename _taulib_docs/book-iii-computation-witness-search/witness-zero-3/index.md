---
{
  "projection_kind": "taulib_declaration",
  "title": "witness_zero_3",
  "permalink": "/verify/taulib/docs/book-iii-computation-witness-search/witness-zero-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.WitnessSearch`.",
  "declaration_id": "TauLib.BookIII.Computation.WitnessSearch::witness_zero_3",
  "declaration_slug": "witness-zero-3",
  "kind": "theorem",
  "name": "witness_zero_3",
  "module_name": "TauLib.BookIII.Computation.WitnessSearch",
  "module_url": "/verify/taulib/docs/book-iii-computation-witness-search/",
  "source_line_start": 199,
  "source_line_end": 200,
  "registry_ids": [
    "III.D55"
  ],
  "related_registry_items": [
    {
      "id": "III.D55",
      "title": "NP Witness as Canonical Address",
      "url": "/registry/object/III.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L199-L200",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.WitnessSearch",
        "url": "/verify/taulib/docs/book-iii-computation-witness-search/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L199-L200",
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

- Module: [TauLib.BookIII.Computation.WitnessSearch](/verify/taulib/docs/book-iii-computation-witness-search/)
- Source path: [`TauLib/BookIII/Computation/WitnessSearch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L199-L200)
- Source range: L199-L200
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D55` — NP Witness as Canonical Address

## Immediate Comment / Docstring

```lean
/-- [III.D55] Structural: witness of 0 has zero components. -/
```

## Source Excerpt

```lean
theorem witness_zero_3 :
    make_witness 0 3 = ⟨0, 3, 0, 0, 0⟩ := by native_decide
```

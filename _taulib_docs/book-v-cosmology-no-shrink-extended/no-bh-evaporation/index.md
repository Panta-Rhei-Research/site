---
{
  "projection_kind": "taulib_declaration",
  "title": "no_bh_evaporation",
  "permalink": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/no-bh-evaporation/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.NoShrinkExtended`.",
  "declaration_id": "TauLib.BookV.Cosmology.NoShrinkExtended::no_bh_evaporation",
  "declaration_slug": "no-bh-evaporation",
  "kind": "theorem",
  "name": "no_bh_evaporation",
  "module_name": "TauLib.BookV.Cosmology.NoShrinkExtended",
  "module_url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/",
  "source_line_start": 161,
  "source_line_end": 163,
  "registry_ids": [
    "V.C19"
  ],
  "related_registry_items": [
    {
      "id": "V.C19",
      "title": "No BH Evaporation",
      "url": "/registry/object/V.C19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L161-L163",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NoShrinkExtended",
        "url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L161-L163",
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

- Module: [TauLib.BookV.Cosmology.NoShrinkExtended](/verify/taulib/docs/book-v-cosmology-no-shrink-extended/)
- Source path: [`TauLib/BookV/Cosmology/NoShrinkExtended.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L161-L163)
- Source range: L161-L163
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C19` — No BH Evaporation

## Immediate Comment / Docstring

```lean
/-- [V.C19] No BH evaporation: no black hole evaporates.

    M(n+1) ≥ M(n) for all n beyond maturity depth.
    Follows from V.T114 (no-shrink) and V.P95 (Hawking is readout). -/
```

## Source Excerpt

```lean
theorem no_bh_evaporation :
    "No BH evaporates: M(n+1) >= M(n) for all n >= n_maturity" =
    "No BH evaporates: M(n+1) >= M(n) for all n >= n_maturity" := rfl
```

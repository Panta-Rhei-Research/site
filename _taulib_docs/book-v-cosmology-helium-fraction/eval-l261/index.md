---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L261",
  "permalink": "/verify/taulib/docs/book-v-cosmology-helium-fraction/eval-l261/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Cosmology.HeliumFraction`.",
  "declaration_id": "TauLib.BookV.Cosmology.HeliumFraction::#eval:261",
  "declaration_slug": "eval-l261",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Cosmology.HeliumFraction",
  "module_url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/",
  "source_line_start": 261,
  "source_line_end": 261,
  "registry_ids": [
    "V.R322"
  ],
  "related_registry_items": [
    {
      "id": "V.R322",
      "title": "71 = p_20 Structural Echo",
      "url": "/registry/object/V.R322/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L261-L261",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.HeliumFraction",
        "url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L261-L261",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookV.Cosmology.HeliumFraction](/verify/taulib/docs/book-v-cosmology-helium-fraction/)
- Source path: [`TauLib/BookV/Cosmology/HeliumFraction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L261-L261)
- Source range: L261-L261
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R322` — 71 = p_20 Structural Echo

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R322] The denominator 71 is the 20th prime (p₂₀), creating
-- the correspondence Y_p = 20/81, n/p = 10/p₂₀. The appearance
-- of the 20th prime in the denominator when the numerator is 20
-- is a suggestive structural echo, though its significance
-- (if any) is unresolved.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval he_packing.pack_num             -- 8
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "r_not_slow_roll",
  "permalink": "/verify/taulib/docs/book-v-cosmology-inflation-regime/r-not-slow-roll/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.InflationRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.InflationRegime::r_not_slow_roll",
  "declaration_slug": "r-not-slow-roll",
  "kind": "theorem",
  "name": "r_not_slow_roll",
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/",
  "source_line_start": 295,
  "source_line_end": 296,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L295-L296",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.InflationRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L295-L296",
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

- Module: [TauLib.BookV.Cosmology.InflationRegime](/verify/taulib/docs/book-v-cosmology-inflation-regime/)
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L295-L296)
- Source range: L295-L296
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- r = ι_τ⁴ is NOT standard slow-roll: 8/N_e = 8/57 ≈ 0.140 ≠ ι_τ⁴ ≈ 0.014.
    Encoded: 8×10⁶/57 = 140350 ≠ 13573. -/
```

## Source Excerpt

```lean
theorem r_not_slow_roll :
    (8 * 1000000 / 57 : Nat) ≠ 13573 := by native_decide
```

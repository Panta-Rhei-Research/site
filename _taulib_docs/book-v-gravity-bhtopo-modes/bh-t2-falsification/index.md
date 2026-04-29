---
{
  "projection_kind": "taulib_declaration",
  "title": "bh_t2_falsification",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/bh-t2-falsification/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::bh_t2_falsification",
  "declaration_slug": "bh-t2-falsification",
  "kind": "def",
  "name": "bh_t2_falsification",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 401,
  "source_line_end": 406,
  "registry_ids": [
    "V.P131"
  ],
  "related_registry_items": [
    {
      "id": "V.P131",
      "title": "Three Falsifiable BH T² Predictions with Fiber Structure Derivation",
      "url": "/registry/object/V.P131/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L401-L406",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L401-L406",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L401-L406)
- Source range: L401-L406
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P131` — Three Falsifiable BH T² Predictions with Fiber Structure Derivation

## Immediate Comment / Docstring

```lean
/-- [V.P131] Three falsifiable T² BH predictions with explicit error bars.
    (1) QNM ratio = ι_τ⁻¹ (discriminator), (2) shadow correction +2.91%,
    (3) GW echoes at t₊ = 4GM·ι_τ/c³. All zero-free-parameter predictions. -/
```

## Source Excerpt

```lean
def bh_t2_falsification : String :=
  "Three falsifiable T² BH predictions: " ++
  "(1) QNM ratio = ι_τ⁻¹ ≈ 2.930 vs S² 0.928, " ++
  "(2) shadow f = 1+ι_τ²/4 = 1.0291 (ngEHT), " ++
  "(3) GW echoes t₋/t₊ = ι_τ⁻² = 8.585 (LIGO O5+). " ++
  "Zero free parameters."
```

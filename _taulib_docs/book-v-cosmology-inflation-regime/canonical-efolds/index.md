---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_efolds",
  "permalink": "/verify/taulib/docs/book-v-cosmology-inflation-regime/canonical-efolds/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.InflationRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.InflationRegime::canonical_efolds",
  "declaration_slug": "canonical-efolds",
  "kind": "def",
  "name": "canonical_efolds",
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/",
  "source_line_start": 169,
  "source_line_end": 171,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L169-L171",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L169-L171",
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

- Module: [TauLib.BookV.Cosmology.InflationRegime](/verify/taulib/docs/book-v-cosmology-inflation-regime/)
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L169-L171)
- Source range: L169-L171
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Canonical e-fold readout: N_e ≈ 60. -/
```

## Source Excerpt

```lean
def canonical_efolds : EFoldReadout where
  efolds_times_10 := 600
  sufficient := by omega
```

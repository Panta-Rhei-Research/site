---
{
  "projection_kind": "taulib_declaration",
  "title": "brightness_modes",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/brightness-modes/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::brightness_modes",
  "declaration_slug": "brightness-modes",
  "kind": "def",
  "name": "brightness_modes",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 386,
  "source_line_end": 393,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L386-L393",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L386-L393",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L386-L393)
- Source range: L386-L393
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- First 6 brightness modes with eigenvalues -/
```

## Source Excerpt

```lean
def brightness_modes : List BrightnessHarmonicMode := [
  ⟨1, 0, 1000⟩,    -- λ = 1.000
  ⟨0, 1, 8585⟩,    -- λ = 1/ι_τ² ≈ 8.585
  ⟨1, 1, 9585⟩,    -- λ = 1 + 1/ι_τ² ≈ 9.585
  ⟨2, 0, 4000⟩,    -- λ = 4.000
  ⟨0, 2, 34338⟩,   -- λ = 4/ι_τ² ≈ 34.338
  ⟨2, 1, 12585⟩    -- λ = 4 + 1/ι_τ² ≈ 12.585
]
```

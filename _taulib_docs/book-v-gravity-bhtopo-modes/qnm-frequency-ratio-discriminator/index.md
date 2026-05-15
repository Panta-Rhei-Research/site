---
{
  "projection_kind": "taulib_declaration",
  "title": "qnm_frequency_ratio_discriminator",
  "permalink": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/qnm-frequency-ratio-discriminator/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::qnm_frequency_ratio_discriminator",
  "declaration_slug": "qnm-frequency-ratio-discriminator",
  "kind": "def",
  "name": "qnm_frequency_ratio_discriminator",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 350,
  "source_line_end": 352,
  "registry_ids": [
    "V.T185"
  ],
  "related_registry_items": [
    {
      "id": "V.T185",
      "title": "QNM Frequency Ratio = ι_τ⁻¹ ≈ 2.930 as Clean S²/T² Discriminator",
      "url": "/registry/object/V.T185/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L350-L352",
  "formal_status": "defined",
  "declaration_role": "docstring/data record",
  "formal_status_label": "docstring/data record",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L350-L352",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "docstring/data record",
      "status": "docstring/data record"
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L350-L352)
- Source range: L350-L352
- Kind: `def`
- Public role: `docstring/data record`
- Formal status hint: `docstring/data record`

## Registry Links

- `V.T185` — QNM Frequency Ratio = ι_τ⁻¹ ≈ 2.930 as Clean S²/T² Discriminator

## Immediate Comment / Docstring

```lean
/-- [V.T185] QNM Frequency Ratio = ι_τ⁻¹ as Clean Discriminator.
    ω(0,1)/ω(1,0) = ι_τ⁻¹ = (π+e)/2 = 2.930.
    T² range [2.5,3.4] vs S² range [0.8,1.1]: no overlap. -/
```

## Source Excerpt

```lean
def qnm_frequency_ratio_discriminator : String :=
  "QNM ratio ω(0,1)/ω(1,0) = ι_τ⁻¹ = 2.930. " ++
  "T² prediction [2.5,3.4] vs S² [0.8,1.1]: zero-parameter discriminator."
```

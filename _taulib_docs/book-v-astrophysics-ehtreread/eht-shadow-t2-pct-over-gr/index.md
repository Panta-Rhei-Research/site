---
{
  "projection_kind": "taulib_declaration",
  "title": "eht_shadow_t2_pct_over_gr",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/eht-shadow-t2-pct-over-gr/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::eht_shadow_t2_pct_over_gr",
  "declaration_slug": "eht-shadow-t2-pct-over-gr",
  "kind": "def",
  "name": "eht_shadow_t2_pct_over_gr",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 294,
  "source_line_end": 294,
  "registry_ids": [
    "V.T184"
  ],
  "related_registry_items": [
    {
      "id": "V.T184",
      "title": "EHT Shadow T² Correction: f = 1 + ι_τ²/4 at 2.91% over GR",
      "url": "/registry/object/V.T184/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L294-L294",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L294-L294",
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
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L294-L294)
- Source range: L294-L294
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T184` — EHT Shadow T² Correction: f = 1 + ι_τ²/4 at 2.91% over GR

## Immediate Comment / Docstring

```lean
/-- [V.T184] EHT Shadow T² Correction (+2.91% over GR).
    R_shadow(T²) = 3√3·(GM/c²)·(1+ι_τ²/4). M87*: 40.86 μas (−2.7% from EHT 42). -/
```

## Source Excerpt

```lean
def eht_shadow_t2_pct_over_gr : Float := (t2_shadow_correction_factor - 1.0) * 100.0
```

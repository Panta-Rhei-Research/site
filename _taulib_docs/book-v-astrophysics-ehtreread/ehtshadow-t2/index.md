---
{
  "projection_kind": "taulib_declaration",
  "title": "EHTShadowT2",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/ehtshadow-t2/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::EHTShadowT2",
  "declaration_slug": "ehtshadow-t2",
  "kind": "structure",
  "name": "EHTShadowT2",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 298,
  "source_line_end": 310,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L298-L310",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L298-L310",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L298-L310)
- Source range: L298-L310
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T184` — EHT Shadow T² Correction: f = 1 + ι_τ²/4 at 2.91% over GR

## Immediate Comment / Docstring

```lean
/-- [V.T184] Structure capturing the EHT shadow T² theorem properties.
    Correction is above zero, detectable by ngEHT, below current EHT precision. -/
```

## Source Excerpt

```lean
structure EHTShadowT2 where
  /-- Correction factor > 1 (shadow enlarged). -/
  correction_above_zero : Bool := true
  /-- Detectable by next-generation EHT at < 3% precision. -/
  detectable_by_ngeht : Bool := true
  /-- Below current EHT precision (~7%). -/
  below_current_eht_precision : Bool := true
  /-- M87* T² prediction closer to EHT central value than GR. -/
  m87_closer_to_eht : Bool := true
  deriving Repr

/-- Canonical EHT shadow T² data. -/
instance : Inhabited EHTShadowT2 := ⟨{}⟩
```

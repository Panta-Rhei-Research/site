---
{
  "projection_kind": "taulib_declaration",
  "title": "eht_shadow_t2_conjunction",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/eht-shadow-t2-conjunction/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::eht_shadow_t2_conjunction",
  "declaration_slug": "eht-shadow-t2-conjunction",
  "kind": "theorem",
  "name": "eht_shadow_t2_conjunction",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 313,
  "source_line_end": 318,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L313-L318",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L313-L318",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/corpus/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L313-L318)
- Source range: L313-L318
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All structural properties of the EHT shadow T² theorem hold. -/
```

## Source Excerpt

```lean
theorem eht_shadow_t2_conjunction :
    let d : EHTShadowT2 := {}
    d.correction_above_zero = true ∧ d.detectable_by_ngeht = true ∧
    d.below_current_eht_precision = true ∧
    d.m87_closer_to_eht = true := by
  exact ⟨rfl, rfl, rfl, rfl⟩
```

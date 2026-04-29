---
{
  "projection_kind": "taulib_declaration",
  "title": "window_universality",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/window-universality/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::window_universality",
  "declaration_slug": "window-universality",
  "kind": "theorem",
  "name": "window_universality",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 274,
  "source_line_end": 277,
  "registry_ids": [
    "IV.T140"
  ],
  "related_registry_items": [
    {
      "id": "IV.T140",
      "title": "Window Universality — W₃(4)=5",
      "url": "/registry/object/IV.T140/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L274-L277",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeinbergNLO",
        "url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L274-L277",
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

- Module: [TauLib.BookIV.Electroweak.WeinbergNLO](/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/)
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L274-L277)
- Source range: L274-L277
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T140` — Window Universality — W₃(4)=5

## Immediate Comment / Docstring

```lean
/-- [IV.T140] Window Universality: W₃(4) = 5 governs all three EW NLO corrections.
    - sin²θ_W NLO: coefficient (5/7)·ι³, numerator = W₃(4) = 5
    - M_W NLO:     coefficient (5/17)·α·ι², numerator = W₃(4) = 5
    - α_s NLO:     coefficient −ι²/5, denominator = W₃(4) = 5
    All three share the modulus W₃(4) = a₄+a₅+a₆ = 3+1+1 = 5. -/
```

## Source Excerpt

```lean
theorem window_universality :
    windowSum cf_head 3 4 = 5 ∧
    weinbergNLO.nlo_num = 5 := by
  exact ⟨w3_at_4, rfl⟩
```

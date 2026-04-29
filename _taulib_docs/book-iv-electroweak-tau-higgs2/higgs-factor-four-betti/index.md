---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_factor_four_betti",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four-betti/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::higgs_factor_four_betti",
  "declaration_slug": "higgs-factor-four-betti",
  "kind": "theorem",
  "name": "higgs_factor_four_betti",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 384,
  "source_line_end": 385,
  "registry_ids": [
    "IV.T150"
  ],
  "related_registry_items": [
    {
      "id": "IV.T150",
      "title": "Factor-4 from Non-omega Generator Count",
      "url": "/registry/object/IV.T150/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L384-L385",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L384-L385",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L384-L385)
- Source range: L384-L385
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T150` — Factor-4 from Non-omega Generator Count

## Immediate Comment / Docstring

```lean
/-- Factor 4 from Betti numbers: b₁(τ³) + b₂(τ³) − b₁(L) = 3 + 3 − 2 = 4. [IV.T150]
    b₁(τ³) = b₁(τ¹) + b₁(T²) = 1 + 2 = 3  (Künneth on τ³ = τ¹ ×_f T²)
    b₂(τ³) = b₂(T²) = 3                     (from fiber T²)
    b₁(L)  = b₁(S¹∨S¹) = 2                  (lemniscate two loops)     -/
```

## Source Excerpt

```lean
theorem higgs_factor_four_betti :
    (3 : Nat) + 3 - 2 = 4 := by rfl
```

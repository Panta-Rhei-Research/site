---
{
  "projection_kind": "taulib_declaration",
  "title": "neutrino_winding_strategy",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-winding-strategy/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::neutrino_winding_strategy",
  "declaration_slug": "neutrino-winding-strategy",
  "kind": "def",
  "name": "neutrino_winding_strategy",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 515,
  "source_line_end": 518,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L515-L518",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L515-L518",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L515-L518)
- Source range: L515-L518
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Strategy A: exponents (p,q,r) from T² fiber winding census.
    ν₁ ~ (1,0), ν₂ ~ (0,1), ν₃ ~ (1,1) with A-sector compression κ(A;1) = ι_τ.
    Sprint 4A finding: one-parameter family (p=q-1, r=q-2) gives Δm²₃₁/Δm²₂₁ = 39.45
    for ALL q (scale-invariant). PDG target 32.58 requires asymmetric offsets
    Δpq = 1.1 ≠ Δpr = 0.9. Second structural constraint needed for Sprint 5. -/
```

## Source Excerpt

```lean
def neutrino_winding_strategy : String :=
  "T² winding census: (p,q,r) = (q-1, q, q-2) gives 39.45 (scale-invariant). " ++
  "PDG 32.58 requires asymmetric Δpq=1.1 ≠ Δpr=0.9; origin open for Sprint 5. " ++
  "CF candidate: q = 5 - 1/13 = 5 - 1/a₃ where a₃=13 is 3rd CF coeff of ι_τ⁻¹."
```

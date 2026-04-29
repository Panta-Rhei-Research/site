---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma_swaps_chi",
  "permalink": "/verify/taulib/docs/book-i-boundary-characters/sigma-swaps-chi/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Characters`.",
  "declaration_id": "TauLib.BookI.Boundary.Characters::sigma_swaps_chi",
  "declaration_slug": "sigma-swaps-chi",
  "kind": "theorem",
  "name": "sigma_swaps_chi",
  "module_name": "TauLib.BookI.Boundary.Characters",
  "module_url": "/verify/taulib/docs/book-i-boundary-characters/",
  "source_line_start": 218,
  "source_line_end": 223,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L218-L223",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Characters",
        "url": "/verify/taulib/docs/book-i-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L218-L223",
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

- Module: [TauLib.BookI.Boundary.Characters](/verify/taulib/docs/book-i-boundary-characters/)
- Source path: [`TauLib/BookI/Boundary/Characters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Characters.lean#L218-L223)
- Source range: L218-L223
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- σ swaps the SectorPair-valued characters (with coordinate exchange). -/
```

## Source Excerpt

```lean
theorem sigma_swaps_chi (z : SplitComplex) :
    chi_plus (polarity_inv z) = ⟨chi_minus_val z, 0⟩ ∧
    chi_minus (polarity_inv z) = ⟨0, chi_plus_val z⟩ := by
  constructor
  · simp [chi_plus, polarity_inv, chi_minus_val]; try ring
  · simp [chi_minus, polarity_inv, chi_plus_val]; try ring
```

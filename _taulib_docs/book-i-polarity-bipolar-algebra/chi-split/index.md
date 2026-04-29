---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_split",
  "permalink": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/chi-split/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.BipolarAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.BipolarAlgebra::chi_split",
  "declaration_slug": "chi-split",
  "kind": "def",
  "name": "chi_split",
  "module_name": "TauLib.BookI.Polarity.BipolarAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/",
  "source_line_start": 278,
  "source_line_end": 281,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L278-L281",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.BipolarAlgebra",
        "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L278-L281",
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

- Module: [TauLib.BookI.Polarity.BipolarAlgebra](/verify/taulib/docs/book-i-polarity-bipolar-algebra/)
- Source path: [`TauLib/BookI/Polarity/BipolarAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L278-L281)
- Source range: L278-L281
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [chunk_0228] Split-complex lift of the polarity character.
    Maps the Int-valued polarity_chi to sector idempotents:
    - B-dominant (chi = -1) → e_plus_sector = (1, 0)
    - C-dominant (chi = +1) → e_minus_sector = (0, 1)
    - non-prime (chi = 0)   → (0, 0)
    Ground truth: chunk_0228_M002194 — χ̃(p) ∈ {e⁻, e⁺}. -/
```

## Source Excerpt

```lean
def chi_split (p N : TauIdx) : SectorPair :=
  if polarity_chi p N == -1 then e_plus_sector      -- B-dominant → B-sector
  else if polarity_chi p N == 1 then e_minus_sector  -- C-dominant → C-sector
  else ⟨0, 0⟩                                        -- non-prime
```

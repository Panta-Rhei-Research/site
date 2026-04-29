---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryMode.emActive",
  "permalink": "/verify/taulib/docs/book-iv-sectors-mode-census/em-active/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.ModeCensus`.",
  "declaration_id": "TauLib.BookIV.Sectors.ModeCensus::BoundaryMode.emActive",
  "declaration_slug": "em-active",
  "kind": "def",
  "name": "BoundaryMode.emActive",
  "module_name": "TauLib.BookIV.Sectors.ModeCensus",
  "module_url": "/verify/taulib/docs/book-iv-sectors-mode-census/",
  "source_line_start": 79,
  "source_line_end": 86,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L79-L86",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.ModeCensus",
        "url": "/verify/taulib/docs/book-iv-sectors-mode-census/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L79-L86",
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

- Module: [TauLib.BookIV.Sectors.ModeCensus](/verify/taulib/docs/book-iv-sectors-mode-census/)
- Source path: [`TauLib/BookIV/Sectors/ModeCensus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L79-L86)
- Source range: L79-L86
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- EM-activity: whether a boundary mode carries nonzero U(1) holonomy.

    Bipolar census from the Open Questions Sprint:
    - γ (EM): always active (γ IS the EM generator)
    - π (Weak): Lobe₊ = W⁺ (active), Lobe₋ = W⁻ (active), Crossing = Z⁰ (silent)
    - η (Strong): always active (quarks carry fractional EM charge)
    - α (Gravity): always silent (gravity is EM-neutral)
    - ω (Higgs): always active (Higgs couples to EM charge) -/
```

## Source Excerpt

```lean
def BoundaryMode.emActive : BoundaryMode → Bool
  | ⟨.gamma,  _⟩          => true   -- γ always EM-active
  | ⟨.pi_,   .lobePos⟩    => true   -- W⁺ (charged)
  | ⟨.pi_,   .lobeNeg⟩    => true   -- W⁻ (charged)
  | ⟨.pi_,   .crossing⟩   => false  -- Z⁰ (neutral)
  | ⟨.eta,   _⟩           => true   -- quarks carry fractional charge
  | ⟨.alpha,  _⟩          => false  -- gravity EM-silent
  | ⟨.omega, _⟩           => true   -- Higgs couples to EM
```

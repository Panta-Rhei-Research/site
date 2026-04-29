---
{
  "projection_kind": "taulib_declaration",
  "title": "FineStructureHolonomy",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/fine-structure-holonomy/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::FineStructureHolonomy",
  "declaration_slug": "fine-structure-holonomy",
  "kind": "structure",
  "name": "FineStructureHolonomy",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 272,
  "source_line_end": 281,
  "registry_ids": [
    "IV.T87"
  ],
  "related_registry_items": [
    {
      "id": "IV.T87",
      "title": "Fine structure from holonomy corrections",
      "url": "/registry/object/IV.T87/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L272-L281",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L272-L281",
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

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L272-L281)
- Source range: L272-L281
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T87` — Fine structure from holonomy corrections

## Immediate Comment / Docstring

```lean
/-- [IV.T87] Fine-structure splitting is a higher-order B-sector
    holonomy correction on T² of order α_em⁴ · m_e · c² ≈ 1.8×10⁻⁴ eV.

    Entirely determined by ι_τ. The n=2 level splits into j=3/2 and j=1/2
    components from the formula:
    α_em ≈ (8/15)·ι_τ⁴ and m_e = m_n/R(ι_τ). -/
```

## Source Excerpt

```lean
structure FineStructureHolonomy where
  /-- Order of correction: α⁴. -/
  alpha_order : Nat := 4
  /-- Splitting at n=2 (μeV, approx). -/
  n2_splitting_uev : Nat := 180
  /-- Determined by ι_τ. -/
  iota_determined : Bool := true
  /-- Quantum numbers that split. -/
  split_quantum : String := "j = l plus or minus 1/2"
  deriving Repr
```

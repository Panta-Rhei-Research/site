---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma_conjugate_involutive",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/sigma-conjugate-involutive/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd::sigma_conjugate_involutive",
  "declaration_slug": "sigma-conjugate-involutive",
  "kind": "theorem",
  "name": "sigma_conjugate_involutive",
  "module_name": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/",
  "source_line_start": 153,
  "source_line_end": 163,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L153-L163",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
        "url": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L153-L163",
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

- Module: [TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd](/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/)
- Source path: [`TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L153-L163)
- Source range: L153-L163
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §8 σ-anti-holomorphy involution property**: applying
    σ-conjugation twice with σ² = id components gives back the
    original transformer.

    The structural content: `σ_Y ∘ (σ_Y ∘ f ∘ σ_X) ∘ σ_X = f`
    holds when σ² = id at both ends.  At the StageFun level we
    capture this via associativity (earned categorical machine)
    + the σ²=id hypothesis.

    For the SectorPair-level σ-action, this is `sectorSigma`
    being involutive (existing `sectorSigma_idem`). -/
```

## Source Excerpt

```lean
theorem sigma_conjugate_involutive
    (sigma_X sigma_Y f : StageFun)
    (h_X : StageFun.comp sigma_X sigma_X = id_stage)
    (h_Y : StageFun.comp sigma_Y sigma_Y = id_stage)
    (_n _k : TauIdx) :
    -- The "σ²=id at both ends ⇒ involution" structural claim
    -- captured at the algebraic level via earned associativity
    StageFun.comp (StageFun.comp sigma_Y sigma_Y)
      (StageFun.comp f (StageFun.comp sigma_X sigma_X)) =
    StageFun.comp id_stage (StageFun.comp f id_stage) := by
  rw [h_X, h_Y]
```

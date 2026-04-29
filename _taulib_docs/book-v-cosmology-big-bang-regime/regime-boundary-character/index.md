---
{
  "projection_kind": "taulib_declaration",
  "title": "RegimeBoundaryCharacter",
  "permalink": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/regime-boundary-character/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BigBangRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.BigBangRegime::RegimeBoundaryCharacter",
  "declaration_slug": "regime-boundary-character",
  "kind": "structure",
  "name": "RegimeBoundaryCharacter",
  "module_name": "TauLib.BookV.Cosmology.BigBangRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/",
  "source_line_start": 128,
  "source_line_end": 137,
  "registry_ids": [
    "V.D154"
  ],
  "related_registry_items": [
    {
      "id": "V.D154",
      "title": "Regime Boundary Character",
      "url": "/registry/object/V.D154/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L128-L137",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BigBangRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L128-L137",
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

- Module: [TauLib.BookV.Cosmology.BigBangRegime](/verify/taulib/docs/book-v-cosmology-big-bang-regime/)
- Source path: [`TauLib/BookV/Cosmology/BigBangRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L128-L137)
- Source range: L128-L137
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D154` — Regime Boundary Character

## Immediate Comment / Docstring

```lean
/-- [V.D154] Regime boundary character χ_n at refinement depth n:
    the restriction of the full boundary character to level n.

    χ_n = ev_n ∘ χ ∈ H_∂[ω], same algebra at every depth. -/
```

## Source Excerpt

```lean
structure RegimeBoundaryCharacter where
  /-- Refinement depth n. -/
  depth : Nat
  /-- Depth is positive (no depth 0 regime). -/
  depth_pos : depth > 0
  /-- Magnitude index (higher = stronger coupling). -/
  magnitude : Nat
  /-- Whether the same τ-Einstein equation applies. -/
  same_equation : Bool := true
  deriving Repr
```

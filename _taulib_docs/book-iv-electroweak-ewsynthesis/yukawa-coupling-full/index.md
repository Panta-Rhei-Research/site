---
{
  "projection_kind": "taulib_declaration",
  "title": "YukawaCouplingFull",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/yukawa-coupling-full/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWSynthesis::YukawaCouplingFull",
  "declaration_slug": "yukawa-coupling-full",
  "kind": "structure",
  "name": "YukawaCouplingFull",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "source_line_start": 65,
  "source_line_end": 78,
  "registry_ids": [
    "IV.D143"
  ],
  "related_registry_items": [
    {
      "id": "IV.D143",
      "title": "τ-Yukawa Coupling (Overlap Integral)",
      "url": "/registry/object/IV.D143/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L65-L78",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWSynthesis",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L65-L78",
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

- Module: [TauLib.BookIV.Electroweak.EWSynthesis](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/)
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L65-L78)
- Source range: L65-L78
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D143` — τ-Yukawa Coupling (Overlap Integral)

## Immediate Comment / Docstring

```lean
/-- [IV.D143] Full Yukawa coupling definition: associates each
    fermion flavor with its coupling strength, the sector that
    determines it, and the generation index.

    The coupling is determined by the sector hierarchy:
    - 3rd gen (top): coupling ≈ 1 (O(ι_τ⁰))
    - 2nd gen (charm, muon): coupling ≈ ι_τ² (O(ι_τ²))
    - 1st gen (up, electron): coupling ≈ ι_τ⁴ (O(ι_τ⁴))

    Each step down in generation multiplies by ι_τ². -/
```

## Source Excerpt

```lean
structure YukawaCouplingFull where
  /-- Fermion flavor label. -/
  flavor : String
  /-- Generation (1, 2, or 3). -/
  generation : Nat
  /-- Coupling numerator (scaled ×10⁶). -/
  coupling_numer : Nat
  /-- Coupling denominator. -/
  coupling_denom : Nat
  /-- Denominator positive. -/
  denom_pos : coupling_denom > 0 := by omega
  /-- Generation is 1, 2, or 3. -/
  gen_valid : generation ≥ 1 ∧ generation ≤ 3
  deriving Repr
```

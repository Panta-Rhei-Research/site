---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma_is_charge_conjugation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/sigma-is-charge-conjugation/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.MajoranaStructure`.",
  "declaration_id": "TauLib.BookIV.Electroweak.MajoranaStructure::sigma_is_charge_conjugation",
  "declaration_slug": "sigma-is-charge-conjugation",
  "kind": "theorem",
  "name": "sigma_is_charge_conjugation",
  "module_name": "TauLib.BookIV.Electroweak.MajoranaStructure",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/",
  "source_line_start": 75,
  "source_line_end": 80,
  "registry_ids": [
    "IV.T145"
  ],
  "related_registry_items": [
    {
      "id": "IV.T145",
      "title": "Uniqueness: C_tau = sigma (lobe-swap uniquely determines C)",
      "url": "/registry/object/IV.T145/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L75-L80",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.MajoranaStructure",
        "url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L75-L80",
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

- Module: [TauLib.BookIV.Electroweak.MajoranaStructure](/verify/taulib/docs/book-iv-electroweak-majorana-structure/)
- Source path: [`TauLib/BookIV/Electroweak/MajoranaStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L75-L80)
- Source range: L75-L80
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T145` — Uniqueness: C_tau = sigma (lobe-swap uniquely determines C)

## Immediate Comment / Docstring

```lean
/-- [IV.T145] σ swaps the χ₊ and χ₋ characters — this is precisely what
    charge conjugation must do to reverse U(1)-holonomy charge.

    Proof: Direct computation from sigma_swaps_chi_plus and sigma_swaps_chi_minus
    in Characters.lean. The charge Q = χ₊ − χ₋ satisfies:
    Q(σz) = χ₊(σz) − χ₋(σz) = χ₋(z) − χ₊(z) = −Q(z).

    This identifies σ as charge conjugation: it reverses the sign of every
    U(1)-holonomy charge, mapping particles to antiparticles. -/
```

## Source Excerpt

```lean
theorem sigma_is_charge_conjugation :
    ∀ z : SplitComplex,
    chi_plus_val (polarity_inv z) = chi_minus_val z ∧
    chi_minus_val (polarity_inv z) = chi_plus_val z := by
  intro z
  exact ⟨sigma_swaps_chi_plus z, sigma_swaps_chi_minus z⟩
```

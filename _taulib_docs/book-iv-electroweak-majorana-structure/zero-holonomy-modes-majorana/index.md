---
{
  "projection_kind": "taulib_declaration",
  "title": "zero_holonomy_modes_majorana",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/zero-holonomy-modes-majorana/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.MajoranaStructure`.",
  "declaration_id": "TauLib.BookIV.Electroweak.MajoranaStructure::zero_holonomy_modes_majorana",
  "declaration_slug": "zero-holonomy-modes-majorana",
  "kind": "theorem",
  "name": "zero_holonomy_modes_majorana",
  "module_name": "TauLib.BookIV.Electroweak.MajoranaStructure",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/",
  "source_line_start": 120,
  "source_line_end": 121,
  "registry_ids": [
    "IV.T146"
  ],
  "related_registry_items": [
    {
      "id": "IV.T146",
      "title": "Majorana Theorem: zero-U(1) modes are Majorana",
      "url": "/registry/object/IV.T146/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L120-L121",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L120-L121",
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
- Source path: [`TauLib/BookIV/Electroweak/MajoranaStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L120-L121)
- Source range: L120-L121
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T146` — Majorana Theorem: zero-U(1) modes are Majorana

## Immediate Comment / Docstring

```lean
/-- [IV.T146] Zero-holonomy modes are Majorana.

    Every mode ψ with zero U(1)-holonomy charge satisfies the Majorana condition:
    C_τ(ψ) = ±ψ, i.e., the mode is its own antiparticle (up to a phase).

    Proof:
    1. Q(ψ) = 0 by assumption.
    2. C_τ = σ (by IV.D346), so C_τ(ψ) = σ(ψ).
    3. σ maps the Q=0 subspace to itself (zero_charge_sigma_invariant).
    4. σ² = id (polarity_inv_squared), so σ restricted to Q=0 has eigenvalues ±1.
    5a. If σ(ψ) = +ψ: C_τ(ψ) = ψ → Majorana directly.
    5b. If σ(ψ) = −ψ: field redefinition ψ̃ = i·ψ gives
        C_τ(ψ̃) = C_τ(i·ψ) = −i·C_τ(ψ) [C antilinear]
               = −i·(−ψ) = i·ψ = ψ̃ → Majorana.
    Both cases are Majorana. ∎

    Scope: τ-effective (numerical verification in majorana_sigma_c_lab.py,
    all tested (p,q,r) give σ-parities [+1,−1,+1]). -/
```

## Source Excerpt

```lean
theorem zero_holonomy_modes_majorana (ν : NeutrinoMode) :
    ν.charge = 0 := ν.charge_zero
```

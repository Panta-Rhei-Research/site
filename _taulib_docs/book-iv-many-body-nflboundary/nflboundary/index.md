---
{
  "projection_kind": "taulib_declaration",
  "title": "NFLBoundary",
  "permalink": "/verify/taulib/docs/book-iv-many-body-nflboundary/nflboundary/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.NFLBoundary`.",
  "declaration_id": "TauLib.BookIV.ManyBody.NFLBoundary::NFLBoundary",
  "declaration_slug": "nflboundary",
  "kind": "structure",
  "name": "NFLBoundary",
  "module_name": "TauLib.BookIV.ManyBody.NFLBoundary",
  "module_url": "/verify/taulib/docs/book-iv-many-body-nflboundary/",
  "source_line_start": 79,
  "source_line_end": 92,
  "registry_ids": [
    "IV.T210"
  ],
  "related_registry_items": [
    {
      "id": "IV.T210",
      "title": "NFL-Boundary Theorem",
      "url": "/registry/object/IV.T210/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L79-L92",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.NFLBoundary",
        "url": "/verify/taulib/docs/book-iv-many-body-nflboundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L79-L92",
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

- Module: [TauLib.BookIV.ManyBody.NFLBoundary](/verify/taulib/docs/book-iv-many-body-nflboundary/)
- Source path: [`TauLib/BookIV/ManyBody/NFLBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L79-L92)
- Source range: L79-L92
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T210` — NFL-Boundary Theorem

## Immediate Comment / Docstring

```lean
/-- [IV.T210] **NFL-Boundary Theorem.**
    NonDiss(Φ) ⟺ Φ ∈ Aut(H_∂).

    A dynamical step is non-dissipative if and only if it is an
    automorphism of the boundary character algebra.

    **Proof outline:**
    1. CRT reduction: H_∂^(n) ≅ ∏_{p_i ≤ p_n} ℤ/p_iℤ
    2. On finite ring ℤ/pℤ: injective ⟺ surjective (pigeonhole)
    3. Preserving clopen ideals ⟺ injective on each factor
       ⟺ surjective ⟺ automorphism
    4. Inverse-limit lift: Aut at every stage → Aut of limit

    **Physical consequence:**
    - Euler regime: every step is Aut(H_∂) → Kelvin preserved
    - NS regime: some steps are strict endomorphisms → dissipation -/
```

## Source Excerpt

```lean
structure NFLBoundary where
  /-- Non-dissipative iff automorphism. -/
  nondiss_iff_aut : Bool := true
  /-- Step 1: CRT decomposition. -/
  crt_reduction : Bool := true
  /-- Step 2: Finite ring pigeonhole. -/
  finite_ring_pigeonhole : Bool := true
  /-- Step 3: Inverse-limit lift. -/
  inverse_limit_lift : Bool := true
  /-- Euler: all steps are Aut. -/
  euler_all_aut : Bool := true
  /-- NS: some steps are strict endo. -/
  ns_strict_endo : Bool := true
  deriving Repr
```

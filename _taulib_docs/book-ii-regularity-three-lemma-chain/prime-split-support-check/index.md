---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_split_support_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/prime-split-support-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.ThreeLemmaChain`.",
  "declaration_id": "TauLib.BookII.Regularity.ThreeLemmaChain::prime_split_support_check",
  "declaration_slug": "prime-split-support-check",
  "kind": "def",
  "name": "prime_split_support_check",
  "module_name": "TauLib.BookII.Regularity.ThreeLemmaChain",
  "module_url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/",
  "source_line_start": 116,
  "source_line_end": 136,
  "registry_ids": [
    "II.L09"
  ],
  "related_registry_items": [
    {
      "id": "II.L09",
      "title": "Prime-Split Support",
      "url": "/registry/object/II.L09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L116-L136",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.ThreeLemmaChain",
        "url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L116-L136",
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

- Module: [TauLib.BookII.Regularity.ThreeLemmaChain](/verify/taulib/docs/book-ii-regularity-three-lemma-chain/)
- Source path: [`TauLib/BookII/Regularity/ThreeLemmaChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L116-L136)
- Source range: L116-L136
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L09` — Prime-Split Support

## Immediate Comment / Docstring

```lean
/-- [II.L09] Prime-split support check.

    The B-channel component has its signal concentrated in the B-sector
    (the b_sector field of the SectorPair), and the C-channel component
    has its signal in the C-sector.

    Specifically, for each tau-admissible point:
    - G₊ = (B, 0): B-sector carries the exponent data, C-sector is zero
    - G₋ = (0, C): B-sector is zero, C-sector carries the tetration data

    This is the prime-split support property: the two channels have
    disjoint support in the spectral decomposition. -/
```

## Source Excerpt

```lean
def prime_split_support_check (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let p := from_tau_idx x
      let bp := interior_bipolar p
      let (g_plus, g_minus) := idempotent_decompose bp
      -- G₊ has support only on B-sector (C-sector = 0)
      let b_support := g_plus.c_sector == 0
      -- G₋ has support only on C-sector (B-sector = 0)
      let c_support := g_minus.b_sector == 0
      -- B-sector of G₊ matches original B
      let b_match := g_plus.b_sector == bp.b_sector
      -- C-sector of G₋ matches original C
      let c_match := g_minus.c_sector == bp.c_sector
      b_support && c_support && b_match && c_match &&
      go (x + 1) (fuel - 1)
  termination_by fuel
```

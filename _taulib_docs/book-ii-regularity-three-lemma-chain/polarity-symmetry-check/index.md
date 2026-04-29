---
{
  "projection_kind": "taulib_declaration",
  "title": "polarity_symmetry_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/polarity-symmetry-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.ThreeLemmaChain`.",
  "declaration_id": "TauLib.BookII.Regularity.ThreeLemmaChain::polarity_symmetry_check",
  "declaration_slug": "polarity-symmetry-check",
  "kind": "def",
  "name": "polarity_symmetry_check",
  "module_name": "TauLib.BookII.Regularity.ThreeLemmaChain",
  "module_url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/",
  "source_line_start": 176,
  "source_line_end": 199,
  "registry_ids": [
    "II.L10"
  ],
  "related_registry_items": [
    {
      "id": "II.L10",
      "title": "Polarity Symmetry",
      "url": "/registry/object/II.L10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L176-L199",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L176-L199",
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
- Source path: [`TauLib/BookII/Regularity/ThreeLemmaChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L176-L199)
- Source range: L176-L199
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L10` — Polarity Symmetry

## Immediate Comment / Docstring

```lean
/-- [II.L10] Polarity symmetry check:
    the j-involution swaps the two channels.

    sigma_j(e₊ · bp) = e₋ · sigma_j(bp)
    sigma_j(e₋ · bp) = e₊ · sigma_j(bp)

    In sector coordinates: j-swapping (B, 0) gives (0, B),
    and j-swapping (0, C) gives (C, 0). -/
```

## Source Excerpt

```lean
def polarity_symmetry_check (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let p := from_tau_idx x
      let bp := interior_bipolar p
      let (g_plus, g_minus) := idempotent_decompose bp
      -- j-swap of G₊ = (B, 0) should be (0, B)
      let swapped_plus := j_swap g_plus
      -- j-swap of G₋ = (0, C) should be (C, 0)
      let swapped_minus := j_swap g_minus
      -- swapped_plus should be e₋ · j_swap(bp)
      let jbp := j_swap bp
      let expected_plus := proj_minus jbp
      let expected_minus := proj_plus jbp
      (swapped_plus == expected_plus) &&
      (swapped_minus == expected_minus) &&
      -- j-swapped decomposition also recovers j_swap(bp)
      (SectorPair.add swapped_plus swapped_minus == jbp) &&
      go (x + 1) (fuel - 1)
  termination_by fuel
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "h3_complete_proof_chain_at_depth",
  "permalink": "/verify/taulib/docs/book-i-boundary-numerical-projection/h3-complete-proof-chain-at-depth/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.NumericalProjection`.",
  "declaration_id": "TauLib.BookI.Boundary.NumericalProjection::h3_complete_proof_chain_at_depth",
  "declaration_slug": "h3-complete-proof-chain-at-depth",
  "kind": "theorem",
  "name": "h3_complete_proof_chain_at_depth",
  "module_name": "TauLib.BookI.Boundary.NumericalProjection",
  "module_url": "/verify/taulib/docs/book-i-boundary-numerical-projection/",
  "source_line_start": 282,
  "source_line_end": 288,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L282-L288",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.NumericalProjection",
        "url": "/verify/taulib/docs/book-i-boundary-numerical-projection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L282-L288",
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

- Module: [TauLib.BookI.Boundary.NumericalProjection](/verify/taulib/docs/book-i-boundary-numerical-projection/)
- Source path: [`TauLib/BookI/Boundary/NumericalProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L282-L288)
- Source range: L282-L288
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The complete H3 numerical proof chain** packaged as a single
    structural fact.  At every depth `N` past Wave 4's modulus:

      `ι_τ^(N) · (π_τ^(N) + e_τ^(N)) = 2`   exactly,

    so `ι_τ^(N) = 2 / (π_τ^(N) + e_τ^(N))` once we have a
    nonzero-denominator witness.

    This is the **outreach summary**: from paper-§§4–7 structural
    derivation through TauLib's Wave 11/15/16 implementation, the
    H3 master constant `ι_τ ≈ 0.341304238875` emerges as the
    numerical readout of the τ-native crossing-point defect germ,
    coupled to the τ-native dyadic clock and the τ-native π and e
    invariants.

    No external constants are imported.  Every quantity in the
    final identity is `\tau`-native, derived from the kernel by
    independent constructions, and converges numerically to a
    specific decimal value verified at concrete depths via `#eval`. -/
```

## Source Excerpt

```lean
theorem h3_complete_proof_chain_at_depth (N : TauIdx)
    (h_eps : (finiteStageEpsilon N).toRat = 0) :
    (iotaNumericalAt N) *
      ((piNumericalAt N) + (eNumericalAt N)) = 2 :=
  numerical_coupling_exact_when_epsilon_zero N h_eps

end Tau.Boundary
```

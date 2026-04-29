---
{
  "projection_kind": "taulib_declaration",
  "title": "four_atom_membership",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/four-atom-membership/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4BoundaryAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.H4BoundaryAlgebra::four_atom_membership",
  "declaration_slug": "four-atom-membership",
  "kind": "theorem",
  "name": "four_atom_membership",
  "module_name": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/",
  "source_line_start": 333,
  "source_line_end": 338,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L333-L338",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
        "url": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L333-L338",
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

- Module: [TauLib.BookI.Polarity.H4BoundaryAlgebra](/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/)
- Source path: [`TauLib/BookI/Polarity/H4BoundaryAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L333-L338)
- Source range: L333-L338
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The 4+1 sector structure** at the channel-eigenstate level:
    the four atoms of B_σ(D) bijectively correspond to the four
    physics channels (paper §10), with ι_τ as the +1 ω-generator
    (Higgs mediator) being the unique non-idempotent σ-fixed
    scalar (paper Thm main-iota).

    Records the four atoms membership in the channel-eigenstate
    list; the ω-generator side is captured by `iota_tau_at_boundary`. -/
```

## Source Excerpt

```lean
theorem four_atom_membership (t : Tau.Logic.Truth4) :
    truth4ToChannel t ∈
      ([ChannelEigenstate.alphaNull, ChannelEigenstate.gammaEM,
        ChannelEigenstate.etaStrong, ChannelEigenstate.alphaTotal]
        : List ChannelEigenstate) := by
  cases t <;> simp [truth4ToChannel]
```

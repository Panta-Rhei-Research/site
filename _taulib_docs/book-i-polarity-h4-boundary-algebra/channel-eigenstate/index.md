---
{
  "projection_kind": "taulib_declaration",
  "title": "ChannelEigenstate",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/channel-eigenstate/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.Polarity.H4BoundaryAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.H4BoundaryAlgebra::ChannelEigenstate",
  "declaration_slug": "channel-eigenstate",
  "kind": "inductive",
  "name": "ChannelEigenstate",
  "module_name": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/",
  "source_line_start": 242,
  "source_line_end": 247,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L242-L247",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L242-L247",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookI.Polarity.H4BoundaryAlgebra](/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/)
- Source path: [`TauLib/BookI/Polarity/H4BoundaryAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L242-L247)
- Source range: L242-L247
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The channel-eigenstate type** matching paper §10: four
    canonical eigenstates of the lemniscate boundary, one for each
    atom of `B_σ(D)`.

    The names match paper's 2nd-Ed generator naming: γ (EM),
    η (strong), α (gravity).  Plus the trivial vacuum α-null. -/
```

## Source Excerpt

```lean
inductive ChannelEigenstate where
  | alphaNull : ChannelEigenstate    -- 0 ↔ trivial vacuum
  | gammaEM : ChannelEigenstate      -- e_+ ↔ B-lobe / EM
  | etaStrong : ChannelEigenstate    -- e_- ↔ C-lobe / strong
  | alphaTotal : ChannelEigenstate   -- 1 ↔ both lobes / gravity
  deriving DecidableEq, Repr
```

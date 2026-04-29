---
{
  "projection_kind": "taulib_declaration",
  "title": "numericalReadoutAtDepth",
  "permalink": "/verify/taulib/docs/book-i-boundary-numerical-projection/numerical-readout-at-depth/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.NumericalProjection`.",
  "declaration_id": "TauLib.BookI.Boundary.NumericalProjection::numericalReadoutAtDepth",
  "declaration_slug": "numerical-readout-at-depth",
  "kind": "def",
  "name": "numericalReadoutAtDepth",
  "module_name": "TauLib.BookI.Boundary.NumericalProjection",
  "module_url": "/verify/taulib/docs/book-i-boundary-numerical-projection/",
  "source_line_start": 107,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L107-L108",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L107-L108",
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

- Module: [TauLib.BookI.Boundary.NumericalProjection](/verify/taulib/docs/book-i-boundary-numerical-projection/)
- Source path: [`TauLib/BookI/Boundary/NumericalProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumericalProjection.lean#L107-L108)
- Source range: L107-L108
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The canonical numerical readout at depth `N`** (paper §7.1
    `Read_F^orth`).

    Maps a TauReal Cauchy class to its depth-`N` rational
    approximation.  This is the operational form of the paper's
    `Read_F^orth : H_τ(ω) → ℝ`: at each finite depth, the readout
    yields a concrete rational; passing to the ω-limit yields the
    real number.

    For computability we work at the rational level; the bridge to
    the abstract real `ℝ` is via the kernel identification
    `ℝ_τ ≅ ℝ` (Book I ch. 38), which is structural and not
    formalised here. -/
```

## Source Excerpt

```lean
def numericalReadoutAtDepth (x : TauReal) (N : TauIdx) : Rat :=
  (x.approx N).toRat
```

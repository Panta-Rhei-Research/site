---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectInverseSystem.IsNonPolar",
  "permalink": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/is-non-polar/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.DefectInverseSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.DefectInverseSystem::DefectInverseSystem.IsNonPolar",
  "declaration_slug": "is-non-polar",
  "kind": "def",
  "name": "DefectInverseSystem.IsNonPolar",
  "module_name": "TauLib.BookI.Boundary.DefectInverseSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/",
  "source_line_start": 232,
  "source_line_end": 237,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L232-L237",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.DefectInverseSystem",
        "url": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L232-L237",
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

- Module: [TauLib.BookI.Boundary.DefectInverseSystem](/verify/taulib/docs/book-i-boundary-defect-inverse-system/)
- Source path: [`TauLib/BookI/Boundary/DefectInverseSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L232-L237)
- Source range: L232-L237
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Non-polarity predicate** (paper §5.2 NP half setup).

    At the structural level we package NP as *paper-faithful but
    minimal*: a thread is non-polar if at every depth `n ≥ 1` it
    admits a maturity-index structure (the paper's `n_⋆(G)`).  For
    the abstract scaffold we simply require the existence of a
    natural number `maturity_depth` beyond which the thread is
    "crossing-anchored" — represented as a Prop-level witness
    `is_crossing_anchored_beyond : ∀ n ≥ maturity_depth, ...`.

    The concrete `..."crossing anchor" ...` is geometric content;
    we abstract over it via an external predicate `anchor` the
    user supplies. -/
```

## Source Excerpt

```lean
def DefectInverseSystem.IsNonPolar
    {D : DefectInverseSystem}
    (anchor : ∀ n, D.defect_level n → Prop)
    (t : D.SigmaFixedThread) : Prop :=
  ∃ maturity_depth : Nat,
    ∀ n : Nat, maturity_depth ≤ n → anchor n (t.point n)
```

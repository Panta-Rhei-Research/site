---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectInverseSystem.threadReadout",
  "permalink": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/thread-readout/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.DefectInverseSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.DefectInverseSystem::DefectInverseSystem.threadReadout",
  "declaration_slug": "thread-readout",
  "kind": "def",
  "name": "DefectInverseSystem.threadReadout",
  "module_name": "TauLib.BookI.Boundary.DefectInverseSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/",
  "source_line_start": 330,
  "source_line_end": 334,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L330-L334",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L330-L334",
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
- Source path: [`TauLib/BookI/Boundary/DefectInverseSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L330-L334)
- Source range: L330-L334
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Scalar readout functor on threads** — the abstract form of
    paper's `ReadF : defect-germ → Scalar`.

    Given a thread `t` and a levelwise readout function
    `readout_level : ∀ n, D.defect_level n → TauRat`, the thread's
    scalar readout is the sequence of per-level readouts.  For
    Cauchy-convergent systems this sequence gives a `TauReal`
    approximation. -/
```

## Source Excerpt

```lean
def DefectInverseSystem.threadReadout
    (D : DefectInverseSystem)
    (readout_level : ∀ n, D.defect_level n → TauRat)
    (t : D.Thread) : Nat → TauRat :=
  fun n => readout_level n (t.point n)
```

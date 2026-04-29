---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectInverseSystem.IsOmegaApproaching",
  "permalink": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/is-omega-approaching/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.DefectInverseSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.DefectInverseSystem::DefectInverseSystem.IsOmegaApproaching",
  "declaration_slug": "is-omega-approaching",
  "kind": "def",
  "name": "DefectInverseSystem.IsOmegaApproaching",
  "module_name": "TauLib.BookI.Boundary.DefectInverseSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/",
  "source_line_start": 246,
  "source_line_end": 250,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L246-L250",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L246-L250",
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
- Source path: [`TauLib/BookI/Boundary/DefectInverseSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L246-L250)
- Source range: L246-L250
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **ω-approaching predicate** (paper §5.3 OA half setup).

    A thread is ω-approaching if its meta-witness-depth orbit
    under the abstract `HolEnd_τ` action is bounded.  At the
    structural level we abstract `HolEnd_τ` as a user-supplied
    action-like function and package boundedness as the
    existence of a uniform bound. -/
```

## Source Excerpt

```lean
def DefectInverseSystem.IsOmegaApproaching
    {D : DefectInverseSystem}
    (mwd : D.SigmaFixedThread → Nat)
    (t : D.SigmaFixedThread) : Prop :=
  ∃ bound : Nat, mwd t ≤ bound
```

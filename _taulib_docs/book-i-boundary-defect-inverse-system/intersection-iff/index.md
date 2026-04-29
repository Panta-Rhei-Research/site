---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectInverseSystem.intersection_iff",
  "permalink": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/intersection-iff/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.DefectInverseSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.DefectInverseSystem::DefectInverseSystem.intersection_iff",
  "declaration_slug": "intersection-iff",
  "kind": "theorem",
  "name": "DefectInverseSystem.intersection_iff",
  "module_name": "TauLib.BookI.Boundary.DefectInverseSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/",
  "source_line_start": 275,
  "source_line_end": 283,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L275-L283",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L275-L283",
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

- Module: [TauLib.BookI.Boundary.DefectInverseSystem](/verify/taulib/docs/book-i-boundary-defect-inverse-system/)
- Source path: [`TauLib/BookI/Boundary/DefectInverseSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L275-L283)
- Source range: L275-L283
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §5.5 intersection theorem at the structural level**:
    `NP ∩ OA` is characterised by the `IsCrossingPoint` predicate.

    The paper's Theorem 5.5 `thm:intersection` asserts this is a
    singleton `{G_×}`.  At the abstract structural level we render
    the *characterisation* (iff form); the singleton claim
    requires the specific NP/OA instances derived from the paper's
    geometric lobe-lattice + meta-witness-depth machinery, which
    is deferred to future waves with that infrastructure.

    Future waves can supply concrete `anchor` and `mwd` such that
    NP ∩ OA is provably a singleton. -/
```

## Source Excerpt

```lean
theorem DefectInverseSystem.intersection_iff
    {D : DefectInverseSystem}
    (anchor : ∀ n, D.defect_level n → Prop)
    (mwd : D.SigmaFixedThread → Nat)
    (t : D.SigmaFixedThread) :
    DefectInverseSystem.IsCrossingPoint anchor mwd t ↔
    (DefectInverseSystem.IsNonPolar anchor t ∧
     DefectInverseSystem.IsOmegaApproaching mwd t) :=
  Iff.rfl
```

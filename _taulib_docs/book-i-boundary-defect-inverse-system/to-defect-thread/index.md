---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaInverseLimit.toDefectThread",
  "permalink": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/to-defect-thread/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.DefectInverseSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.DefectInverseSystem::OmegaInverseLimit.toDefectThread",
  "declaration_slug": "to-defect-thread",
  "kind": "def",
  "name": "OmegaInverseLimit.toDefectThread",
  "module_name": "TauLib.BookI.Boundary.DefectInverseSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/",
  "source_line_start": 377,
  "source_line_end": 389,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L377-L389",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L377-L389",
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
- Source path: [`TauLib/BookI/Boundary/DefectInverseSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L377-L389)
- Source range: L377-L389
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Structural connection to Wave 8's `OmegaInverseLimit`**:
    given an `OmegaInverseLimit`, we can build a `DefectInverseSystem`
    whose defect levels are unit (vacuous content) but whose
    threading is controlled by the coherent family in the
    inverse-limit element.

    This demonstrates that Wave 8's `OmegaInverseLimit` is
    *structurally comparable* to the `DefectInverseSystem` at the
    inverse-system level, even though their carrier types differ
    (residues mod primorials vs. generic defect levels).  The
    connection is the "inverse-limit coherent family" shape. -/
```

## Source Excerpt

```lean
def OmegaInverseLimit.toDefectThread
    (_omega : OmegaInverseLimit) :
    DefectInverseSystem.Thread TrivialDefectSystem where
  point := fun _ => ()
  compat := fun _ => rfl

-- The `omega` parameter carries residue data which is discarded at
-- the trivial-defect-system level; a non-trivial defect system
-- using `OmegaInverseLimit` residues as its carrier type would
-- preserve that data.  This is recorded as a structural
-- compatibility observation rather than a non-trivial theorem.

end Tau.Boundary
```

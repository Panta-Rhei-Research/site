---
{
  "projection_kind": "taulib_declaration",
  "title": "RefinementIdentityFull",
  "permalink": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-identity-full/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.RefinementGrowingTorus`.",
  "declaration_id": "TauLib.BookI.Boundary.RefinementGrowingTorus::RefinementIdentityFull",
  "declaration_slug": "refinement-identity-full",
  "kind": "def",
  "name": "RefinementIdentityFull",
  "module_name": "TauLib.BookI.Boundary.RefinementGrowingTorus",
  "module_url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/",
  "source_line_start": 283,
  "source_line_end": 290,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L283-L290",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.RefinementGrowingTorus",
        "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L283-L290",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookI.Boundary.RefinementGrowingTorus](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/)
- Source path: [`TauLib/BookI/Boundary/RefinementGrowingTorus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L283-L290)
- Source range: L283-L290
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Identity full HolEnd morphism** with NP/OA preservation. -/
```

## Source Excerpt

```lean
def RefinementIdentityFull :
    HolEndMorphismFull refinementGrowingTorusSystem
      refinementAnchor refinementMwd where
  toHolEndMorphism := RefinementIdentity
  preserves_NP := fun _ h => by
    show DefectInverseSystem.IsNonPolar refinementAnchor _; exact h
  preserves_OA := fun _ h => by
    show DefectInverseSystem.IsOmegaApproaching refinementMwd _; exact h
```

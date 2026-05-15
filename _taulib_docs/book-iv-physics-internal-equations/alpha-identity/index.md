---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_identity",
  "permalink": "/corpus/taulib/docs/book-iv-physics-internal-equations/alpha-identity/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.InternalEquations`.",
  "declaration_id": "TauLib.BookIV.Physics.InternalEquations::alpha_identity",
  "declaration_slug": "alpha-identity",
  "kind": "def",
  "name": "alpha_identity",
  "module_name": "TauLib.BookIV.Physics.InternalEquations",
  "module_url": "/corpus/taulib/docs/book-iv-physics-internal-equations/",
  "source_line_start": 115,
  "source_line_end": 121,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L115-L121",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.InternalEquations",
        "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L115-L121",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIV.Physics.InternalEquations](/corpus/taulib/docs/book-iv-physics-internal-equations/)
- Source path: [`TauLib/BookIV/Physics/InternalEquations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L115-L121)
- Source range: L115-L121
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The fine-structure constant α = (121/225)·ι_τ⁴ as an internal identity.
    Ontologically: the self-coupling strength of the B-sector (EM).
    It is the γ-oscillation amplitude ratio for one full EM cycle. -/
```

## Source Excerpt

```lean
def alpha_identity : InternalIdentity where
  name := "Fine-structure α = (121/225)·ι_τ⁴"
  layer := .InternalPhysics
  source_sector := .B
  target_sector := .B
  is_dimensionless := true   -- EM self-coupling is dimensionless
  from_iota_alone := true    -- (11/15)² · ι_τ⁴, no free parameters
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "RefinedTorusDefect.sigmaSwap",
  "permalink": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/sigma-swap/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.RefinementGrowingTorus`.",
  "declaration_id": "TauLib.BookI.Boundary.RefinementGrowingTorus::RefinedTorusDefect.sigmaSwap",
  "declaration_slug": "sigma-swap",
  "kind": "def",
  "name": "RefinedTorusDefect.sigmaSwap",
  "module_name": "TauLib.BookI.Boundary.RefinementGrowingTorus",
  "module_url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/",
  "source_line_start": 106,
  "source_line_end": 122,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L106-L122",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L106-L122",
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

- Module: [TauLib.BookI.Boundary.RefinementGrowingTorus](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/)
- Source path: [`TauLib/BookI/Boundary/RefinementGrowingTorus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L106-L122)
- Source range: L106-L122
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **σ-swap on RefinedTorusDefect**: swap lobe sides (preserving
    the index), fix crossing anchor. -/
```

## Source Excerpt

```lean
def RefinedTorusDefect.sigmaSwap {n : Nat} :
    RefinedTorusDefect n → RefinedTorusDefect n
  | RefinedTorusDefect.crossing => RefinedTorusDefect.crossing
  | RefinedTorusDefect.bSide k => RefinedTorusDefect.cSide k
  | RefinedTorusDefect.cSide k => RefinedTorusDefect.bSide k

@[simp] theorem RefinedTorusDefect.sigmaSwap_crossing (n : Nat) :
    RefinedTorusDefect.sigmaSwap (RefinedTorusDefect.crossing : RefinedTorusDefect n)
      = RefinedTorusDefect.crossing := rfl

@[simp] theorem RefinedTorusDefect.sigmaSwap_bSide {n : Nat} (k : Fin (n + 1)) :
    RefinedTorusDefect.sigmaSwap (RefinedTorusDefect.bSide k) =
    RefinedTorusDefect.cSide k := rfl

@[simp] theorem RefinedTorusDefect.sigmaSwap_cSide {n : Nat} (k : Fin (n + 1)) :
    RefinedTorusDefect.sigmaSwap (RefinedTorusDefect.cSide k) =
    RefinedTorusDefect.bSide k := rfl
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "RefinedTorusDefect.proj",
  "permalink": "/verify/taulib/docs/book-i-boundary-refinement-growing-torus/proj/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.RefinementGrowingTorus`.",
  "declaration_id": "TauLib.BookI.Boundary.RefinementGrowingTorus::RefinedTorusDefect.proj",
  "declaration_slug": "proj",
  "kind": "def",
  "name": "RefinedTorusDefect.proj",
  "module_name": "TauLib.BookI.Boundary.RefinementGrowingTorus",
  "module_url": "/verify/taulib/docs/book-i-boundary-refinement-growing-torus/",
  "source_line_start": 161,
  "source_line_end": 167,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L161-L167",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.RefinementGrowingTorus",
        "url": "/verify/taulib/docs/book-i-boundary-refinement-growing-torus/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L161-L167",
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

- Module: [TauLib.BookI.Boundary.RefinementGrowingTorus](/verify/taulib/docs/book-i-boundary-refinement-growing-torus/)
- Source path: [`TauLib/BookI/Boundary/RefinementGrowingTorus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L161-L167)
- Source range: L161-L167
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Refinement projection** from depth `n+1` to depth `n`.

    On crossing: identity.
    On `bSide ⟨k, hk⟩` at depth `n+1` (so `hk : k < n + 2`): map to
    `bSide ⟨k % (n+1), _⟩` at depth `n`.
    Symmetric for cSide.

    The mod-reduction yields a structurally non-trivial projection
    while preserving the lobe label and σ-equivariance. -/
```

## Source Excerpt

```lean
def RefinedTorusDefect.proj {n : Nat} :
    RefinedTorusDefect (n + 1) → RefinedTorusDefect n
  | RefinedTorusDefect.crossing => RefinedTorusDefect.crossing
  | RefinedTorusDefect.bSide ⟨k, _⟩ =>
    RefinedTorusDefect.bSide ⟨k % (n + 1), Nat.mod_lt _ (Nat.succ_pos n)⟩
  | RefinedTorusDefect.cSide ⟨k, _⟩ =>
    RefinedTorusDefect.cSide ⟨k % (n + 1), Nat.mod_lt _ (Nat.succ_pos n)⟩
```

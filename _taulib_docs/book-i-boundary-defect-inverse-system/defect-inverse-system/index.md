---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectInverseSystem",
  "permalink": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/defect-inverse-system/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Boundary.DefectInverseSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.DefectInverseSystem::DefectInverseSystem",
  "declaration_slug": "defect-inverse-system",
  "kind": "structure",
  "name": "DefectInverseSystem",
  "module_name": "TauLib.BookI.Boundary.DefectInverseSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/",
  "source_line_start": 143,
  "source_line_end": 159,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L143-L159",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L143-L159",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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
- Source path: [`TauLib/BookI/Boundary/DefectInverseSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L143-L159)
- Source range: L143-L159
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **An abstract defect inverse system** (paper §4.1 five-step
    program, Steps 1–4 packaged structurally).

    Captures:
    - Step 1/3: a depth-indexed family of "defect levels"
      (the complement `Δ_n = T_n \ R_n` at every depth).
    - Step 4: refinement-compatibility projections
      `Δ_{n+1} → Δ_n`.
    - Step 5 data (σ-involution): σ acts on every level,
      involutively, and commutes with projections.

    The *geometric* content (what torus, what realised relation,
    what lobe labels) is abstracted away; what remains is the
    inverse-system shape that Wave 8's `OmegaInverseLimit`
    infrastructure consumes.  Consumers plug in specific
    instances (e.g. the τ-circle presentation's refinement
    tower) to recover the full paper §4 construction. -/
```

## Source Excerpt

```lean
structure DefectInverseSystem where
  /-- The defect object at each depth `n ≥ 1`.
      Encodes Step 3's `Δ_n = T_n \ R_n`. -/
  defect_level : Nat → Type
  /-- The refinement projection `Δ_{n+1} → Δ_n` of Step 4.
      Witnesses paper's `lem:defect-compatible`. -/
  proj : ∀ n, defect_level (n + 1) → defect_level n
  /-- The polarity involution σ restricted to depth `n`.
      Step 5 data. -/
  sigma_level : ∀ n, defect_level n → defect_level n
  /-- σ is involutive at every depth: `σ² = id`. -/
  sigma_involutive : ∀ n (x : defect_level n),
    sigma_level n (sigma_level n x) = x
  /-- σ commutes with refinement projection: the key
      compatibility that lifts σ-invariance to the inverse limit. -/
  sigma_commutes_proj : ∀ n (x : defect_level (n + 1)),
    proj n (sigma_level (n + 1) x) = sigma_level n (proj n x)
```

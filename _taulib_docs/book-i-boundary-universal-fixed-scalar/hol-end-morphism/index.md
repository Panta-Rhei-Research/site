---
{
  "projection_kind": "taulib_declaration",
  "title": "HolEndMorphism",
  "permalink": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/hol-end-morphism/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Boundary.UniversalFixedScalar`.",
  "declaration_id": "TauLib.BookI.Boundary.UniversalFixedScalar::HolEndMorphism",
  "declaration_slug": "hol-end-morphism",
  "kind": "structure",
  "name": "HolEndMorphism",
  "module_name": "TauLib.BookI.Boundary.UniversalFixedScalar",
  "module_url": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/",
  "source_line_start": 123,
  "source_line_end": 130,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L123-L130",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.UniversalFixedScalar",
        "url": "/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L123-L130",
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

- Module: [TauLib.BookI.Boundary.UniversalFixedScalar](/verify/taulib/docs/book-i-boundary-universal-fixed-scalar/)
- Source path: [`TauLib/BookI/Boundary/UniversalFixedScalar.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/UniversalFixedScalar.lean#L123-L130)
- Source range: L123-L130
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **A HolEnd_τ morphism on a `DefectInverseSystem`**
    (paper's `HolEnd_τ(ω)` class restricted to the defect tower).

    Packages:
    - `act : D.Thread → D.Thread`: the action on threads.
    - `preserves_sigma_fixed`: σ-equivariance at the thread level —
      σ-fixed threads map to σ-fixed threads (paper Prop 5.6's
      content, built in as a structural field).
    - `preserves_NP` and `preserves_OA`: preservation of the
      paper §5 non-polarity and ω-approach halves.

    σ-equivariance via `σ(f(G)) = f(σ(G))` would require the
    underlying σ-action on arbitrary threads; the preservation
    form `f(σ-fixed) = σ-fixed` is equivalent and cleaner. -/
```

## Source Excerpt

```lean
structure HolEndMorphism (D : DefectInverseSystem) where
  /-- Action on arbitrary threads. -/
  act : D.Thread → D.Thread
  /-- **σ-equivariance** (paper Prop 5.6): σ-fixed threads map
      to σ-fixed threads. -/
  preserves_sigma_fixed : ∀ (t : D.Thread),
    (∀ n, D.sigma_level n (t.point n) = t.point n) →
    (∀ n, D.sigma_level n ((act t).point n) = (act t).point n)
```

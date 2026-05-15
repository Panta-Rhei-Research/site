---
{
  "projection_kind": "taulib_declaration",
  "title": "TauEinstein",
  "permalink": "/corpus/taulib/docs/book-v-gravity-einstein-equation/tau-einstein/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.EinsteinEquation`.",
  "declaration_id": "TauLib.BookV.Gravity.EinsteinEquation::TauEinstein",
  "declaration_slug": "tau-einstein",
  "kind": "structure",
  "name": "TauEinstein",
  "module_name": "TauLib.BookV.Gravity.EinsteinEquation",
  "module_url": "/corpus/taulib/docs/book-v-gravity-einstein-equation/",
  "source_line_start": 194,
  "source_line_end": 205,
  "registry_ids": [
    "V.D06"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L194-L205",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.EinsteinEquation",
        "url": "/corpus/taulib/docs/book-v-gravity-einstein-equation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L194-L205",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Gravity.EinsteinEquation](/corpus/taulib/docs/book-v-gravity-einstein-equation/)
- Source path: [`TauLib/BookV/Gravity/EinsteinEquation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L194-L205)
- Source range: L194-L205
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.D06] Tau-Einstein equation: G_ω(x) = κ_τ · T^mat_ω(x).

    This is a **boundary-character identity** in H_∂[ω], NOT a
    nonlinear PDE. It states that the curvature character equals
    the GR coupling times the matter character.

    Key distinctions from orthodox GR:
    1. Algebraic identity, not differential equation
    2. Boundary determines interior (Hartogs principle)
    3. Unique solution by τ-NF minimization (no gauge freedom)
    4. Backreaction automatic (not extra axiom)

    The structural relation (cross-multiplied):
    curvature_numer · kappa_denom · matter_denom =
    kappa_numer · matter_total · curvature_denom -/
```

## Source Excerpt

```lean
structure TauEinstein where
  /-- The GR coupling constant κ_τ. -/
  kappa : GRCoupling
  /-- The matter character T^mat (3 sector contributions). -/
  matter : MatterCharacter
  /-- The curvature character G. -/
  curvature : CurvatureCharacter
  /-- The Einstein identity: G = κ_τ · T^mat (cross-multiplied). -/
  einstein_identity :
    curvature.numer * kappa.kappa_denom * matter.denom =
    kappa.kappa_numer * matter.total_numer * curvature.denom
  deriving Repr
```

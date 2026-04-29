---
{
  "projection_kind": "taulib_declaration",
  "title": "TauBianchi",
  "permalink": "/verify/taulib/docs/book-v-gravity-einstein-equation/tau-bianchi/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.EinsteinEquation`.",
  "declaration_id": "TauLib.BookV.Gravity.EinsteinEquation::TauBianchi",
  "declaration_slug": "tau-bianchi",
  "kind": "structure",
  "name": "TauBianchi",
  "module_name": "TauLib.BookV.Gravity.EinsteinEquation",
  "module_url": "/verify/taulib/docs/book-v-gravity-einstein-equation/",
  "source_line_start": 221,
  "source_line_end": 226,
  "registry_ids": [
    "V.R01"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L221-L226",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.EinsteinEquation",
        "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L221-L226",
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

- Module: [TauLib.BookV.Gravity.EinsteinEquation](/verify/taulib/docs/book-v-gravity-einstein-equation/)
- Source path: [`TauLib/BookV/Gravity/EinsteinEquation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L221-L226)
- Source range: L221-L226
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.R01] Conservation is a COROLLARY of the tau-Einstein identity,
    NOT an extra axiom.

    ∇ · G = ∇ · (κ_τ · T^mat)

    No admissible refinement can change matter-character without
    compensating curvature change. Backreaction is automatic.

    This structure records the conservation principle for a given
    Einstein system. -/
```

## Source Excerpt

```lean
structure TauBianchi where
  /-- The underlying Einstein system. -/
  einstein : TauEinstein
  /-- Conservation is derived (not postulated). -/
  is_derived : Bool := true
  deriving Repr
```

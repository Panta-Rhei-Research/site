---
{
  "projection_kind": "taulib_declaration",
  "title": "PathOrderedExp",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/path-ordered-exp/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::PathOrderedExp",
  "declaration_slug": "path-ordered-exp",
  "kind": "structure",
  "name": "PathOrderedExp",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 260,
  "source_line_end": 266,
  "registry_ids": [
    "IV.P42"
  ],
  "related_registry_items": [
    {
      "id": "IV.P42",
      "title": "Non-Abelian Holonomy",
      "url": "/registry/object/IV.P42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L260-L266",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance2",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L260-L266",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance2](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L260-L266)
- Source range: L260-L266
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P42` — Non-Abelian Holonomy

## Immediate Comment / Docstring

```lean
/-- [IV.P42] Non-abelian holonomy requires path-ordering:
    Hol(γ) = P exp(i∮_γ A) because [A(s₁), A(s₂)] ≠ 0 in general.
    For abelian U(1), path-ordering is trivial (ordinary exponential). -/
```

## Source Excerpt

```lean
structure PathOrderedExp where
  /-- Whether path-ordering is required. -/
  requires_ordering : Bool
  /-- Whether the gauge group is abelian. -/
  is_abelian : Bool
  /-- For abelian groups, path-ordering is not required. -/
  abelian_no_ordering : is_abelian = true → requires_ordering = false
```

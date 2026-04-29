---
{
  "projection_kind": "taulib_declaration",
  "title": "GenerationMassOrdering",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/generation-mass-ordering/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::GenerationMassOrdering",
  "declaration_slug": "generation-mass-ordering",
  "kind": "structure",
  "name": "GenerationMassOrdering",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 200,
  "source_line_end": 207,
  "registry_ids": [
    "IV.P114"
  ],
  "related_registry_items": [
    {
      "id": "IV.P114",
      "title": "Generation mass ordering",
      "url": "/registry/object/IV.P114/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L200-L207",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.QuarksGluons",
        "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L200-L207",
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

- Module: [TauLib.BookIV.Strong.QuarksGluons](/verify/taulib/docs/book-iv-strong-quarks-gluons/)
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L200-L207)
- Source range: L200-L207
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P114` — Generation mass ordering

## Immediate Comment / Docstring

```lean
/-- [IV.P114] Generation mass ordering (conjectural):
    lambda_crossing < lambda_singleLobe < lambda_fullL
    => m_u < m_c < m_t and m_d < m_s < m_b.

    Scope: conjectural (quantitative mass ratios not yet derived). -/
```

## Source Excerpt

```lean
structure GenerationMassOrdering where
  /-- Mass ordering follows breathing eigenvalue ordering. -/
  follows_eigenvalue : Bool := true
  /-- Scope: tau-effective. -/
  scope : String := "tau-effective"
  /-- Qualitative hierarchy: crossing < singleLobe < fullL. -/
  hierarchy : String := "lambda_crossing < lambda_singleLobe < lambda_fullL"
  deriving Repr
```

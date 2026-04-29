---
{
  "projection_kind": "taulib_declaration",
  "title": "semigroup_12_4",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/semigroup-12-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::semigroup_12_4",
  "declaration_slug": "semigroup-12-4",
  "kind": "theorem",
  "name": "semigroup_12_4",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 312,
  "source_line_end": 313,
  "registry_ids": [
    "II.T28"
  ],
  "related_registry_items": [
    {
      "id": "II.T28",
      "title": "B/C Asymmetry Implies Time Arrow",
      "url": "/registry/object/II.T28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L312-L313",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.EvolutionOperator",
        "url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L312-L313",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookII.Hartogs.EvolutionOperator](/verify/taulib/docs/book-ii-hartogs-evolution-operator/)
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L312-L313)
- Source range: L312-L313
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T28` — B/C Asymmetry Implies Time Arrow

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- Evolution semigroup [II.T28]
```

## Source Excerpt

```lean
theorem semigroup_12_4 :
    evolution_semigroup_check 12 4 = true := by native_decide
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "asymmetry_witness",
  "permalink": "/corpus/taulib/docs/book-ii-hartogs-evolution-operator/asymmetry-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::asymmetry_witness",
  "declaration_slug": "asymmetry-witness",
  "kind": "theorem",
  "name": "asymmetry_witness",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/corpus/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 322,
  "source_line_end": 323,
  "registry_ids": [
    "II.D38"
  ],
  "related_registry_items": [
    {
      "id": "II.D38",
      "title": "Causal Arrow",
      "url": "/registry/object/II.D38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L322-L323",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.EvolutionOperator",
        "url": "/corpus/taulib/docs/book-ii-hartogs-evolution-operator/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L322-L323",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookII.Hartogs.EvolutionOperator](/corpus/taulib/docs/book-ii-hartogs-evolution-operator/)
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L322-L323)
- Source range: L322-L323
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.D38` — Causal Arrow

## Immediate Comment / Docstring

```lean
-- Causal arrow [II.D38]
```

## Source Excerpt

```lean
theorem asymmetry_witness :
    bc_asymmetry_witness = true := by native_decide
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "evolution_identity_thm",
  "permalink": "/corpus/taulib/docs/book-ii-hartogs-evolution-operator/evolution-identity-thm/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::evolution_identity_thm",
  "declaration_slug": "evolution-identity-thm",
  "kind": "theorem",
  "name": "evolution_identity_thm",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/corpus/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 149,
  "source_line_end": 151,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L149-L151",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L149-L151",
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
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L149-L151)
- Source range: L149-L151
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Evolution identity theorem (formal):
    reduce(reduce(x, n), n) = reduce(x, n). -/
```

## Source Excerpt

```lean
theorem evolution_identity_thm (x n : TauIdx) :
    reduce (reduce x n) n = reduce x n := by
  exact reduction_compat x (Nat.le_refl n)
```

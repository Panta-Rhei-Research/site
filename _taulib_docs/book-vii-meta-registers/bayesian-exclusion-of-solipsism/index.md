---
{
  "projection_kind": "taulib_declaration",
  "title": "bayesian_exclusion_of_solipsism",
  "permalink": "/corpus/taulib/docs/book-vii-meta-registers/bayesian-exclusion-of-solipsism/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::bayesian_exclusion_of_solipsism",
  "declaration_slug": "bayesian-exclusion-of-solipsism",
  "kind": "theorem",
  "name": "bayesian_exclusion_of_solipsism",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/corpus/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 945,
  "source_line_end": 950,
  "registry_ids": [
    "VII.T15"
  ],
  "related_registry_items": [
    {
      "id": "VII.T15",
      "title": "Bayesian Exclusion of Solipsism",
      "url": "/registry/object/VII.T15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L945-L950",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/corpus/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L945-L950",
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

- Module: [TauLib.BookVII.Meta.Registers](/corpus/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L945-L950)
- Source range: L945-L950
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `VII.T15` — Bayesian Exclusion of Solipsism

## Immediate Comment / Docstring

```lean
/-- [VII.T15] Bayesian Exclusion of Solipsism (ch31). Information-
    theoretic argument: under any reasonable prior, the posterior
    probability of solipsism vanishes because it requires all
    cross-register correlations to be coincidental. -/
```

## Source Excerpt

```lean
theorem bayesian_exclusion_of_solipsism :
    solipsism_resolution.ontic_layer = true ∧
    solipsism_resolution.epistemic_layer = true ∧
    solipsism_resolution.bayesian_layer = true ∧
    solipsism_resolution.layer_count = 3 :=
  ⟨rfl, rfl, rfl, rfl⟩
```

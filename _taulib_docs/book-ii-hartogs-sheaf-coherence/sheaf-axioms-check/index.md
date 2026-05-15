---
{
  "projection_kind": "taulib_declaration",
  "title": "sheaf_axioms_check",
  "permalink": "/corpus/taulib/docs/book-ii-hartogs-sheaf-coherence/sheaf-axioms-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::sheaf_axioms_check",
  "declaration_slug": "sheaf-axioms-check",
  "kind": "def",
  "name": "sheaf_axioms_check",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/corpus/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 312,
  "source_line_end": 313,
  "registry_ids": [
    "II.T32"
  ],
  "related_registry_items": [
    {
      "id": "II.T32",
      "title": "Sheaf Axioms",
      "url": "/registry/object/II.T32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L312-L313",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/corpus/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L312-L313",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/corpus/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L312-L313)
- Source range: L312-L313
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.T32` — Sheaf Axioms

## Immediate Comment / Docstring

```lean
/-- [II.T32] Full sheaf axioms check: both locality and gluing. -/
```

## Source Excerpt

```lean
def sheaf_axioms_check (k_max : TauIdx) : Bool :=
  locality_check k_max && gluing_axiom_check k_max
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "dag_strongly_normalising_statement",
  "permalink": "/corpus/taulib/docs/book-i-addressability-hinge-integration/dag-strongly-normalising-statement/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.HingeIntegration`.",
  "declaration_id": "TauLib.BookI.Addressability.HingeIntegration::dag_strongly_normalising_statement",
  "declaration_slug": "dag-strongly-normalising-statement",
  "kind": "theorem",
  "name": "dag_strongly_normalising_statement",
  "module_name": "TauLib.BookI.Addressability.HingeIntegration",
  "module_url": "/corpus/taulib/docs/book-i-addressability-hinge-integration/",
  "source_line_start": 170,
  "source_line_end": 172,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L170-L172",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.HingeIntegration",
        "url": "/corpus/taulib/docs/book-i-addressability-hinge-integration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L170-L172",
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

- Module: [TauLib.BookI.Addressability.HingeIntegration](/corpus/taulib/docs/book-i-addressability-hinge-integration/)
- Source path: [`TauLib/BookI/Addressability/HingeIntegration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L170-L172)
- Source range: L170-L172
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem 3 (Genealogical DAG) — strong normalisation**:
    every Program reduces to a NormalForm in finitely many steps,
    captured by the fact that `normalize` is a total function
    (no divergence). -/
```

## Source Excerpt

```lean
theorem dag_strongly_normalising_statement (p : Program) :
    ∃ nf : NormalForm, normalize p = nf :=
  ⟨normalize p, rfl⟩
```

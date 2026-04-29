---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_normalisation_statement",
  "permalink": "/verify/taulib/docs/book-i-addressability-hinge-integration/canonical-normalisation-statement/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.HingeIntegration`.",
  "declaration_id": "TauLib.BookI.Addressability.HingeIntegration::canonical_normalisation_statement",
  "declaration_slug": "canonical-normalisation-statement",
  "kind": "theorem",
  "name": "canonical_normalisation_statement",
  "module_name": "TauLib.BookI.Addressability.HingeIntegration",
  "module_url": "/verify/taulib/docs/book-i-addressability-hinge-integration/",
  "source_line_start": 105,
  "source_line_end": 107,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L105-L107",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.HingeIntegration",
        "url": "/verify/taulib/docs/book-i-addressability-hinge-integration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L105-L107",
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

- Module: [TauLib.BookI.Addressability.HingeIntegration](/verify/taulib/docs/book-i-addressability-hinge-integration/)
- Source path: [`TauLib/BookI/Addressability/HingeIntegration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L105-L107)
- Source range: L105-L107
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem 1 (Canonical Normalisation)** restated for
    paper-bundle alignment.

    Every Program reduces to a unique NormalForm via Wave 5's
    `normalize` function.  The map is idempotent at the structural
    level: applying normalize twice produces the same NormalForm
    (since NormalForm is the target type of normalize).

    The full "tEq-preserving idempotent surjective" claim from the
    paper is captured by the existing Wave 5 theorems
    (`tauEq_refl`, `tauEq_implies_execNF_eq`, etc.). -/
```

## Source Excerpt

```lean
theorem canonical_normalisation_statement (p : Program) :
    ∃ nf : NormalForm, normalize p = nf :=
  ⟨normalize p, rfl⟩
```

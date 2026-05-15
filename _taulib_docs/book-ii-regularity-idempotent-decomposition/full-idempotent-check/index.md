---
{
  "projection_kind": "taulib_declaration",
  "title": "full_idempotent_check",
  "permalink": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/full-idempotent-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.IdempotentDecomposition`.",
  "declaration_id": "TauLib.BookII.Regularity.IdempotentDecomposition::full_idempotent_check",
  "declaration_slug": "full-idempotent-check",
  "kind": "def",
  "name": "full_idempotent_check",
  "module_name": "TauLib.BookII.Regularity.IdempotentDecomposition",
  "module_url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/",
  "source_line_start": 262,
  "source_line_end": 266,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L262-L266",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.IdempotentDecomposition",
        "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L262-L266",
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

- Module: [TauLib.BookII.Regularity.IdempotentDecomposition](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/)
- Source path: [`TauLib/BookII/Regularity/IdempotentDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L262-L266)
- Source range: L262-L266
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.L07 + II.D48 + II.P10] Complete idempotent decomposition verification. -/
```

## Source Excerpt

```lean
def full_idempotent_check (bound db : TauIdx) : Bool :=
  decompose_recovery_check bound &&
  stagefun_decompose_check bound db &&
  decompose_functorial_check bound db &&
  decompose_functorial_extended bound db
```

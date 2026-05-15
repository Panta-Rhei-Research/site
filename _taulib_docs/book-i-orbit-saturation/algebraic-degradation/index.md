---
{
  "projection_kind": "taulib_declaration",
  "title": "AlgebraicDegradation",
  "permalink": "/corpus/taulib/docs/book-i-orbit-saturation/algebraic-degradation/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Orbit.Saturation`.",
  "declaration_id": "TauLib.BookI.Orbit.Saturation::AlgebraicDegradation",
  "declaration_slug": "algebraic-degradation",
  "kind": "structure",
  "name": "AlgebraicDegradation",
  "module_name": "TauLib.BookI.Orbit.Saturation",
  "module_url": "/corpus/taulib/docs/book-i-orbit-saturation/",
  "source_line_start": 83,
  "source_line_end": 86,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L83-L86",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Saturation",
        "url": "/corpus/taulib/docs/book-i-orbit-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L83-L86",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookI.Orbit.Saturation](/corpus/taulib/docs/book-i-orbit-saturation/)
- Source path: [`TauLib/BookI/Orbit/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L83-L86)
- Source range: L83-L86
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tetration is algebraically degraded: non-commutative, non-associative,
    no left identity ≥ 2. This is the algebraic obstruction to canonicality
    at the 4th operation level. -/
```

## Source Excerpt

```lean
structure AlgebraicDegradation where
  non_comm : tetration 2 3 ≠ tetration 3 2
  non_assoc : tetration (tetration 2 2) 2 ≠ tetration 2 (tetration 2 2)
  no_left_identity : ¬∃ e, e ≥ 2 ∧ ∀ n, n ≥ 1 → tetration e n = n
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "is_stable",
  "permalink": "/corpus/taulib/docs/book-iii-physics-positive-regularity/is-stable/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.PositiveRegularity`.",
  "declaration_id": "TauLib.BookIII.Physics.PositiveRegularity::is_stable",
  "declaration_slug": "is-stable",
  "kind": "def",
  "name": "is_stable",
  "module_name": "TauLib.BookIII.Physics.PositiveRegularity",
  "module_url": "/corpus/taulib/docs/book-iii-physics-positive-regularity/",
  "source_line_start": 167,
  "source_line_end": 168,
  "registry_ids": [
    "III.P15"
  ],
  "related_registry_items": [
    {
      "id": "III.P15",
      "title": "3-Condition Sufficiency",
      "url": "/registry/object/III.P15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L167-L168",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.PositiveRegularity",
        "url": "/corpus/taulib/docs/book-iii-physics-positive-regularity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L167-L168",
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

- Module: [TauLib.BookIII.Physics.PositiveRegularity](/corpus/taulib/docs/book-iii-physics-positive-regularity/)
- Source path: [`TauLib/BookIII/Physics/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L167-L168)
- Source range: L167-L168
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.P15` — 3-Condition Sufficiency

## Immediate Comment / Docstring

```lean
/-- [III.P15] Stability criterion: a fluid datum is stable iff its
    defect functional is zero. This is a computable predicate. -/
```

## Source Excerpt

```lean
def is_stable (k : TauIdx) : Bool :=
  defect_functional k == 0
```

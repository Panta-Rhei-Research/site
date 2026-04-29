---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_basis_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/canonical-basis-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::canonical_basis_check",
  "declaration_slug": "canonical-basis-check",
  "kind": "def",
  "name": "canonical_basis_check",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 175,
  "source_line_end": 178,
  "registry_ids": [
    "II.D45"
  ],
  "related_registry_items": [
    {
      "id": "II.D45",
      "title": "Canonical Holomorphic Basis",
      "url": "/registry/object/II.D45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L175-L178",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CanonicalBasis",
        "url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L175-L178",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookII.Hartogs.CanonicalBasis](/verify/taulib/docs/book-ii-hartogs-canonical-basis/)
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L175-L178)
- Source range: L175-L178
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D45` — Canonical Holomorphic Basis

## Immediate Comment / Docstring

```lean
/-- [II.D45] Full canonical basis verification:
    orthogonality + completeness + independence. -/
```

## Source Excerpt

```lean
def canonical_basis_check (k_max bound : TauIdx) : Bool :=
  basis_orthogonality_check k_max bound &&
  basis_completeness_check k_max bound &&
  basis_independence_check k_max
```
